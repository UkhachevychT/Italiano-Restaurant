from django.shortcuts import render, get_list_or_404, get_object_or_404

from datetime import datetime

from . import models

def index(request):
    return render(request, 'index.html')

def menu(request):
    recomended_dishes = get_list_or_404(models.Dish, recomended=True)
    categories = get_list_or_404(models.Category)

    return render(request, 'menu.html', {
        'recomended_dishes': recomended_dishes,
        'categories': categories,
    })

def gallery(request):
    return render(request, 'gallery.html')

def reservation(request):
    return render(request, 'booking.html')

def book(request):
    if 'name' in request.GET:

        reservation = models.Reservation(
            name=request.GET['name'],
            email=request.GET['email'],
            number=request.GET['number'],
            person_count=request.GET['people'],
            date=datetime.strptime(request.GET['date'], "%d/%m/%Y").date(),
            time=request.GET['time'],
            special_request=request.GET['request'],
        )
        reservation.save()
        message = 'You succesfuly booked your table!'
    else:
        message = 'Something went wrong. Try again'
    return render(request, 'booking_result.html', {'message': message})

def contact(request):
    return render(request, 'contact.html')

def contact_result(request):
    if 'username' in request.GET:
        contact = models.Contact(
            name=request.GET['username'],
            email=request.GET['useremail'],
            message=request.GET['message'],
        )
        contact.save()
        message = 'You succesfuly send us message!'
    else:
        message = 'Something went wrong. Try again'
    return render(request, 'contact_result.html', {'message': message})