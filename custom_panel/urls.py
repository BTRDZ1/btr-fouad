from django.urls import path
from .views import ClientDataListView

urlpatterns = [
    path('clientdata/', ClientDataListView.as_view(), name='clientdata-list'),
]
