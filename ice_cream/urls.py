from django.urls import path
from . import views

app_name = 'ice_cream'

urlpatterns = [
    path(r'^delete/(?P<pk>[0-9]+)/$', views.icecream_delete, name='icecream_delete'),
    path('new/', views.CreateView.as_view(), name='create'),
    path('<int:ice_cream_id>/results/', views.results, name='results'),
    path('<int:ice_cream_id>/vote/', views.vote, name='vote'),
    path('<str:selection>/', views.index, name='selection'),
    path('', views.index, name='index'),
]
