from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ice_cream_id>/', views.detail, name='detail'),

]
