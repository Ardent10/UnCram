from multiprocessing import context
from django.shortcuts import render , redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

# from django.http import HttpResponse 
# return HttpResponse('Study room')
# return HttpResponse('Welcome Professor')

# rooms = [
#     {'id':1, 'name':'Learning DevOps'},
#     {'id':2, 'name':'Learning Machine learning'},
#     {'id':3, 'name':'Learning Data Science'},
# ]


def home(request):
    rooms = Room.objects.all()
    # Creating context dictionary
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request,pk): 
    
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i

    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html',context)


# CRUD operations 

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'base/room_form.html',context)


def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method=='POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'base/room_form.html',context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})