"""



"""

from rest_framework import serializers

from models import CustomUser, Group, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id','street_details', 'city', 'state', 'country')


class UserSerializer(serializers.ModelSerializer):
    print 'hererere'
    location =  AddressSerializer(many=False, read_only=False)


    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'blood_group', 'mobile_no', 'last_donated', 'location', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
