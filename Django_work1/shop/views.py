from django.shortcuts import render


def index(request):
    goods = {'goods': 'shop stuf'}
    return render(request, 'shop_goods/index.html', goods)
