# paths for differents webpages(views)
from django.urls import path
from . import views

urlpatterns = [
    #go to the views of the path
    path("home/", views.index, name= 'index'),
    path("momo/", views.v1, name= 'view 1'),
    # path("start/", views.index, name= 'index')
]