from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

#registration
#forgot password
#Normal login
#OTP Login


def register_view(request):
    if request.method == "POST":
        print(f"{request.POST=}")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save()  # Save the new user,
            print("User created")
            login(request,user)
            print("Login Successful rendering index.html")
            return redirect(registration_app_home_page_view)
        else:
            print("Form is not valid")
            # Handle the case where the form is not valid
            return render(request, 'user_mgmt/register/register.html', {'form': form, 'error_message': 'Invalid form data. Please check the provided information.'})
    else: #if method is GET it will give empty form for user to fill
        form = CustomUserCreationForm()
    return render(request, "user_mgmt/register/register.html", {"form": form})


def login_view(request):
    return render(request,"user_mgmt/login/login_page.html")


def forgot_password(request):
    pass


def otp_login_view(request):
    pass

@login_required()
def registration_app_home_page_view(request):
    return render(request,"index.html")