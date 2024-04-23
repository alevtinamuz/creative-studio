from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api
from . import consumers

urlpatterns = [
    path('users/', api.user_list, name='user_list'),
    path('me/', api.me, name='me'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search_by_name/', api.search_by_name, name='search_by_name'),
    path('search_by_email/', api.search_by_email, name='search_by_email'),
    # path('search_by_id/', api.search_by_id, name='search_by_id'),
    path('<str:user_id>/', api.search_by_id, name='search_by_id'),
    path('<str:user_id>/add_canv/', api.add_canv, name='add_canv'),
    path('<str:user_id>/get_canv/', api.get_canv, name='get_canv'),
    path("ws/", consumers.Consumer.as_asgi()),
]
