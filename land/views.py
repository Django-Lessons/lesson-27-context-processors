from django.shortcuts import render
from land.models import Category


def index(request):

    return render(
        request,
        'land/index.html',
    )


def privacy_policy(request):
    return render(
        request,
        'land/privacy.html',
    )


def login(request):
    return render(
        request,
        'land/login.html',
    )


def user_profile(request):
    return render(
        request,
        'land/user_profile.html',
    )



