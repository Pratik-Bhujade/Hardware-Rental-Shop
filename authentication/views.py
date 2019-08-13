# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout, authenticate
from .forms import *
from staff.models import *

# Create your views here.

def home(request):
	tools = Tool.objects.exclude(quantity = 0)
	if request.user.is_staff:
		return render(request,'all_tools.html',{"tools":tools})
	return render(request,'index.html',{"tools":tools})

def tool(request,type):
	tools = Tool.objects.filter(tooltype = type)
	return render(request, 'tools.html',{'tools':tools})

def signup(request):
	args = {}
	form = SignUpForm(request.POST)
	args["form"] = form
	print(request.method)
	if request.method == "POST":
		if form.is_valid():
			user = form.save()
			return redirect('/login')
		print(form.errors)
        # else:
		# 	return HttpResponse("Check form data")
	return render(request, 'signup.html', args)

class SignIn(LoginView):
	template_name = 'login.html'

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("/")
		return HttpResponse("Error")


class SignOut(LogoutView):
	pass
