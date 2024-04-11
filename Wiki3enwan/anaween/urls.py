from django.urls import path
from .views import enwaanDetailView
from . import views
from .views import SignUpView


urlpatterns = [
    path('', views.Home, name='Home'),
    path('add-enwaan/', views.add_enwaan, name="add_enwaan"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('<slug:slug>/', enwaanDetailView.as_view(), name='enwaan_detail'),
    path('<slug:slug>/edit/', views.enwaanEditView.as_view(), name='edit_enwaan')
    
]