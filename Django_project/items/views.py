from django.shortcuts import render
from items.models import Item
from items.forms import ItemForm
from items.model_forms import ItemModelForm

def items(request, *args, **kwargs):

    if request.method == 'POST':
        form = ItemModelForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = ItemModelForm()

    context = {'items': Item.objects.all(), 'form': form}

    return render(request, 'items/index.html', context=context)
