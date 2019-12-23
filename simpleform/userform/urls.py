from django.urls import path
from . import views

app_name = 'userform'

urlpatterns = [
    path('',views.index,name='index'),

]