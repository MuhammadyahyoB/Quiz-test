from . import views
from django.urls import path


urlpatterns = [
    path('', views.eror, ),
    path('<str:code>/', views.quiz_detail)
]