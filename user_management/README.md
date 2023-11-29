
# User Authentication

This folder contains mini projects for User Authentication

And a brief summary of Django user authentication works


Django authentication provides both authentication and authorization

'django.contrib.auth' contains the core of the authentication framework, and its default models.

User object is the core of the authentication system
there are 2 types of user normal and super user both are User class instances only

some minor attribute value change


Primary Attribute of User are:

username
password
email
first_name
last_name


To create a normal user :

from django.contrib.auth.models import User
    
def create_user(username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    #here the user gets saved to database no need to save it
    #to modify this user 
    we can say
    user.last_name = "Lennon"
    user.save
    return user


TO create a super user:

def create_super_user(username, email, password):
    user = User.objects.create_superuser(username=username, email=email, password=password)
    return user

    # so for normal user
        create_user function is used 
    #for super user
        create_superuser is used

#using cli
    python manage.py createsuperuser
    and follow the prompt

To change password
Django does not store raw (clear text) passwords on the user model, but only a hash
So use helper function to change password
Django e PBKDF2 algorithm with a SHA256 hash

    def change_user_password(username, new_password):
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()

#cli
python manage.py changepassword <username>


Django Authenticate user
Uses authenticate module in auth for authentication
The authenticate function returns user object is successfull else None if not successfull


    from django.contrib.auth import authenticate

    def authenticate_user(username, password):
    user = authenticate(username=username, password=password)

    if user is not None:
        print(f"Authentication successful. Welcome, {user.username}!")
    else:
        print("Authentication failed. Invalid username or password.")


Django Permission:
View,add,change,delete