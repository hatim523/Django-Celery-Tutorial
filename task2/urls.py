from django.urls import path

from . import views

app_name = "task2"

urlpatterns = [
    path('', views.ReviewEmailView.as_view(), name='review'),
]