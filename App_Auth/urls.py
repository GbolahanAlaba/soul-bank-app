from django.urls import path, include
from . import views
from . views import *
from knox import views as knox_views


#  SWAGGER
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Soul Bank API",
      default_version='v1',
      description="This is HOF Soul Bank App API Doc",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jedida@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path('create-auth/', SetupViewSets.as_view({"post": "create_auth_code"}), name='auth-create'),
   path('create-team/', SetupViewSets.as_view({"post": "create_team"}), name='team-create'),
   path('create-sector/', SetupViewSets.as_view({"post": "create_sector"}), name='sector-create'),
   path('signin/', AuthViewSets.as_view({"post": "signin"}), name='signin'),
   path('signup/', AuthViewSets.as_view({"post": "signup"}), name='signup'),

   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('go/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]