from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return f"{ self.first_name } { self.last_name }"

class Device(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    maker = models.CharField(max_length=50, null=True, blank=True)
    device_type = models.CharField(max_length=50)
    model_type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, unique=True)
    date_of_purchase = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{ self.model_type } { self.maker } { self.device_type } {self.owner} "

class StoreEntry(models.Model):
    malfunction_description = models.TextField()
    device_condition = models.TextField()
    entry_date = models.DateTimeField()
    inspection_date = models.DateTimeField(null=True, blank=True)
    repair_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    repair_description = models.TextField(null=True, blank=True)
    repair_cost = models.FloatField(null=True, blank=True)
    part_description = models.CharField(max_length=50, null=True, blank=True)
    part_cost = models.FloatField(null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    technician = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"StoreEntry {self.id} - {self.device.device_type}"

class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #connects users with technicians as one to one
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    bio = models.CharField(max_length=240, blank=True)
    shop = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            # Create a new user instance
            user = User.objects.create(
                username=f'{self.first_name.lower()}{self.last_name.lower()}',
                email=self.email,
                password='defaultpassword',  # You should hash the password or prompt the user to set it
            )
            self.user = user

        super(Technician, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"