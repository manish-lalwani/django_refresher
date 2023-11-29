from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm

#code for login


#creating a view for Registration Page it will return empty form if request is get for POSt(when form is filled) it will login the user and redirect to home.htnl
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): #all validation passing
            user = form.save() #it returns the user object
            login(request,user) #logs in user and sets cookie
            return redirect("home1")
    else: #if method is GET it will return empty form for registration
        form = CustomUserCreationForm()
    return render(request,"register/register.html",{"form": form})


#code for user_login without using Django form
def user_login_without_form(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request=request,username=username,password=password) #returns user object if authentication successfull else false
        if user:
            print("Login Successful")
            return redirect("home1")

#code for user login with authentication form
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] #after validation data is stored in cleaned_data dictionary
            password = form.cleaned_data['password']
            user = authenticate(request=request,username=username,password=password)
            if user is not None:
                login(request,user)
                print(f"LOgin successful for {user=}")
                return redirect("home1")
            else: #password or username is wrong
                print(f"Wrong credentials")
                return render(request=request,template_name="register/login.html",context={"form": form,"error_message": "Invalid Login Credentials"})
        else:
            # Handle the case where the form is not valid
            return render(request, 'register/login.html', {'form': form, 'error_message': 'Invalid form data. Please check the provided information.'})
    else: #request is get
        form = AuthenticationForm()
        return render(request=request,template_name="register/login.html",context={"form": form})

@login_required(login_url="user_login")
def home(request):
    return render(request,"index.html")