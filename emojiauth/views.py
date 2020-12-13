from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
import emoji
import random
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
            user.start()
            user.save()  #save in DB
            print(user)
            return HttpResponseRedirect('/sign_in/')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

pinarr = None
def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                if username:
                    user = LoginInfo.objects.get(user=username)
                    request.session['username'] = username
                    return redirect ('EmojiDrag')
                else:
                    return HttpResponse('You are using invalide credintials')
            except LoginInfo.DoesNotExist:
                return HttpResponse('You are using invalide credintials')
    else:
        form = LoginForm()
    return render(request, 'sign_in.html', {'form': form})

def sign_upp (request):
    results = []
    for i in range(4):
        row = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
        random.shuffle(row)
        line = []
        for j in range(10):
            line.append({ "id": f'{i}'+f'{j}', "value": row[j] })
        results.append(line)
    username = request.session.get('username')
    user = LoginInfo.objects.get(user=username)
    Question, pin, EmojiArray = user.GetEmojiArray()

    EmojiArray = ["".join( a for a in EmojiArray.split())]
    Emojiarray = []
    for x in EmojiArray[0]:
        Emojiarray.append(x)

    arr = request.POST.getlist('result[]')
    if request.method == 'POST':
        """ process user login"""
        try:
            if arr[int(pin[0])] == arr[10+int(pin[1])] == arr[20+int(pin[2])] == arr[30+int(pin[3])]:
                name = str(username)+"has been successfully signed in!"
                return HttpResponse(name)
            else:
                return HttpResponse('DragPIN used is incorect')
        except LoginInfo.DoesNotExist:
            return HttpResponse('DragPIN used is incorect')
    return render(request, 'EmojiDrag.html', {'results': results, 'EmojiArray': Emojiarray, 'Question': Question})

def feedback(request):
    return render(request, 'feedback.html')
