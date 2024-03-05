from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from teretana.forms import *
from teretana.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
import logging



# Create your views here.

def Home(request):
    trener = Trener.objects.all()
    plan = Plan.objects.all()
    return render(request,"home.html", {'trener': trener, 'plan': plan})

def Dashboard(request):
    return render(request,"dashboard.html")

def AdminHome(request):
    return render(request,"adminhome.html")


def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login and try again")
        return redirect('/login')

    if request.method == 'POST':
        form = PretplatnikForm(request.POST)
        if form.is_valid():
            # Create a new Pretplatnik instance
            pretplatnik_instance = form.save(commit=False)
            pretplatnik_instance.korisnik = request.user
            # Set first_name and last_name based on the logged-in user
            pretplatnik_instance.first_name = request.user.first_name
            pretplatnik_instance.last_name = request.user.last_name
            pretplatnik_instance.save()
            
            messages.success(request, "You have successfully enrolled.")
            return redirect('/')  # Redirect to a success page or dashboard
        else:
            messages.error(request, "Form submission failed. Please check the errors.")

    else:
        form = PretplatnikForm()
        
    return render(request, 'enroll.html', {'form': form})


def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        first_name=request.POST.get('name')
        last_name=request.POST.get('surname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser = User.objects.create_user(username=username, email=email, password=pass1, first_name=first_name, last_name=last_name)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
        
        
    return render(request,"signup.html")


def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser.is_superuser:
            return (redirect('/adminhome')) 
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
        
    return render(request,"handlelogin.html")


def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')



#CRUD Plan

class PlanList(ListView):
    model = Plan
    template_name = "main/plan_list.html"


class PlanCreateView(CreateView):
    model = Plan
    form_class = PlanForm
    template_name = 'main/addnewplan.html'
    success_url = reverse_lazy('teretana:plan_list')

class PlanUpdateView(UpdateView):
    model = Plan
    form_class = PlanForm
    template_name = 'main/updateplan.html'
    success_url = reverse_lazy('teretana:plan_list')

def destroyplan(request, id):  
    plan = Plan.objects.get(id=id)  
    plan.delete()  
    return redirect("/plan_list")  


#CRUD Trener


class TrenerList(ListView):
    model = Trener
    template_name = "main/trener_list.html"

class TrenerCreateView(CreateView):
    model = Trener
    form_class = TrenerForm
    template_name = 'main/addnewtrener.html'
    success_url = reverse_lazy('teretana:trener_list')

class TrenerUpdateView(UpdateView):
    model = Trener
    form_class = TrenerForm
    template_name = 'main/updatetrener.html'
    success_url = reverse_lazy('teretana:trener_list')

def destroytrener(request, id):  
    trener = Trener.objects.get(id=id)  
    trener.delete()  
    return redirect("/trener_list")

#CRUD Pretplatnik

class PretplatnikList(ListView):
    model = Pretplatnik
    template_name = "main/pretplatnik_list.html"

class PretplatnikCreateView(CreateView):
    model = Pretplatnik
    form_class = PretplatnikForm
    template_name = 'main/addnewpretplatnik.html'
    success_url = reverse_lazy('teretana:pretplatnik_list')

class PretplatnikUpdateView(UpdateView):
    model = Pretplatnik
    form_class = PretplatnikForm
    template_name = 'main/updatepretplatnik.html'
    success_url = reverse_lazy('teretana:pretplatnik_list')

def destroypretplatnik(request, id):  
    pretplatnik = Pretplatnik.objects.get(id=id)
    pretplatnik.delete()  
    return redirect("/pretplatnik_list")

#CRUD Oznake

class OznakaList(ListView):
    model = Oznaka
    template_name = "main/oznaka_list.html"


class OznakaCreateView(CreateView):
    model = Oznaka
    form_class = OznakaForm
    template_name = 'main/addnewoznaka.html'
    success_url = reverse_lazy('teretana:oznaka_list')

class OznakaUpdateView(UpdateView):
    model = Oznaka
    form_class = OznakaForm
    template_name = 'main/updateoznaka.html'
    success_url = reverse_lazy('teretana:oznaka_list')

def destroyoznaka(request, id):
    oznaka = Oznaka.objects.get(id=id)  
    oznaka.delete()  
    return redirect("/oznaka_list")

#CRUD User


class UsersListView(ListView):
    template_name = 'main/userlist.html'
    login_url = '/login/'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()

class UsersCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'main/addnewuser.html'
    success_url = reverse_lazy('teretana:user_list')

class UsersUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    template_name = 'main/updateuser.html'
    success_url = reverse_lazy('teretana:user_list')

def destroyuser(request, id):  
    myuser = User.objects.get(id=id)  
    myuser.delete()  
    return redirect("/user_list")

