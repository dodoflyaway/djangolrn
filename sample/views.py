from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todolist,Item,showthis
from .forms import CreateNewList


def index(response, id):
	ls = Todolist.objects.get(id=id)
	if response.method == "POST":
		print(response.POST)
		if response.POST.get("save"):
			for item in ls.item_set.all():
				if response.POST.get("c" + str(item.id)) == "clicked":
					item.complete = True
				else:
					item.complete = False

				item.save()

		elif response.POST.get("newItem"):
			txt = response.POST.get("new")
			if len(txt) > 2:
				ls.item_set.create(text=txt,complete=False)
			else:
				print("invalid")


	return render(response, "sample/list.html", {"ls":ls})



def indexall(response):
	ls = Todolist.objects.all()
	return render(response, "sample/home.html", {})


def home(response):
	return render(response, "sample/home.html", {})



def create(response):
	ls = Todolist.objects.all()
	if response.method == "POST":
		form = CreateNewList(response.POST)
		if form.is_valid():
			n = form.cleaned_data["name"]
			t = Todolist(name=n)
			t.save()
		return HttpResponseRedirect("/%i" %t.id)


	else:
		form = CreateNewList()
	return render(response, "sample/create.html", {"form":form,"ls":ls})

