from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
import emoji
from .models import LoginInfo
from .forms import SignUpForm, LoginForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def sign_up (request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the LoginInfo instance created by the signal
            user.save()  #save in DB
            print(user)
            return HttpResponseRedirect('/sign_in/')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        data = request.POST.get('form')
        print(data)
        if data is not None:
                    username = data [data.find("username")+9:data.find("&Password")]
                    emojipass = data [data.find("Password_emoji")+15:len(data)]
                    user = LoginInfo.objects.get(user=username)
                    if user:
                        print(user)
                        LoginInfo_object = LoginInfo._meta.get_field('choice_text')
                        pin = getattr(user, LoginInfo_object.attname)
                        pin = str(pin.encode('utf-8'))
                        emojiUTF = emojipass.lower().replace("%", r"\x")
                        p = pin [pin.find("b'")+2:len(pin)-1]
                        print(emojiUTF) # testing
                        print(p)        # testing
                        if p == emojiUTF:
                            return HttpResponse('You have Signed in successfully using your emoji password')
                        else:
                            LoginInfo_object = LoginInfo._meta.get_field('fails')
                            fails = getattr(user, LoginInfo_object.attname) #check for fails can be added here 
                            return HttpResponse('You are using invalide credintials')
                    else:
                        HttpResponse('You are using invalide credintials')
    else:
        form = LoginForm()
    return render(request, 'sign_in.html', {'form': form})
