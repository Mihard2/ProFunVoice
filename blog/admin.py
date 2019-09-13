from django.contrib import admin
from blog.models import (Slider, Longgrid, LonggridTag)

# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'public')

@admin.register(Longgrid)
class LonggridAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}    
    list_display = ('title', 'public', 'date_pub')

@admin.register(LonggridTag)
class LonggridTag(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    display = ('name')
