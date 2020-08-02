from django.shortcuts import render
import emoji
from .models import LoginInfo
# Create your views here.
def home(request):
    return render(request, 'home.html')
def sign_up (request):

    return render(request, 'sign_up.html')
def sign_in(request):

    return render(request, 'sign_in.html')
