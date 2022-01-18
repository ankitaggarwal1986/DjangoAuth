from . models import Buyer,Sale,Machine
from rest_framework import serializers
from django.db.models import fields

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = "__all__"

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"

                

                

