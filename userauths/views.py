from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("userauths:sign-up")
    else:
        form = UserRegisterForm()

    return render(
        request,
        "userauths/sign-up.html",
        {"form": form},
    )
