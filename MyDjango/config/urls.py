from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import re_path
from  django.contrib import admin
from django.urls import path
from django.urls import  include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from  django.views.generic import  TemplateView

from  rest_framework import  permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(
    title='My Api',
    default_version='v 0.0.1',
    description='My description',
    terms_of_service='https://www.google.com/polisies/terms',
    contact=openapi.Contact(email='hjhj@qwe.com'),
    license=openapi.License(name='BSD license'),
    ),
    patterns=[ path('',include('api.urls')), ],
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

# from rest_framework_simplejwt.views import TokenObtainPairView, \
#     TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    #Api urls
    path('',include('api.urls')),
    path('api/authentication/',include('authentication.urls')),

    # Auth endpoints
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),


    #debug toolbar
    path('__debug__/', include('debug_toolbar.urls')),


    #swagger UI
    path('swagger-ui/',TemplateView.as_view(
        template_name='swagger/swagger_ui.html',
        extra_context={'schema_url':'openapi-schema'},
    ),
        name ='swagger-ui',
    ),

    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout = 1),
        name = 'schema-json',
    ),

     ]



if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

else:
    urlpatterns += staticfiles_urlpatterns()