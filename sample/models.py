from django.db import models

# Create your models here.

class Todolist(models.Model):
	name = models.CharField(max_length=250)


	def __str__(self):
		return self.name



class Item(models.Model):
	todolist = models.ForeignKey(Todolist,on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text



class showthis(models.Model):
	tasks = models.ForeignKey(Todolist,on_delete=models.CASCADE) #related_name=x
	user_name = models.CharField(max_length=150)

	def __str__(self):
		return self.user_name

		#from sample.models import Todolist,Item,user
		#ls = Todolist.objects.all()
		#ls = Todolist.objects.get(id=2)
		#user.objects.create(tasks=ls,user_name="monis")


