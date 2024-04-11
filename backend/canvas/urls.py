from django.urls import path

from . import api


urlpatterns = [
    path('', api.canvas_list, name='canvas_list'),
    path('create/', api.canvas_create, name='canvas_create'),
]
