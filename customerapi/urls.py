from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from customerapi.views import InvoiceViewSet,InvoiceDetailViewSet



router = routers.DefaultRouter()
router.register(r"customerapi",InvoiceViewSet)
router.register(r'customer',InvoiceDetailViewSet)

urlpatterns = [
    path('',include(router.urls))
]