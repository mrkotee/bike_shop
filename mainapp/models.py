# from django.db import models
from django.db.models import Model, CharField, TextField, ForeignKey, ManyToManyField, IntegerField, EmailField
from django.db.models import DateTimeField, ImageField, FloatField, PROTECT
# Create your models here.


class Bike(Model):
    BIKE_TYPES = (
        ('MNTN', 'Mountain bikes'),
        ('SSB', 'Single-speed bikes'),
        ('RB', 'Road bikes')
    )
    # SIZE = (
    #     ('XS', 'xs'),
    #     ('M', 'm'),
    #     ('S', 's')
    # )

    name = CharField(max_length=20)
    brand = CharField(max_length=25)
    # model_art = CharField(max_length=40, blank=True)
    bike_type = CharField(max_length=5, choices=BIKE_TYPES)
    # size = CharField(max_length=2, choices=SIZE)
    description = TextField()
    cost = IntegerField(default=500)
    wheeldia = IntegerField(blank=True, null=True) # inch
    speeds = IntegerField(default=1)
    color = CharField(max_length=30, default='color')
    weight = FloatField(blank=True, null=True)

    def __str__(self):
        return '{}, color: {}'.format(self.name, self.color)


class BikeImages(Model):
    image = ImageField(upload_to='bikes')
    bike = ForeignKey(Bike, related_name='img', on_delete=PROTECT)

    def __str__(self):
        return 'image for {}'.format(self.bike.name)


class MessagesFromContactUs(Model):
    user_name = CharField(max_length=50)
    user_surname = CharField(max_length=50)
    user_email = EmailField(max_length=100)
    message = TextField()
    d_time = DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}, from {}'.format(self.d_time, self.user_email)

