from django.shortcuts import render
from userauths.forms import UserRegisterForm

def reigster_view(request):
    form = UserRegisterForm(request.POST)

    context = {'form': form}

def register_view(request):
    return render(request, "userauths/sign-up.html", context)




# from django.http import HttpResponse
#
# def register_view(request):
#     return HttpResponse("Register page")