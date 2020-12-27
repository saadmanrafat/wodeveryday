from django.contrib import admin
from .models import (
    Region,
    Country,
    City,
    Gym,
)

admin.site.register(Region)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Gym)

# Register your models here.
