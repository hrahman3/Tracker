from django.shortcuts import render, redirect
from accounts.forms import LoginForm
from django.contrib.auth import login, authenticate


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect("home")

            else:
                form.add_error("username", "Invalid Login")

    else:
        form = LoginForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/login.html", context)
