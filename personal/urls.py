from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('insert',views.insert),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),

]


