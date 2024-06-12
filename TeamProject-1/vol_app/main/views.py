from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import *
from .forms import *
from django.db.models import Q

def index(request):
    events = Events.objects.all()
    return render(request,'main/index.html',{'events': events,})

def category_medical(request):
    events = Events.objects.filter(category=1)
    return render(request, 'main/index.html', {'events': events})

def category_sport(request):
    events = Events.objects.filter(category=2)
    return render(request, 'main/index.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        add_form = AddEVentForm2(request.POST, request.FILES)
        if add_form.is_valid():
            photo1 = request.FILES['photo'] if 'photo' in request.FILES else 'photo/2024/04/06/empty.png'    
            
            Events(
                name = add_form.cleaned_data['name'],
                pre_description = add_form.cleaned_data['pre_description'],
                description = add_form.cleaned_data['description'],
                date = add_form.cleaned_data['date'],
                category = Category.objects.get(id=add_form.cleaned_data['category']),
                organization = Organization.objects.get(id=add_form.cleaned_data['organization']),
                level = Level.objects.get(id=add_form.cleaned_data['organization']),
                photo = photo1,
                points = add_form.cleaned_data['points']
            ).save()
    else:
        pass
    add_form = AddEVentForm2()
    return render(request, 'main/add.html', {'add_form': add_form})

def delete_event(request, event_id):
    product = get_object_or_404(Events, id=event_id)
    product.delete()
    return render(request, 'main/index.html') 

            
def detail(request, event_id):
    try:
        event = Events.objects.get(id=event_id)
    except:
        return redirect('/')
    return render(request,'main/detail.html', {'event': event})

def search(request):
    events = []
    if request.method == 'GET':
        query = request.GET.get('q')
        print(query,"HEREREE")
        events = Events.objects.filter(Q(name__icontains=query))
    return render(request, 'main/index.html', {'query': query, 'events': events})

@login_required
def participate(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    user_points, created = UserPoints.objects.get_or_create(user=request.user)

    if not created:
        # If user already has points, add points from the event
        user_points.points += event.points
        print(user_points,'HERERE!@!@@!@')
        user_points.save()
        return render(request,'main/index.html')
    else:
        # If user points object is newly created, redirect to login page
        return render(request, 'user_auth/login.html')
        
        
