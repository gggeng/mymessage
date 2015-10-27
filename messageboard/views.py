from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.list import ListView

from .models import Msg
from forms import MsgCreateForm

# Create your views here.

def msg_list_page(request):
    posts = Msg.objects.all()
    return render_to_response('msg_list_page.html', {'posts':posts})

def msg_create_page(request):
    model = Msg
    if request.method == 'POST':
        form = MsgCreateForm(request.POST)
        if form.is_valid():
            newmessage = Msg(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
            )
            newmessage.save()
        return HttpResponseRedirect('/')
    else:
        form = MsgCreateForm()
    variables = RequestContext(request, {'form':form})
    return render_to_response('msg_create_page.html', variables)