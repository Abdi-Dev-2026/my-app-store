from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('request-download/<int:product_id>/', views.request_download, name='request_download'),
    path('my-apps/', views.my_apps, name='my_apps'),
    path('buy-with-points/<int:product_id>/', views.buy_with_points, name='buy_with_points'),
    path('favorite/<int:product_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.my_favorites, name='favorites'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]