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
    return HttpResponse( "You're looking at the details for Suspect %s. %s"
        % (suspect_id, suspect))

def results(request, suspect_id):
    response = "You are looking at the results of Suspect %s."
    return HttpResponse(response % suspect_id)

def edit(request, suspect_id):
    return HttpResponse("You are now editing information for Suspect %s." % suspect_id)
