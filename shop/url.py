from django.urls import path
from .views import ProductView,UserView


urlpatterns = [
    path('task/', ProductView.as_view()),
    path('task/<int:pk>/', ProductView.as_view()),
    path('user/', UserView.as_view()),
    path('user/<int:pk>/', UserView.as_view()),
]
