from django.contrib import admin
from .models import Todolist,Item,showthis

# Register your models here.
admin.site.register(Todolist)
admin.site.register(Item)
admin.site.register(showthis)
