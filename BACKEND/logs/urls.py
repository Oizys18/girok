from django.urls import path
from . import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='GIROK API',
        default_version='v1',
    )
)

app_name = 'logs'

urlpatterns = [
    path('', views.logs, name='logs')
]
