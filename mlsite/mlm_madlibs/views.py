from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .mlm_model import *

def index(request):
    #template = loader.get_template("mlm_madlibs/index.html")
    if request.method=='POST':
        g=get_masked_guesses(request.POST['text'],model)
        pred=show_all_guesses(request.POST['text'],g)
        print(pred)
        context={'original':request.POST['text'],'text':[{'type':'list','value':[z.replace('##','') for z in _]} if type(_)==list else {'type':'word','value':_} for _ in pred[1:-1]]}
    else:
        context=dict()
    return render(request, "mlm_madlibs/index.html", context)
    #return HttpResponse(template.render(context, request))