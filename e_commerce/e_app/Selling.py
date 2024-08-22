from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import *
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .product_seller import * 


def login(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        print(type(email), type(password))
        user = auth_authenticate(request, username= email, password = password)
        print(user) 
        if user is not None:
            auth_login(request, user)    
            owner=get_object_or_404(Seller_reg,Seller_email= email)
            return redirect("/my_products/",owner=email)

        else:
            msg="Invalid email id or Password."
            return render(request,"failed.html",{"msg":msg})

    return render(request, "pslogin.html")

@login_required(login_url="/login/")
def postproduct(request,email):

    sel=get_object_or_404(Seller_reg,Seller_email=email)

    if request.method == "POST":
        prname= request.POST.get("product_name")
        prphoto= request.FILES.get("product_photo")
        specfi= request.POST.get("spec")
        qty= request.POST.get("qty")
        price= request.POST.get("price")

        products.objects.create(Product= prname, product_Photo=prphoto, Seller_email = email,
                                Specification=specfi, Quantity= qty, Price=price, Seller=sel)
        return redirect("/my_products/",email=email)

    return render(request,"sales.html", {"sel":sel})

@login_required(login_url="/login/")
def my_products(request, email):
    p_val=products.objects.filter(Seller_email = email)
    print(p_val)
    s_sel=get_object_or_404(Seller_reg,Seller_email = email)
    if request.method == "POST":  
        return render(request, "my_views.html",{"p_val":p_val, "s_sel":s_sel})
    return HttpResponse("Failed")

@login_required(login_url="/login/")
def pro_update(request,id):
    pro=get_object_or_404(products,No=id)
    sal=get_object_or_404(Seller_reg,Seller_email=pro.Seller_email)

    if request.method == "POST": 
        pro.Product= request.POST.get("product_name")
        pro.product_Photo= request.FILES.get("product_photo")
        pro.Specification= request.POST.get("spec")
        pro.Quantity= request.POST.get("qty")
        pro.Price= request.POST.get("price")

        pro.save()
        return redirect("/myview/")     


    return render(request, "update_pro.html", {"pro":pro, "sal":sal})

@login_required(login_url="/login/")
def pro_delete(request,id):
    
    dl=get_object_or_404(products,No=id)
    if request.method == "POST":
        dl.delete()
        return HttpResponse("Product deleted succesfully.")
    
@login_required(login_url="/login/")
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("/home")
    