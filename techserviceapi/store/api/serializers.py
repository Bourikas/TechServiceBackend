from rest_framework import serializers
from store.models import Customer, Device, StoreEntry, Technician, User

class CustomerSerializer(serializers.ModelSerializer):

  #  devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"
       
    
class DeviceSerializer(serializers.ModelSerializer):

    owner = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    owner_details = CustomerSerializer(source='owner', read_only=True)

    class Meta:
        model = Device
        fields = ['id', 'owner', 'owner_details', 'maker', 'device_type', 'model_type', 'serial_number', 'date_of_purchase']

    def create(self, validated_data):
        owner = validated_data.pop('owner')
        device = Device.objects.create(owner=owner, **validated_data)
        return device


class StoreEntrySerializer(serializers.ModelSerializer):

    # device = DeviceSerializer(read_only=True)
#    technician = TechnicianSerializer(read_only=True)
    
    class Meta:
        model = StoreEntry
        fields = "__all__"

    def is_delivered(self, object):
        return object.return_date is not blank

class StoreEntryDetailedSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    owner = serializers.SerializerMethodField()

    class Meta:
        model = StoreEntry
        fields = [
            'id', 'malfunction_description', 'device_condition', 'entry_date', 
            'inspection_date', 'repair_date', 'return_date', 'repair_description',
            'repair_cost', 'part_description', 'part_cost', 'device', 'owner'
        ]

    def get_owner(self, obj):
        if obj.device and obj.device.owner:
            return CustomerSerializer(obj.device.owner).data
        return None

class TechnicianSerializer(serializers.ModelSerializer):

    # store_entries = StoreEntrySerializer(many=True, read_only=True)

    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Technician
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']