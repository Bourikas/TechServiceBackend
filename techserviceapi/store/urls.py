from django.urls import path
from .views import CustomerDetailView, CustomerListView, DeviceListView, DeviceDetailView, StoreEntryDetailView, StoreEntryListView, TechnicianDetailView, TechnicianListView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customer_list"),
    path("customers/<int:pk>/", CustomerDetailView.as_view(),
    name="customer_detail"),
    path("devices/", DeviceListView.as_view(), name="device_list"),
    path("devices/<int:pk>/", DeviceDetailView.as_view(),
    name="device_detail"),
    path("store_entries/", StoreEntryListView.as_view(), name="store_entry_list"),
    path("store_entries/<int:pk>/", StoreEntryDetailView.as_view(),
    name="store_entry_detail"),
    path("technicians/", TechnicianListView.as_view(), name="technician_list"),
    path("technicians/<int:pk>/", TechnicianDetailView.as_view(),
    name="technician_detail"),
] 
