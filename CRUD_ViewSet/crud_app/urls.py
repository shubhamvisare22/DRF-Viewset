from django.urls import path
from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('list-emp',EmployeeViewSet.as_view({'get': 'list'}), name='list-emp'),
    path('retrieve-emp/<int:pk>/',EmployeeViewSet.as_view({'get': 'retrieve'}), name='retrieve-emp'),
    path('create-emp/',EmployeeViewSet.as_view({'post': 'create'}), name='create-emp'),
    path('update-emp/<int:pk>/',EmployeeViewSet.as_view({'put': 'update'}), name='update-emp'),
    path('partial_update-emp/<int:pk>/',EmployeeViewSet.as_view({'patch': 'partial_update'}), name='partial-update'),
    path('delete-emp/<int:pk>/',EmployeeViewSet.as_view({'delete': 'destroy'}), name='delete-emp'),
]
