from django.http import Http404
from django.shortcuts import redirect, render
from numpy import product

from shop.form import ProductForm
from .models import Product

# Create your views here.


def index(request):
    try:
        product_list = Product.objects.all()
        context = {
            'products': product_list,
        }
    except:
        raise Http404("Product does not exist")
    return render(request, 'shop/index.html', context)


def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        context = {
            'product': product,
            'range': range(product.quantity)
        }
    except Product.DoesNotExist:
        raise Http404("This product doesn't exist")
    return render(request, 'shop/detail.html', context)


def create(request):
    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('/shop/')
            except:
                pass
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'shop/create.html', context)


def edit(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("This product doesn't exist")

    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            try:
                form.save()
                return redirect('/shop/')
            except:
                pass
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'shop/edit.html', context)


def delete(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("This product doesn't exist")
    product.delete()

    context = {
        'product': product,
    }
    return render(request, 'shop/delete.html', context)


def buy(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.quantity -= 1
        product.save()
        print(product.quantity)
        redirect("/shop/")
    except Product.DoesNotExist:
        raise Http404("This product doesn't exist")

    context = {
        'product': product,
    }
    return render(request, 'shop/buy.html', context)
