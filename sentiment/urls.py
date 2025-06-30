from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_sentiment, name='sentiment_form'),
    path('result/<int:pk>/', views.show_result, name='sentiment_result'),
    path('messages/', views.message_list, name='message_list'),
]
