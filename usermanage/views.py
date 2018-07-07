from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from .forms import RegistrationForm, UserChangeForm
# Create your views here.


def userpage(request, id):
    localuser = get_object_or_404(User, id=id)
    usertags = {'name': localuser.username, 'email': localuser.email}
    return render(request, 'userpage.html', {'usertags': usertags})


def edit(request, id):
    localuser = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=localuser)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/myadmin/')
        context = {'form': form}
        return render(request, 'edit-user.html', context)
    context = {'form': UserChangeForm(instance=localuser)}
    return render(request, 'edit-user.html', context)


def delete(request, id):
    localuser = get_object_or_404(User, id=id)
    if request.method == 'POST':
        localuser.delete()
        return HttpResponseRedirect('/myadmin')
    if request.is_ajax():
        localuser.delete()
        return JsonResponse('done')
    user_dict = {'username': localuser.username, 'Email': localuser.email}
    return render(request, 'confirm-delete.html', {'dict': user_dict})


def login(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'index.html', {'page': 'index', 'errors': True})
    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST.get('password1')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'registration.html', context)
    context = {'form': RegistrationForm()}
    return render(request, 'registration.html', context)
