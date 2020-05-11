from django.urls import path
from django.conf.urls import include 

# from rest_framework.routers import DefaultRouter
from rest_framework import routers

from .views import EntryListView

router= routers.DefaultRouter()
router.register('entries', EntryListView)

urlpatterns = [
    path('', include(router.urls)),
]