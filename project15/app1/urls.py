from django.urls import path
from app1.views import *
app_name='app1'

urlpatterns=[
    path('dad/',dad,name='dad'),
    path('child1/',child1,name='child1'),

]