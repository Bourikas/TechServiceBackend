from django.urls import path
from store.api.views import UserDetailView,StoreEntryDetailedListCreateAPIView,TechnicianDetailAPIView,TechnicianListCreateAPIView,StoreEntryDetailAPIView,   StoreEntryListCreateAPIView,DeviceListCreateAPIView,DeviceDetailAPIView, CustomerListCreateAPIView, CustomerDetailAPIView, TechnicianRegister,CheckDuplicateEmailView


urlpatterns = [
path('customers/', CustomerListCreateAPIView.as_view(), name="customers-list"),
path('customers/<int:pk>/', CustomerDetailAPIView.as_view(), name="customer-detail"),

path('devices/', DeviceListCreateAPIView.as_view(), name="devices-list"),
path('devices/<int:pk>/', DeviceDetailAPIView.as_view(), name="device-detail"),

path('store_entries/', StoreEntryListCreateAPIView.as_view(), name="store-entry-list"),
path('store_entries_detailed/', StoreEntryDetailedListCreateAPIView.as_view(), name="store-entry-detailed-list"),
path('store_entries/<int:pk>/', StoreEntryDetailAPIView.as_view(), name="store-entry-detail"),



path('technicians/', TechnicianListCreateAPIView.as_view(), name="technicians-list"),
path('technicians/<int:pk>/', TechnicianDetailAPIView.as_view(), name="technicians-detail"),
path('technicians/register/', TechnicianRegister.as_view(), name='technician_register'),

path('check-duplicate-email/', CheckDuplicateEmailView.as_view(), name='check-duplicate-email'),
path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]