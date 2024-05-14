from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .mlm_model import *

def index(request):
    #template = loader.get_template("mlm_madlibs/index.html")
    if request.method=='POST':
        if request.POST['form_type']=='predict_masks':
            g=get_masked_guesses(request.POST['text'],model)
            pred=show_all_guesses(request.POST['text'],g)
            print([type(i) for i in pred])
            context={'original':request.POST['text'],'text':[{'type':'list','value':[z[0] for z in _]} if type(_)==tuple else {'type':'word','value':_} for _ in pred]}
        elif request.POST['form_type']=='resolve_masks':
            print(request.POST)
            words=[request.POST[_] for _ in sorted([i for i in request.POST.keys() if 'word_' in i or 'mask_' in i],key=lambda x:int(x[x.index('_')+1:]))]
            context={'original':retokenize(' '.join(words).replace(' ##',''))}
    else:
        context=dict()
    return render(request, "mlm_madlibs/index.html", context)
    #return HttpResponse(template.render(context, request))