from django.shortcuts import render
from rest_framework.response import Response

# views for testing.
def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Jaz'})


def say_hi(request):
    return Response('Hi')

