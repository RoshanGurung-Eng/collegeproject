from django.shortcuts import render
from rest_framework import generics, viewsets
from .serialization import *
from .models import * 
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class CutomerGetView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDestroyView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


from django.conf import settings

class EsewaPaymentView(APIView):
    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')
        amount = request.data.get('amount')

        try:
            order = VehicleOrders.objects.get(id=order_id)
        except VehicleOrders.DoesNotExist:
            return Response({'error': 'Order not found'}, status=404)

        payment = esewaPayment.objects.create(
            esewa_order_id=order_id,
            amount=amount,
            order=order
        )

        payment_url = (
            f"{settings.ESEWA_PAYMENT_URL}?"
            f"amount={amount}&"
            f"pcd=0&psc=0&txnid=0&"
            f"tAmt={amount}&pid={payment.esewa_order_id}&"
            f"scd={settings.ESEWA_MERCHANT_ID}&"
            f"su={settings.ESEWA_SUCCESS_URL}&fn={settings.ESEWA_FAILED_URL}&"
        )

        return Response(payment_url)
    

class EsewaCallBackView(APIView):
    def post(self, request, *args, **kwargs):
        status_param = request.query_params.get('status')
        pid = request.query_params.get('oid')
        refId = request.query_params.get('refId')

        if status_param == 'success':
            try:
                payment = esewaPayment.objects.get(esewa_order_id=pid)
            except esewaPayment.DoesNotExist:
                return Response({'error': 'Payment not found'}, status=404)
            
            verification_url = (
                f"https://uat.esewa.com.np/epay/transrec?amt={payment.amount}&"
                f"scd={settings.ESEWA_MERCHANT_ID}"
                f"pid={payment.esewa_order_id}&rid={refId}"
            )
            
            response = request.post(verification_url)

            if response.status_code == 200:
                payment.status = "Success"
                payment.save()
                return Response({'success': 'Payment successful'}, status=200)
            else:
                payment.status = "Failed"
                payment.save()
                return Response({'error': 'Payment failed'}, status=400)

        else:
            return Response({'error': 'Payment failed'}, status=400)



