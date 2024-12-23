from django.shortcuts import render,redirect
from django.contrib.auth import login
from . forms import SignUpForm
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'chatapp/home.html')

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
        
        else:
            return render(request, 'chatapp/signup.html', {'form': form})
        
    else:
        form=SignUpForm()
        return render(request,'chatapp/signup.html',{'form':form})