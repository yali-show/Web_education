from django.shortcuts import render

# Create your views here.


def items(request, *args, **kwargs):
    return render(request, 'items/index.html')
