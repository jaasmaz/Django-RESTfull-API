from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def product_list(request):
    return Response('Hello')


# Create your views here.
def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Jaz'})


def say_hi(request):
    return HttpResponse('Hi')

