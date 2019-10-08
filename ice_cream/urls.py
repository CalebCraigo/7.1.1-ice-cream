from django.urls import path
from . import views

urlpatterns = [
    path('<int:ice_cream_id>/', views.detail, name='detail'),
    path('<int:ice_cream_id>/results/', views.results, name='results'),
    path('', views.index, name='index'),

]
