from django.db import models
import re
import datetime
import bcrypt

class UserManager(models.Manager):
    def reg_validator(self, form):

        errors = {}
        
        name = form['name']
        uname = form['uname']
        password = form['password']
        confirm_password = form['confirm_password']
        date_hired = form['date_hired']
        print(date_hired)
        if len(name) < 3:
            errors['name'] = "Name cannot be blank and must be more then 3 characters"
        elif not name.isalpha():
            errors['name'] = "Name cannot contain number or special characters!"
        if len(uname) < 3:
            errors['uname'] = "Username cannot be blank and must be more then 3 characters"
        else:
            users = User.objects.filter(uname=uname)
            if len(users) > 0:
                errors['uname'] = "Username already exists. Please login."

        if len(password) < 8:
            errors['password'] = "Password must be at least 8 characters"
        elif password != confirm_password:
            errors['confirm_password'] = "Passwords do not match"

        if not date_hired:
            errors['date_hired'] = "Please enter the date you were hired"
        elif date_hired > str(datetime.datetime.now()):
            errors['date_hired'] = "Date hired has to be in the past"
        

        return errors
            
    
    def loginvalidator(self, form):
        errors = {}
        uname = form['uname']
        password = form['password']
        if len(uname) < 0:
            errors["uname"] = "Please enter a Username"
        elif len(User.objects.filter(uname = uname)) < 1:
            errors['uname'] = "Username is not in database please register!"
        else:
            if not bcrypt.checkpw(password.encode(), User.objects.get(uname = uname).password.encode()):
                errors['uname'] = "Password does not match what is in database!"
                
        return errors


class WishlistManager(models.Manager):
    def wishlist_validator(self, form):

        errors = {} 
        item = form['item']
        # print(form)  print form to terminal for debugging
        if len(item) < 3:
            errors["item"] = "Must provide item name longer then three characters"
        return errors       


class User(models.Model):
    name = models.CharField(max_length=255)
    uname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    """uploaded_movies get list of uploaded movies for user"""
    """favorites get list of favorited movies from user"""

    objects = UserManager()
class Wishlist(models.Model):
    item = models.CharField(max_length=255)
    addedby = models.ForeignKey(User, related_name="uploaded_wishlist", on_delete=models.CASCADE)
    wishlists=models.ManyToManyField(User,related_name="wishlists")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    objects = WishlistManager()

