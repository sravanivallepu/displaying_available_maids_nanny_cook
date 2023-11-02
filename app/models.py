from django.db import models

# Create your models here.
import numpy as np
from django.utils import timezone
from django.utils.timezone import datetime
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    profile_picture=models.ImageField()

    def __str__(self):
        return str(self.username)
    
    
SERVICE_CHOICES = (
    ("Maid", "Maid"),
    ("Cook", "Cook"),
    ("Nanny", "Nanny"),
    ("Care Taker", "Care Taker"),
    )
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100,choices=SERVICE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    availability_start = models.TimeField(null=True)
    availability_end = models.TimeField(null=True)
    
    def __str__(self):
        return f"{self.createdAt.strftime('%H-%m-%p')}"

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return str(self.name)
    
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    name = models.ForeignKey(Service,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    booking_time = models.TimeField(null=True)

    def __str__(self):
        return f"{self.createdAt.strftime('%d-%m-%Y')}"
    
class Book_maid(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('service', 'booking','review')

    def __str__(self):
        return str(self.service) + '|' + str(self.booking) + '|' + str(self.review)

   
class Book_cook(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('service', 'booking','review')

    def __str__(self):
        return str(self.service) + '|' + str(self.booking) + '|' + str(self.review)
   
class Book_nanny(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('service', 'booking','review')

    def __str__(self):
        return str(self.service) + '|' + str(self.booking) + '|' + str(self.review)
    
 

class Maid(models.Model):
    name = models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    rating = models.FloatField()
    availability_start = models.TimeField()
    availability_end = models.TimeField()
    society=models.CharField(max_length=100)
    service_name=models.CharField(max_length=100,choices=SERVICE_CHOICES)

    def __str__(self):
        return self.name
    

class Cook(models.Model):
    name = models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    rating = models.FloatField()
    availability_start = models.TimeField()
    availability_end = models.TimeField()
    society=models.CharField(max_length=100)
    service=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Nanny(models.Model):
    name = models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    rating = models.FloatField()
    availability_start = models.TimeField()
    availability_end = models.TimeField()
    society=models.CharField(max_length=100)
    service=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Care_Taker(models.Model):
    name = models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    rating = models.FloatField()
    availability_start = models.TimeField()
    availability_end = models.TimeField()
    society=models.CharField(max_length=100)
    service=models.CharField(max_length=100)

    def __str__(self):
        return self.name