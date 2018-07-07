from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from mainapp.models import Bike, MessagesFromContactUs

# Create your views here.


def admin_page(request):
    # page_models = {}
    users = User.objects.all()[:3]
    # page_models['Userlist'] = users

    bikes = Bike.objects.all()[:3]
    # page_models['Bike'] = bikes

    messages = MessagesFromContactUs.objects.all()[:3]

    return render(request, 'admin-page.html', locals())


def user_manage(request):
    users = User.objects.all()
    paginator = Paginator(users, 10)

    page = request.GET.get('page')
    try:
        user_list = paginator.page(page)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)
    return render(request, 'admin-usermanage.html', {'user_list': user_list})


def bikes_manage(request):
    bikes = Bike.objects.all()
    paginator = Paginator(bikes, 10)

    page = request.GET.get('page')
    try:
        bike_list = paginator.page(page)
    except PageNotAnInteger:
        bike_list = paginator.page(1)
    except EmptyPage:
        bike_list = paginator.page(paginator.num_pages)
    return render(request, 'admin-bikesmanage.html', {'bike_list': bike_list})


def contact_messages(request):
    mes = MessagesFromContactUs.objects.all()
    paginator = Paginator(mes, 3)

    page = request.GET.get('page')
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        messages = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        messages = paginator.page(paginator.num_pages)
    return render(request, 'admin-messages-from-contact.html', {'messages': messages})
