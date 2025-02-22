#!/ismailmwarumba/bin/env python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   context_dict ={'boldmessage':'Crunchy, creamy ,cookie, candy, cupcake! '}
   return render(request, 'bambakofi/index.html', context=context_dict)
def about(request):
   context_dict ={'boldmessage':'This tutorial has been put together by Ismail '}
   return render(request, 'bambakofi/about.html', context=context_dict)