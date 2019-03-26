from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt



def index(request):
    return render(request, "index.html")


def register(request):
    print('inside register method in views')
    result = User.objects.reg_validator(request.POST)
    print('back inside register in views')
    print(result)
    if len(result) > 0:
        for key, value in result.items():
            messages.add_message(request, messages.ERROR, value)
        return redirect('/')
    else:
        hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST['name'], uname=request.POST['uname'],  password=hash.decode(), date_hired = request.POST['date_hired'])
        print(user.id)
        request.session['userid'] = user.id
        return redirect('/dashboard')


def login(request):
    result = User.objects.loginvalidator(request.POST)
    if len(result) > 0:
        for key, value in result.items():
            messages.add_message(request, messages.ERROR, value)
        return redirect('/')
    else:
        user = User.objects.get(uname = request.POST['uname'])
        request.session['userid'] = user.id
        return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    if 'userid' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['userid'])
        user_wishlists=user.wishlists.all()
        others_wishlist=[]
        all_wishlists=Wishlist.objects.all()
        for i in all_wishlists:
            if i not in user_wishlists:
                others_wishlist.append(i)
        context = {
            'user': user,
            'user_wishlists': user_wishlists,
            'others_wishlist': others_wishlist
            
        }
    return render(request, "dashboard.html", context)

def wish_item(request, id):
    context={
        "user_wishlist" : Wishlist.objects.get(id=id),
        "wishlists": Wishlist.objects.get(id=id).wishlists.all()
    }
    return render(request, "wish_item.html", context)

def create(request):
    return render(request, "create.html")


def addwish(request, id):
    user = User.objects.get(id = request.session['userid'])
    user_wishlist=Wishlist.objects.get(id=id)
    user.wishlists.add(user_wishlist)
    return redirect('/dashboard')


def processwish_item(request):
    result = Wishlist.objects.wishlist_validator(request.POST)
    print(result)
    if len(result) > 0:
        for key, value in result.items():
            messages.add_message(request, messages.ERROR, value)
        return redirect('/create')
    else:
        user_wishlist = Wishlist.objects.create(item=request.POST['item'], addedby_id=request.session['userid'])
        user = User.objects.get(id = request.session['userid'])
        user.wishlists.add(user_wishlist)
    return redirect("/dashboard")

def remove(request, id):
    user = User.objects.get(id = request.session['userid'])
    user_wishlist=Wishlist.objects.get(id=id)
    user.wishlists.remove(user_wishlist)
    return redirect('/dashboard')

def delete(request, id):
    w=Wishlist.objects.get(id=id)
    w.delete()
    return redirect('/dashboard')







