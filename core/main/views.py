from multiprocessing import context
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, View, FormView, TemplateView, CreateView
from . models import HomeBackGroud , ArkacayinTurizm,Kayqimasin, Loginimg, aboutuss,apranqnervacharvox,blokej2,blokej,hyuranoc,hajortvayr,staysej,staysej3
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.




def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home2")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home2")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home2")





class HomeBackGroudListView(ListView):
    template_name = 'indexs.html'
    
    def get(self,request):
        backs = HomeBackGroud.objects.all()
        arkac = ArkacayinTurizm.objects.all()
        kayq = Kayqimasin.objects.all()
        apranq = apranqnervacharvox.objects.all()
        hyuranocc = hyuranoc.objects.all()
        vayr = hajortvayr.objects.all()
        context = {'backs':backs,'arkac':arkac,'kayq':kayq,'apranq':apranq,'hyuranocc':hyuranocc,'vayr':vayr}

        return render(request,self.template_name,context)

class ApranqnerDetal(DetailView):
    template_name = 'apranqner_detal.html'
    def get(self,request,id):
        apranqd = apranqnervacharvox.objects.get(pk=id)
        context = {'apranqd':apranqd}
        return  render(request,self.template_name,context)

class IndexDetalView(DetailView):
    template_name = 'index_detal.html'
    def get(self,request,id):
        arkacc = ArkacayinTurizm.objects.get(pk=id)
        context = {'arkacc':arkacc}
        return render(request,self.template_name,context)


class homegroudDetal(DetailView):
    template_name = 'gr_detal.html'
    def get(self,request,id):
        homdetal = HomeBackGroud.objects.get(pk=id)
        context =  {'homdetal':homdetal}
        return render(request,self.template_name, context)


class KayqimasinListView(ListView):
    template_name = 'aboutus.html'

    def get(self,request):
        kayqaboutus = aboutuss.objects.all()
        context = {'kayqaboutus':kayqaboutus}
        return render(request,self.template_name,context)


class blogListView(ListView):
    template_name = 'blog.html'

    def get(self,request):
        blogis = blokej.objects.all()
        blogis2 = blokej2.objects.all()
        context = {'blogis2':blogis2,'blogis':blogis}
        return render(request,self.template_name,context)

class flightsListView(ListView):
    template_name = 'flights.html'
    def get(self,request):

        return render(request,self.template_name)


class staysListView(ListView):
    template_name = 'stays.html'
    def get(self,request):
        staysstays = staysej.objects.all()
        stays33 = staysej3.objects.all()
        return render(request,self.template_name,{'staysstays': staysstays,'stays33':stays33})

class LOGINListView(ListView):
    template_name = 'login.html'
    def get(self,request):
        loginn = Loginimg.objects.all()
        return render(request,self.template_name,{'loginn':loginn})


