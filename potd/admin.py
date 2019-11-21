from django.contrib import admin
from django import forms
from .models import PhotoOfTheDay

class PhotoOfTheDayAdmin(admin.ModelAdmin):
    list_display = ('title', 'photographer', 'feature_potd', 'featured_as_potd', 'photographer_url')

admin.site.register(PhotoOfTheDay, PhotoOfTheDayAdmin)