from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Premier test de page en code dégueulasse
def home(request):
    return render(request, "coach_Xu_Wenwu_app/home.html")

def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        new_user = User.objects.create_user(username, email, password1)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.is_active = True
        new_user.save()

        messages.success(request, "Votre compte est créer avec succès.")

        return redirect(signin)

    return render(request, "coach_Xu_Wenwu_app/signup.html")


def signin(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]


        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "coach_Xu_Wenwu_app/dashboard.html", {"fname": fname})

        else:
            messages.error(request, "Nom d'utilisateur et/ou Mot de passe incorrect.")
            return redirect(signin)

    return render(request, "coach_Xu_Wenwu_app/signin.html")



@login_required
def signout(request):
    logout(request)
    messages.success(request, "Déconnexion réussie.")
    return redirect(home)


@login_required
def dashboard(request):
    return render(request, "coach_Xu_Wenwu_app/dashboard.html")


@login_required
def take_appointment(request):
    return render(request, "coach_Xu_Wenwu_app/take_appointment.html")

@login_required
def appointment(request):
    if request.method == "POST":
        your_name = request.POST["your-name"]
        your_surname = request.POST["your-surname"]
        your_phone_number = request.POST["your-phone-number"]
        your_time = request.POST["your-time"]
        your_message = request.POST["your-message"]

        return render(request, "coach_Xu_Wenwu_app/dashboard.html", {"your_time": your_time})

    else:
        return render(request, "coach_Xu_Wenwu_app/take_appointment.html", {})