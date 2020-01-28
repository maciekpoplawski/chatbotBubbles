from django.urls import path
from bubblesbot.views import ChatterBotAppView, ChatterBotApiView, ChatterBotTest

urlpatterns = [
    path('', ChatterBotAppView.as_view(), name='main'),
    path('chatterbotapi/', ChatterBotApiView.as_view(), name='chatterbot'),
    path('test/', ChatterBotTest.as_view(), name='test'),
]
