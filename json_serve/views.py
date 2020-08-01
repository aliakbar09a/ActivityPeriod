from django.shortcuts import render
from django.http import JsonResponse

def send(request):
    
    data = {'first': {'name': 'Peter', 'email': 'peter@example.org'},
            'second': {'name': 'Julia', 'email': 'julia@example.org'}}

    return JsonResponse(data, safe=False)