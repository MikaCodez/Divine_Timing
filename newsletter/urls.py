from django.urls import path
from . import views


urlpatterns = [
    path('subscriber', views.subscribers, name='subscriber'),
    path('add_subscriber', views.add_subscriber, name='add_subscriber'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('unsubscribe_registered_user', views.unsubscribe_registered_user,
         name='unsubscribe_registered_user'),
]