from rest_framework import serializers
from .models import Product , Location ,Family ,Transaction

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location 
        fields = ('reference','title', 'description')

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family 
        fields = ('title', 'description','unit','minQuantity')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product 
        fields = ('sku','barcode', 'title', 'description','location','family')

class TransactionSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    class Meta:
        model = Transaction 
        fields = ('sku', 'barcode','product')