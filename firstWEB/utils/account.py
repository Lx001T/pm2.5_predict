from django.shortcuts import render, HttpResponse, redirect
import tkinter.messagebox
from django import forms
from firstWEB import models

class LoginForm(forms.Form):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(attrs={"class":"form-control"})

    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form":form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "username or password error")
            return render(request, "login.html", {'form': form})

        request.session["info"] = {"id":admin_object.id, "name": admin_object.username}

        return redirect("/current")

    return render(request, "login.html", {'form':form})


def logout(request):

    request.session.clear()

    return redirect("/login")