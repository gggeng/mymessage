from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import list

# Create your views here.
ITEMS_PER_PAGE = 10
def msg_list_page(request):
    return HttpResponse('Hello, this is my message board.')