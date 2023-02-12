from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import FormPickDate, EditNoteForm
from .models import PickDate


# Premier test de page en code dégueulasse
def home(request):
    return render(request, "coach_Xu_Wenwu_app/client/home.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]

        # TODO Check password === confirm_password
        # TODO Check password length, one uppercase, one lowercase, one number and one symbol

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.is_active = True
        new_user.save()

        messages.success(request, "Votre compte est créer avec succès.")

        return redirect(signin)

    return render(request, "coach_Xu_Wenwu_app/client/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(dashboard)

        else:
            messages.error(request, "Nom d'utilisateur et/ou Mot de passe incorrect.")
            return redirect(signin)

    return render(request, "coach_Xu_Wenwu_app/client/signin.html")



def signout(request):
    logout(request)
    messages.success(request, "Déconnexion réussie.")
    return redirect(home)


@login_required(login_url='/connexion')
def dashboard(request):
    return render(request, "coach_Xu_Wenwu_app/back_office/dashboard.html", {"fname": request.user.first_name})


@login_required(login_url='/connexion')
def take_appointment(request):
    return render(request, "coach_Xu_Wenwu_app/back_office/take_appointment.html")

@login_required(login_url='/connexion')
def book_appointment(request):
    if request.method == 'POST':
        form = FormPickDate(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time_slot = form.cleaned_data['time_slot']
            subject = form.cleaned_data['subject']

            # Check if the day is a weekend
            if date.weekday() >= 5:
                messages.error(request, "Vous ne pouvez pas prendre de rendez-vous les week-ends.")
                return redirect(book_appointment)

            existing_appointment = PickDate.objects.filter(date=date, time_slot=time_slot)

            if existing_appointment.exists():
                messages.error(request, 'Ce rendez-vous est déjà pris.')
                return redirect(book_appointment)

            appointment = PickDate(
                date=date,
                time_slot=time_slot,
                subject=subject,
                user=request.user,
                name=request.user.first_name + ' ' + request.user.last_name,
                email=request.user.email,
            )
            appointment.save()
            messages.success(request, 'Votre rendez-vous a été pris avec succès!')
            return redirect(book_appointment)
    else:
        form = FormPickDate()

    return render(request, 'coach_Xu_Wenwu_app/back_office/take_appointment.html', {'form': form})


@login_required(login_url='/connexion')
def view_appointments(request):
    user_appointments_informations = PickDate.objects.filter(user=request.user)
    if request.user.is_staff:
        return render(request, 'coach_Xu_Wenwu_app/back_office/history_appointment.html',
                      {'appointments': user_appointments_informations, 'is_superuser': True})
    else:
        return render(request, 'coach_Xu_Wenwu_app/back_office/history_appointment.html', {'appointments': user_appointments_informations})


@login_required(login_url='/connexion')
def edit_notes(request, appointment_id):
    appointment = PickDate.objects.get(id=appointment_id)
    if request.method == 'POST':
        form = EditNoteForm(request.POST)
        if form.is_valid():
            appointment.notes = form.cleaned_data['note']
            appointment.save()
            messages.success(request, 'Note modifiée avec succès!')
            return redirect(view_appointments)
    else:
        form = EditNoteForm(initial={'note': appointment.notes})
    return render(request, 'coach_Xu_Wenwu_app/back_office/edit_notes.html', {'form': form})

@login_required(login_url='/connexion')
def general_appointments_view(request):
    patient = PickDate.objects.values('name').distinct()
    return render(request, "coach_Xu_Wenwu_app/back_office/history_appointment_complementary.html", {"patients": patient})

@login_required(login_url='/connexion')
def patient_appointments(request, patient_name):
    patient_appointments = PickDate.objects.filter(name=patient_name)
    return render(request, 'coach_Xu_Wenwu_app/back_office/history_appointment.html',
                  {'appointments': patient_appointments, 'is_superuser': True})
