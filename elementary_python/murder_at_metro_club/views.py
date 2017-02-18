from django.http import HttpResponse
from .models import Suspect
from django.template import loader

# Create your views here.
def index( request ):
    suspect_list = Suspect.objects.order_by('id');
    template = loader.get_template('murder_at_metro_club/index.html')
    context = {
        'suspect_list': suspect_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, suspect_id):
    suspect = Suspect.objects.get(pk=suspect_id)
    template = loader.get_template('murder_at_metro_club/details.html')
    context = {
        'suspect': suspect
    }
    return HttpResponse(template.render(context, request))

def edit(request):
    suspect_list = Suspect.objects.order_by('id');
    murderer = ''
    for suspect in suspect_list:
        if request.method == 'POST':
            suspect.id = request.POST.get(str(suspect.id))
            suspect.name = request.POST.get("suspect_name_" + str(suspect.id))
            suspect.hair = request.POST.get("suspect_hair_" + str(suspect.id))
            suspect.attire = request.POST.get("suspect_attire_" + str(suspect.id))
            suspect.room = request.POST.get("suspect_room_" + str(suspect.id))
            if suspect.room == '':
                suspect.room = 0
            if (suspect.hair.lower() == 'brown' and
            suspect.attire.lower() == 'pince-nez' and
            suspect.room == 10):
                suspect.is_murderer = True
            else:
                suspect.is_murderer = False
            suspect.save()

        if suspect.is_murderer == True:
            murderer = suspect.name

    template = loader.get_template('murder_at_metro_club/edit.html')
    context = {
        'suspect_list': suspect_list,
        'murderer': murderer
    }
    return HttpResponse(template.render(context, request))

def results(request, suspect_id):
    response = "You are looking at the results of Suspect %s."
    return HttpResponse(response % suspect_id)
