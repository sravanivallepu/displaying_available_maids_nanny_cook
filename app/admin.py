from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(Profile)

admin.site.register(Service)

admin.site.register(Booking)

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('rating', 'name', 'comment')
    list_filter = [ 'name']
    search_fields = ['comment']
    
admin.site.register(Review, ReviewAdmin)

admin.site.register(Book_cook)

admin.site.register(Book_maid)

admin.site.register(Book_nanny)

admin.site.register(Maid)

admin.site.register(Cook)

admin.site.register(Nanny)

admin.site.register(Care_Taker)