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

def edit(request, suspect_id):
    if request.method == 'POST':
        print(request.POST.get(suspect_id))
        print(request.POST.get('suspect_name_1'))
        print(request.POST.get('suspect_hair_1'))
        print(request.POST.get('suspect_attire_1'))
        print(request.POST.get('suspect_room_1'))

    suspect_list = Suspect.objects.order_by('id');
    template = loader.get_template('murder_at_metro_club/edit.html')
    context = {
        'suspect_list': suspect_list
    }
    return HttpResponse(template.render(context, request))

def results(request, suspect_id):
    response = "You are looking at the results of Suspect %s."
    return HttpResponse(response % suspect_id)
