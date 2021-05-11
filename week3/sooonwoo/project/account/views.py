from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request=request, username=username, password=password)
            if user is None:
                login(ruquest, user)
            
            return redirect("home")
    form = AuthenticationForm()
    return render(request,'login.html',{'form':form})