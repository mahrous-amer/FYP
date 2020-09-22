from django.shortcuts import render, HttpResponse, redirect
from .forms import Profileform, Drag
from .models import Profile
# Create your views here.



def Drag_up (request):
    if request.method == 'POST':
        form = Profileform(request.POST)
        if form.is_valid():
            Profile = form.save()
            Profile.refresh_from_db()  # load the instance created by the signal
            Profile.save()
            return redirect ('Drag_in')
    else:
        form = Profileform()
    return render(request, 'DragPIN_sign_up.html', context={'form': form, })

def Drag_in(request):
    results = [
                [{"id": "00", "value": "A"}, {"id": "01", "value": "B"}, {"id": "02", "value": "C"}, {"id": "03", "value": "D"}, {"id": "04", "value": "E"},{"id": "05", "value": "A"},{"id": "06", "value": "B"}, {"id": "07", "value": "C"}, {"id": "08", "value": "D"}, {"id": "09", "value": "E"}],
                [{"id": "10", "value": "A"}, {"id": "11", "value": "B"}, {"id": "12", "value": "C"}, {"id": "13", "value": "D"}, {"id": "14", "value": "E"},{"id": "15", "value": "A"},{"id": "16", "value": "B"}, {"id": "17", "value": "C"}, {"id": "18", "value": "D"}, {"id": "19", "value": "E"}],
                [{"id": "20", "value": "A"}, {"id": "21", "value": "B"}, {"id": "22", "value": "C"}, {"id": "23", "value": "D"}, {"id": "24", "value": "E"},{"id": "25", "value": "A"},{"id": "26", "value": "B"}, {"id": "27", "value": "C"}, {"id": "28", "value": "D"}, {"id": "29", "value": "E"}],
                [{"id": "30", "value": "A"}, {"id": "31", "value": "B"}, {"id": "32", "value": "C"}, {"id": "33", "value": "D"}, {"id": "34", "value": "E"},{"id": "35", "value": "A"},{"id": "36", "value": "B"}, {"id": "37", "value": "C"}, {"id": "38", "value": "D"}, {"id": "39", "value": "E"}],
                ]
                
    if request.method == 'POST':
        form = Drag(request.POST)
        arr = request.POST.getlist('result[]')
        data = request.POST.get('form')
        """ process user login"""
        if data is not None:
            DragId = data [data.find("DragID")+7:len(data)]
            context_dict = {'DragID': DragId}
            try:
                draguser = Profile.objects.get(DragID=DragId)
                Profile_object = Profile._meta.get_field('PIN')
                pin = getattr(draguser, Profile_object.attname)
                Profile_object = Profile._meta.get_field('Identifier')
                identifier = getattr(draguser, Profile_object.attname)
                count = 0
                for x in pin:
                    if count == 0:
                        one = identifier is arr[int(x)]
                    elif count == 1:
                        two = identifier is arr[10+int(x)]
                    elif count == 2:
                        three = identifier is arr[10+10+int(x)]
                    elif count == 3:
                        four = identifier is arr[10+10+10+int(x)]
                    count=count+1
                print(one,two,three,four)
                if one == True and two == True and three == True and four == True:
                    return HttpResponse('User has been successfully signed in!')
                else:
                    return HttpResponse('Dragid or DragPIN used is incorect')
            except Profile.DoesNotExist:
                return HttpResponse('Dragid or DragPIN used is incorect')

        #return HttpResponse('User has been successfully signed in!')
    else:
        form = Drag()
    return render(request, 'DragPIN_sign_in.html', {'form': form, 'results': results,})
