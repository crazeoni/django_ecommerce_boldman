from django.urls import path
from . import views
from boldmann_wears.views import (
	remove_from_cart,
    reduce_quantity_item,
    add_to_cart,
    HomeView,
    ProductView,
    OrderSummaryView
)


app_name = 'boldmann_wears'
urlpatterns = [
	path('', views.home, name='home'),
	path('products/', HomeView.as_view(), name='products'),
	path('product/<pk>/', ProductView.as_view(), name='product'),
	path('categories/', views.category, name='category'),
	path('categories/boots/', views.boots, name='boots'),
	path('categories/monkstrap/', views.monkstrap, name='monkstrap'),
	path('categories/loafers/', views.loafers, name='loafers'),
	path('categories/leather_slides/', views.leather_slides, name='leather_slides'),
	path('categories/oxfords/', views.oxfords, name='oxfords'),
	path('categories/brogues/', views.brogues, name='brogues'),
	path('categories/leather_mules/', views.leather_mules, name='leather_mules'),
	#path('products/product_overview/<int:product_id>', views.product_overview, name='product_overview'),
	path('order-summary', OrderSummaryView.as_view(), name='order_summary'),
    path('add-to-cart/<pk>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove_from_cart'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce_quantity_item')
]



