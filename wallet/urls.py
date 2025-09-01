from django.urls import path
from . import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions





schema_view = get_schema_view(
    openapi.Info(
        title="Wallet API",
        default_version='v1',
        description="API documentation for Wallet Project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)







urlpatterns = [
    path("", views.home, name="home"),  # <-- FIX for /
    path('users/', views.list_users, name='list_users'),
    path('wallet/update/', views.update_wallet, name='update_wallet'),
    path('transactions/<int:user_id>/', views.fetch_transactions, name='fetch_transactions'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]