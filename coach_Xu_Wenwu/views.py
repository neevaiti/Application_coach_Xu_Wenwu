from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Premier test de page en code dégueulasse
def home(request):
    return render(request, "coach_Xu_Wenwu_app/home.html")

def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        surname = request.POST["surname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        new_user = User.objects.create_user(username, email, password)
        new_user.name = name
        new_user.surname = surname
        new_user.phone = phone

        new_user.save()

        messages.success(request, "Votre compte est créer avec succès.")

        return redirect(signin)

    return render(request, "coach_Xu_Wenwu_app/signup.html")


def signin(request):
    return render(request, "coach_Xu_Wenwu_app/signin.html")


def logout(request):
    pass