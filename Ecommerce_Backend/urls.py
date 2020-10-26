"""Ecommerce_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.urls import path

# from rest_framework import routers
from Ecommerce_Backend.ecommerce import views

# router = routers.DefaultRouter()
# router.register(r'users', views.userView)
# #router.register(r'products', views.GroupViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('users/<int:num>', views.userView),
    path('addUsers/', views.userView),
    path('addProducts/', views.productView),
    path('auth/', views.authView),
    path('products/edit', views.updateProductView),
    path('products/', views.showAllProductsView),
    path('products/<slug:id>', views.showAProductView),
    path('products/<slug:id>/order/', views.orderProductView),
    path('user/myOrders/', views.myOrdersView),
    path('agent/<slug:id>/updateOrderStatus/', views.updateOrderStatusView),


   #url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

#urlpatterns = patterns(
#    'entities.views',
#    # api
#    url(r'^$', 'userView'),
#)