from django.urls import path

from . import api


urlpatterns = [
    path('', api.canvas_list, name='canvas_list'),
    path('feed/<str:id>/', api.canvas_list_feed, name='canvas_list_feed'),
    path('create/', api.canvas_create, name='canvas_create'),
    path('search_canvas_by_user/', api.search_canvas_by_user, name='search_canvas_by_user'),
     path('<str:canvas_id>/', api.get_canvas_by_id, name='get_canvas_by_id'),
     path('<str:canvas_id>/update/', api.canvas_update, name='canvas_update'),
     path('<str:canvas_id>/delete/', api.delete_canvas, name='delete_canvas'),

]
