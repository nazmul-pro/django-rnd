from django.contrib import admin

# Register your models here.
from .models import Product , Location ,Family ,Transaction

admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Family)
admin.site.register(Transaction)