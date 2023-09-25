from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category)  # registers new Stock class model from Models file
admin.site.register(models.Item)  # registers new Stock class model from Models file