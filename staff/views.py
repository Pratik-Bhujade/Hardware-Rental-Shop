# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *
# Create your views here.
def insert(request):
    if request.user.is_staff:
        args = {}
        form = ToolForm(request.POST)
        args["form"] = form
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("/")
            else:
                tool = Tool.objects.get(name = request.POST.get('name'))
                update(request,tool.id)
                return redirect("/")
        return render(request, 'insert.html', args)

def update(request,id):
    if request.user.is_staff:
        tool = Tool.objects.get(id = id)
        if request.method == "POST":
            tool.tooltype = request.POST.get('tooltype')
            tool.name = request.POST.get('name')
            tool.quantity = request.POST.get('quantity')
            tool.daycost = request.POST.get('daycost')
            tool.weekcost = request.POST.get('weekcost')
            tool.monthcost = request.POST.get('monthcost')

            tool.save()
            return redirect("/")
        else:
            return render(request, 'update.html', {'tool':tool})

def delete(request,id):
    if request.user.is_staff:
        tool = Tool.objects.get(id = id)
        tool.delete()
        return redirect("/")

def rent(request,id):
    if not request.user.is_staff:
        tool = Tool.objects.get(id = id)
        if request.method == "POST":
            if tool.quantity - int(request.POST.get("quantity")) >= 0:
                tool.quantity = tool.quantity - int(request.POST.get("quantity"))
                tool.save()
                entry = Entry()
                entry.item = tool
                print(int(request.POST.get("dwm")))
                entry.dwm = int(request.POST.get("dwm"))
                entry.quantity = int(request.POST.get("quantity"))
                entry.duration = int(request.POST.get("duration"))
                if entry.dwm == 1:
                    entry.cost = tool.daycost * entry.duration * entry.quantity
                elif entry.dwm == 2:
                    entry.cost = tool.weekcost * entry.duration * entry.quantity
                else:
                    entry.cost = tool.monthcost * entry.duration * entry.quantity
                entry.save()
                return redirect("/review")
            else:
                return HttpResponse("Change quantity")
        return render(request, "rent.html",{"tool":tool})
    return HttpResponse("Admin can't rent")

def review(request):
    entries = Entry.objects.filter(cart__isnull = True)
    if request.method == "POST":
        for entry in entries:
            if(request.POST.get(str(entry.id)) != entry.quantity):
                tool = Tool.objects.get(id = entry.item.id)
                sub = int(request.POST.get(str(entry.id))) - entry.quantity
                if tool.quantity - sub >= 0:
                    tool.quantity = tool.quantity - sub
                    tool.save()
                    entry.quantity = int(request.POST.get(str(entry.id)))
                    if entry.dwm == 1:
                        entry.cost = tool.daycost * entry.duration * entry.quantity
                    elif entry.dwm == 2:
                        entry.cost = tool.weekcost * entry.duration * entry.quantity
                    else:
                        entry.cost = tool.monthcost * entry.duration * entry.quantity
                    entry.save()
    cost = 0
    for entry in entries:
        cost  = entry.cost + cost
    return render(request, "display.html",{"entries":entries,"cost":cost})

def checkout(request):
    entries = Entry.objects.filter(cart__isnull = True)
    if request.method == "POST":
        cart = Cart()
        cart.name = request.POST.get('name')
        cart.address = request.POST.get('address')
        cart.payment = request.POST.get('payment')
        cart.phonenumber = request.POST.get('phonenumber')
        cart.cost = 0
        for entry in entries:
            cart.cost = cart.cost + entry.cost
            cart.save()
            entry.cart = cart
            entry.save()
        return redirect("/")
    cost = 0
    for entry in entries:
        cost  = entry.cost + cost
    return render(request, "checkout.html",{"entries":entries,"cost":cost})
