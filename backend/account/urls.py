from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('users/', api.user_list, name='user_list'),
    path('me/', api.me, name='me'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search_by_name/', api.search_by_name, name='search_by_name'),
    path('search_by_email/', api.search_by_email, name='search_by_email'),
]
