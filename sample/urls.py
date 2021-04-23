from django.urls import path
from . import views #to import the funtions from views.py

urlpatterns = [
 path("<int:id>",views.index,name="index"),
 path("indexall",views.indexall,name="indexall"),
 path("home/",views.home,name="home"),
 path("create/",views.create,name="create"),
 
]