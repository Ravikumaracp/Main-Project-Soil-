from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path("about/",views.about,name='about'),
    path("soilprediction/",views.soilprediction,name="soilprediction"),
    path("croppredictiopn/",views.croppredictiopn,name="croppredictiopn"),
    path("plantprediction/",views.plantprediction,name="plantprediction"),
    path("result/",views.result,name="result")
    
]