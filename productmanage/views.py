from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from mainapp.models import Bike
from .forms import BikeChangeForm
# Create your views here.


def edit_bike(request, id):
    bike = get_object_or_404(Bike, id=id)
    if request.method == 'POST':
        form = BikeChangeForm(request.POST, instance=bike)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.HTTP_REFERER)
        context = {'form': form}
        return render(request, 'edit-bike.html', context)
    context = {'form': BikeChangeForm(instance=bike)}
    return render(request, 'edit-bike.html', context)

