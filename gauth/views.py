from django.shortcuts import render
import emoji
from .models import LoginInfo
from .forms import SignUpForm
# Create your views here.
def home(request):
    return render(request, 'home.html')
def sign_up (request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the LoginInfo instance created by the signal
            user.save()
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):

    return render(request, 'sign_in.html')
