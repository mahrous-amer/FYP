from django.shortcuts import render, HttpResponse, redirect
from .forms import Profileform, Drag
from .models import Profile
import random
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
    results = []
    for i in range(4):
        row = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
        random.shuffle(row)
        line = []
        for j in range(10):
            line.append({"id": str(i)+str(j), "value": row[j]})
        results.append(line)
    print(results)
    # "Cleaner code = Slower code <in this case>"
    # credits @ Dr.MahrousAmer ^
    # Bad way >>>
    # charlist = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
    # row1 = charlist
    # random.shuffle(charlist)
    # row1 = charlist
    # charlist = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
    # random.shuffle(charlist)
    # row2 = charlist
    # charlist = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
    # random.shuffle(charlist)
    # row3 = charlist
    # charlist = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
    # random.shuffle(charlist)
    # row4 = charlist
    # results = [
    #             [{"id": "00", "value": row1[0]}, {"id": "01", "value": row1[1]}, {"id": "02", "value": row1[2]}, {"id": "03", "value": row1[3]}, {"id": "04", "value": row1[4]},{"id": "05", "value": row1[5]},{"id": "06", "value": row1[6]}, {"id": "07", "value": row1[7]}, {"id": "08", "value": row1[8]}, {"id": "09", "value": row1[9]}],
    #             [{"id": "10", "value": row2[0]}, {"id": "11", "value": row2[1]}, {"id": "12", "value": row2[2]}, {"id": "13", "value": row2[3]}, {"id": "14", "value": row2[4]},{"id": "15", "value": row2[5]},{"id": "16", "value": row2[6]}, {"id": "17", "value": row2[7]}, {"id": "18", "value": row2[8]}, {"id": "19", "value": row2[9]}],
    #             [{"id": "20", "value": row3[0]}, {"id": "21", "value": row3[1]}, {"id": "22", "value": row3[2]}, {"id": "23", "value": row3[3]}, {"id": "24", "value": row3[4]},{"id": "25", "value": row3[5]},{"id": "26", "value": row3[6]}, {"id": "27", "value": row3[7]}, {"id": "28", "value": row3[8]}, {"id": "29", "value": row3[9]}],
    #             [{"id": "30", "value": row4[0]}, {"id": "31", "value": row4[1]}, {"id": "32", "value": row4[2]}, {"id": "33", "value": row4[3]}, {"id": "34", "value": row4[4]},{"id": "35", "value": row4[5]},{"id": "36", "value": row4[6]}, {"id": "37", "value": row4[7]}, {"id": "38", "value": row4[8]}, {"id": "39", "value": row4[9]}]
    #             ]
    # <<<
    # results.append([{"id": str(i)+"0", "value": row1[0]}, {"id": str(i)+"1", "value": row1[1]}, {"id": str(i)+"2", "value": row1[2]}, {"id": str(i)+"3", "value": row1[3]}, {"id": str(i)+"4", "value": row1[4]},{"id": str(i)+"5", "value": row1[5]},{"id": str(i)+"6", "value": row1[6]}, {"id": str(i)+"7", "value": row1[7]}, {"id": str(i)+"8", "value": row1[8]}, {"id": str(i)+"9", "value": row1[9]}])
    # <<< v1

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
                print(DragId)
                print(pin)
                print(arr)
                #Profile_object = Profile._meta.get_field('Identifier')
                #identifier = getattr(draguser, Profile_object.attname)
                #extras are not allways good
                # count = 0
                # for x in pin:
                #     if count == 0:
                #         one = identifier is arr[int(x)]
                #     elif count == 1:
                #         two = identifier is arr[10+int(x)]
                #     elif count == 2:
                #         three = identifier is arr[10+10+int(x)]
                #     elif count == 3:
                #         four = identifier is arr[10+10+10+int(x)]
                #     count=count+1
                # print(one,two,three,four)
                # print( arr[int(pin[0])], arr[int(pin[1])], arr[int(pin[2])], arr[int(pin[3])] )
                # #if one == True and two == True and three == True and four == True:
                if arr[int(pin[0])] == arr[10+int(pin[1])] == arr[20+int(pin[2])] == arr[30+int(pin[3])]:
                    return HttpResponse('User has been successfully signed in!')
                else:
                    return HttpResponse('Dragid or DragPIN used is incorect')
            except Profile.DoesNotExist:
                return HttpResponse('Dragid or DragPIN used is incorect')

        #return HttpResponse('User has been successfully signed in!')
    else:
        form = Drag()
    return render(request, 'DragPIN_sign_in.html', {'form': form, 'results': results,})
