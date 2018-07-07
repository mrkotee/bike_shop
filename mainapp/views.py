from django.http import Http404
from django.shortcuts import render

from .models import MessagesFromContactUs, Bike, BikeImages


# Create your views here.


def main(request, message_receved=False):
    bike_list = Bike.objects.all()

    return render(request, 'index.html', {'page': 'index', 'bike_list': bike_list, 
                                        'bikeimages': BikeImages,
                                        'message_receved': message_receved}
                                        )


# def bicycles(request):
#     mountain_bikes = Bike.objects.filter(bike_type='MNTN')
#     ss_bikes = Bike.objects.filter(bike_type='SSB')
#     road_bikes = Bike.objects.filter(bike_type='RB')
#
#     return render(request, 'bicycles.html', {'mountain_bikes': mountain_bikes,
#                                              'ss_bikes': ss_bikes,
#                                              'road_bikes': road_bikes})
def bicycles(request):
    categories = {}
    for category in Bike.BIKE_TYPES:
        bike_list = Bike.objects.filter(bike_type=category[0])
        if bike_list:
            categories[category[1]] = bike_list

    return render(request, 'bicycles_dict.html', {'categories': categories})


def parts(request):
    return render(request, 'parts.html')


def accessories(request):
    return render(request, 'accessories.html')


def cart(request):
    return render(request, 'cart.html')


def single(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
    bike_images = BikeImages.objects.filter(bike=bike_id)
    return render(request, 'single.html', {'bike': bike, 'bike_images': bike_images})


def send_message(request):
    if request.method == 'POST':
        name, surname, email, message = request.POST.get('name'), request.POST.get('surname'), \
                                        request.POST.get('email'), request.POST.get('message')

        mfc = MessagesFromContactUs.objects.create(user_name=name, user_surname=surname,
                                                   user_email=email, message=message)
        mfc.save()

        # return redirect('index', message_receved=True) #, {'page': 'index', 'message_receved': True})
        return render(request, 'index.html', {'page': 'index', 'message_receved': True})
    raise Http404
