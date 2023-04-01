from django.urls import path

from . import views

urlpatterns = [
    path('api/cars', views.ListCreateCarView.as_view()),
    path('api/find-cars', views.ListCreateCarView.as_view()),
    path('api/cars/<int:pk>', views.UpdateDeleteCarView.as_view()),
]