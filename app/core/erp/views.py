from django.shortcuts import render
from core.erp.models import Category,Product
# Create your views here.
def myfirtsview(request):
    data ={'name':'andres',
            'categories': Category.objects.all()
            }
    return render(request, 'index.html', data)
def mysecondview(request):
    data ={'name':'andres',
            'products': Product.objects.all()
            }
    return render(request, 'second.html', data)
