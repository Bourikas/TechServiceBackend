from rest_framework import generics
from rest_framework import mixins
from store.models import Customer, Device, StoreEntry, Technician
from store.api.serializers import UserSerializer, StoreEntrySerializer,StoreEntryDetailedSerializer, CustomerSerializer, TechnicianSerializer, DeviceSerializer 
from rest_framework import permissions
from store.api.permissions import IsAdminUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from store.forms import TechnicianRegistrationForm



class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    search_fields = ["last_name", "phone_number", "email"]
    permission_classes = [IsAuthenticated] 

class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated] 



class DeviceListCreateAPIView(generics.ListCreateAPIView):
    # permission_classes = [IsAdminUserOrReadOnly] 

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    search_fields = ["serial_number", "maker", "device_type","model_type"]
    permission_classes = [IsAuthenticated] 

class DeviceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUserOrReadOnly] 
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated] 



class StoreEntryListCreateAPIView(generics.ListCreateAPIView):
    queryset = StoreEntry.objects.all()
    serializer_class = StoreEntrySerializer
    
    search_fields = ["device", "technician"]
    permission_classes = [IsAuthenticated] 

class StoreEntryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreEntry.objects.all()
    serializer_class = StoreEntrySerializer
    permission_classes = [IsAuthenticated] 

class StoreEntryDetailedListCreateAPIView(generics.ListCreateAPIView):
    queryset = StoreEntry.objects.all()
    serializer_class = StoreEntryDetailedSerializer
    
    search_fields = ["device", "technician"]
    permission_classes = [IsAuthenticated] 


class TechnicianListCreateAPIView(generics.ListCreateAPIView):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer
    permission_classes = []
    search_fields = ["user", "last_name", "first_name", "shop"]
    permission_classes = [IsAuthenticated] 

class TechnicianDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer
    permission_classes = [IsAuthenticated] 

class LookupStoreEntry(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        serial_number = request.data.get('serial_number')

        if not phone_number or not serial_number:
            return Response({'error': 'Phone number and serial number are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            customer = get_object_or_404(Customer, phone_number=phone_number)
            device = get_object_or_404(Device, serial_number=serial_number, owner=customer)
            store_entry = StoreEntry.objects.filter(device=device).latest('entry_date')
            serializer = StoreEntrySerializer(store_entry)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Device.DoesNotExist:
            return Response({'error': 'Device not found.'}, status=status.HTTP_404_NOT_FOUND)
        except StoreEntry.DoesNotExist:
            return Response({'error': 'No store entries found for this device.'}, status=status.HTTP_404_NOT_FOUND)

class TechnicianRegister(APIView):
    def post(self, request):
        form = TechnicianRegistrationForm(request.data)
        if form.is_valid():
            # Create User
            user = User.objects.create(
                username=f"{form.cleaned_data['first_name'].lower()}{form.cleaned_data['last_name'].lower()}",
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password']),
            )
            # Create Technician
            technician = form.save(commit=False)
            technician.user = user
            technician.save()
            return Response({"message": "Technician registered successfully!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckDuplicateEmailView(APIView):
    def get(self, request):
        email = request.query_params.get('email', None)
        if email:
            if User.objects.filter(email=email).exists():
                return Response({'exists': True}, status=status.HTTP_200_OK)
            else:
                return Response({'exists': False}, status=status.HTTP_200_OK)
        return Response({'error': 'Email parameter not provided'}, status=status.HTTP_400_BAD_REQUEST)            

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 
