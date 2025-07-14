from django.shortcuts import render, redirect

from products.models import Products


def products_list(request):
    products = Products.objects.all()
    q = request.GET.get('q')
    if q:
        products = products.filter(name__icontains=q)

    context = {"products": products}
    return render(request, 'products.html', context)


def products_detail(request, pk):
    product = Products.objects.filter(id=pk)
    if product.exists():
        context = {"product": product.first()}
        return render(request, 'product-detail.html', context)
    else:
        return render(request, '404.html')


def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        Products.objects.create(
            name=name, quantity=quantity, image=image, description=description
        )
        return redirect('products:list')
    else:
        return render(request, 'add-product.html')


def update_product(request, pk):
    product = Products.objects.filter(id=pk).first()
    if not product:
        return render(request, '404.html')

    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        product.name = name
        product.quantity = quantity
        product.save()

    return render(
        request, 'update-product.html',
        context={"product": product}
    )


def delete_product(request, pk):
    product = Products.objects.filter(id=pk).first()
    if not product:
        return render(request, '404.html')
    if request.method == "POST":
        product.delete()
        return redirect("products:list")
    else:
        return render(
            request, 'delete-product.html',
            context={"product": product})
