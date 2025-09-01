from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.list_users, name='list_users'),
    path('wallet/update/', views.update_wallet, name='update_wallet'),
    path('transactions/<int:user_id>/', views.fetch_transactions, name='fetch_transactions'),

]