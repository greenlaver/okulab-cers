from django.urls import path

from .views import AttendanceAPIView, UserRetrieveAPIView, UserListAPIView


urlpatterns = [
    path('attendance/', AttendanceAPIView.as_view()),
    path('user/<str:number>/', UserRetrieveAPIView.as_view()),
    path('user/', UserListAPIView.as_view()),
]
