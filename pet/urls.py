from django.urls import path
from . import views

urlpatterns =[
    path('index.html', views.index,name='index'),
    path('index2.html', views.index2,name='index2'),
    path('index3.html', views.index3,name='index3'),
    path('index4.html', views.index4,name='index4'),
    path('index5.html', views.index5,name='index5'),
    path('index6.html', views.index6,name='index6'),
    path('get_sensor_data', views.get_sensor_data),
    path('get_speed_history', views.get_speed_history),
    path('feed', views.feed),
]