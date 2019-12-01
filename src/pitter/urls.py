from django.urls import include
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from api_client.views import registration_view, login_view, make_delete_pitt_view, save_pitt_view, follow_view, \
    getusers_view, finduser_view, feed_view


SchemaView = get_schema_view(
    openapi.Info(title="Pitter API", default_version='v1', description="Pitter REST API"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

API_V1_URLS = [
    path('mobile/', include(('api_client.urls', 'pitter_client'), namespace='pitter_client')),
]

urlpatterns = [  # pylint: disable=invalid-name
    path('api/pitter/v1/', include((API_V1_URLS, 'pitter'), namespace='v1')),
    path('api/pitter/swagger/', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
<<<<<<< HEAD
    path('registration/', registration_view.Registration.as_view(), name='registration'),
    path('login/', login_view.Login.as_view(), name='user'),
    path('makepitt/', make_delete_pitt_view.MakeDeletePitt.as_view(), name='pitt'),
    path('savepitt/', save_pitt_view.SavePitt.as_view(), name='save_pitt'),
    path('follow/', follow_view.Follow.as_view(), name='follow'),
    path('users/', getusers_view.GetUsers.as_view(), name='users'),
    path('finduser/', finduser_view.FindUser.as_view(), name='finduser'),
    path('feed/', feed_view.Feed.as_view(), name='feed'),
=======
    path('registration/', views.registration),
    path('login/', views.login),
    path('auth/', views.auth),
    path('makepitt', views.makepitt),
    path('savepitt/', views.savepitt),
    path('follow/', views.follow),
    path('users/', views.getusers),
    path('finduser/', views.finduser),
>>>>>>> master
]

