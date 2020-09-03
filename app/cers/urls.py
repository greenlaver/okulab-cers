from django.urls import path

from .views import AttendanceListView, PaperExport


urlpatterns = [
    path('', AttendanceListView.as_view(), name='attendance'),
    path('paper/', PaperExport, name='paper'),
]
