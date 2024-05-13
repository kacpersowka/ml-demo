from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .mlm_model import *

def index(request):
    #template = loader.get_template("mlm_madlibs/index.html")
    if request.method=='POST':
        g=get_masked_guesses(request.POST['text'],model)
        pred=show_guess(request.POST['text'],g)
        context={'text':pred}
    else:
        context=dict()
    return render(request, "mlm_madlibs/index.html", context)
    #return HttpResponse(template.render(context, request))