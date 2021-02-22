from django.urls import path
from .views import main, RoomView

urlpatterns = [
    path('', main),
    path('rooms', RoomView.as_view()),
]
