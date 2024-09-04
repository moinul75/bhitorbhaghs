from django.urls import path  
from .views import (
    HomeView,
    AboutView,
    NoticeView,
    ContactView,
    AdmissionView,
    AcadamicsView,
    TeachersView, 
    StuentsView, 
    GallaryView, 
    ResultView,
    )



urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about/',AboutView.as_view(),name='about'),
    path('notice/',NoticeView.as_view(),name='notice'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('admission/',AdmissionView.as_view(),name='admission'),
    path('acadamics/',AcadamicsView.as_view(),name='acadamics'),
    path('teachers/',TeachersView.as_view(),name='teachers'),
    path('students/',StuentsView.as_view(),name='students'),
    path('gallary/',GallaryView.as_view(),name='gallary'),
    path('results/',ResultView.as_view(),name='results'),
]
