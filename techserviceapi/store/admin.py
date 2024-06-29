from django.contrib import admin
from store.models import Customer, StoreEntry, Device, User, Technician
# Register your models here.
admin.site.register(Customer)
admin.site.register(StoreEntry)
admin.site.register(Device)
admin.site.register(Technician)