from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from store.models import Device, StoreEntry, Technician, Customer
from rest_framework import generics
from store.api.serializers import CustomerSerializer, StoreEntrySerializer, TechnicianSerializer, DeviceSerializer
# Create your views here.

class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"

class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html" 
 
class DeviceDetailView(DetailView):
    model = Device
    template_name = "devices/device_detail.html"

class DeviceListView(ListView):
    model = Device
    template_name = "devices/device_list.html"

class StoreEntryDetailView(DetailView):
    model = StoreEntry
    template_name = "store_entries/store_entry_detail.html"

class StoreEntryListView(ListView):
    model = StoreEntry
    template_name = "store_entries/store_entry_list.html"


class TechnicianDetailView(DetailView):
    model = Technician
    template_name = "technicians/technician_detail.html"

class TechnicianListView(ListView):
    model = Technician
    template_name = "technicians/technician_list.html"
    
