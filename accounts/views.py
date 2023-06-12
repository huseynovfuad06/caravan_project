from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout
from .forms import LoginForm, RegisterForm


User = get_user_model()



def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            user = User.objects.get(username=username)

            login(request, user)

            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)



def register_view(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)



def logout_view(request):
    logout(request)
    return redirect("/")