from django.shortcuts import render
from django.shortcuts import redirect
from .forms import RegisterForm
# Create your views here.

def register(response):

	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
		return redirect("/create")
	else:
		form = RegisterForm()

	return render(response, "register/register.html" ,{"form":form})
