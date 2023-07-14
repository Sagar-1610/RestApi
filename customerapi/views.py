from django.shortcuts import render
from rest_framework import viewsets
from customerapi.models import Invoice,InvoiceDetail
from customerapi.serializers import InvoiceSerializers,InvoiceDetailSerializers


# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializers


class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializers