from django.shortcuts import render, redirect

from products.utils import generate_id, write, read


def products_list(request):
    products = read(filename="products.csv")
    context = {"products": products}
    return render(request, 'products.html', context)


def add_product(request):
    if request.method == "POST":
        print("Hellloooooooooo")
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        new_id = generate_id(filename='products.csv')
        data = [new_id, name, quantity]
        write(filename="products.csv", data=data, mode="a")
        return redirect('products:list')
    else:
        return render(request, 'add-product.html')


def update_product(request, product_id):
    # find product
    return render(request, 'update-product.html')


def delete_product(request, product_id):
    # find product
    return render(request, 'delete-product.html')
