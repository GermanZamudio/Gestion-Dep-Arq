
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm

class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'my-input'})
        self.fields['password'].widget.attrs.update({'class': 'my-input'})
def signin (request):
    #try:
        if request.method=='GET':
            return render(request,"log/login.html",{"form":MyAuthenticationForm})
        else:
            user=authenticate(request,username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request,"log/login.html",{"form":MyAuthenticationForm,"credencial_fail":"credencial_fail"})
            else: 
                login(request,user)
                return redirect('home')
    #except:
    #    return render(request,"log/login.html",{"form":MyAuthenticationForm,"error":"error"})
        
def singout(request):
    logout(request)
    return redirect('signin')

@login_required
def home(request):
    usuario=request.user.username
    return render(request,'home/home.html',{'usuario':usuario})