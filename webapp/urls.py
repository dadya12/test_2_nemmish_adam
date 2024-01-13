from django.urls import path
from django.views.generic import RedirectView

from webapp.views.product_views import (ProductListView, ProductDetailView, ProductCreateView,
                                        ProductUpdateView, ProductDeleteView)
from webapp.views.revew_views import ReviewCreateView

app_name = 'webapp'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/', RedirectView.as_view(pattern_name='webapp:home')),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('product/add/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('products/<int:pk>/review/add/', ReviewCreateView.as_view(), name='create_review'),
]
