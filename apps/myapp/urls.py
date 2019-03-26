from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('wish_item/<id>', views.wish_item),
    path('addwish/<id>', views.addwish),
    path('delete/<id>', views.delete),
    path('remove/<id>', views.remove),
    path('create', views.create),
    path('processwish_item', views.processwish_item)
]
