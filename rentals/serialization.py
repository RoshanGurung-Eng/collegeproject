from rest_framework import serializers
from .models import *
from vheicles.models import Vehicle

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CarOrdersSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), many=True)
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = CarOrders
        fields = ['id','name', 'address', 'phone','vehicle', 'quantity', 'user', 'orderStatus', 'created_at']
        read_only_fields = ['orderStatus', 'created_at']
    
    def create (self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
    
    
class EsewaPaymentSerializer(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(queryset=CarOrders.objects.all(), many=True)
    esewa_order_id = serializers.CharField(max_length=255)
    amount = serializers.IntegerField()

    class Meta:
        model = esewaPayment
        fields = ['id', 'esewa_order_id', 'amount', 'order_id', 'status', 'created_at']
        read_only_fields = ['status','created_at']

    # to validate the the data from esewa payment https://uat.esewa.com.np/epay/transrec   {
    def create(self, validated_data):
        payment = esewaPayment.objects.create(
            esewa_order_id=validated_data['esewa_order_id'],
            amount=validated_data['amount'],
            order=validated_data['order_id'],
            status = "Pending"
        )
        return payment