from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def myfirtsview(request):
    data ={'name':'andres'}
    return render(request, 'index.html', data)
