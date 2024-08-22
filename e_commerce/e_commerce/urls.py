"""
URL configuration for e_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from e_app.views import home, contact
from e_app.product_seller import product_salers, pro_sal_view, update_sal, delete_sal
from e_app.consumer import consumer_reg, view, update, delete, con_login, con_logout, searchbar, buying, final, pview, my_purchase, about
from e_app.Selling import postproduct, login, logout, my_products, pro_update, pro_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('salreg/', product_salers, name="salreg"),
    path('conreg/', consumer_reg),
    path('selview/', pro_sal_view),
    path('update_sal/<id>/', update_sal, name="updatesal"),
    path('deletesal/<id>/', delete_sal, name="deletesal"),
    path('view/', view),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
    path('product/<email>/', postproduct, name="product"),
    path('pslogin/', login, name="pslogin"),
    path('pslogout/', logout, name="pslogout"),
    path('myview/<email>/', my_products, name='myview'),
    path('updatepro/<id>/', pro_update, name='updatepro'),
    path('deletepro/<id>/', pro_delete, name='deletepro'),
    path('cuslogin/', con_login),
    path('cuslogout/<email>/', con_logout, name='cuslogout'),
    path('searchbar/<email>/', searchbar, name='search'),
    path('buy/<no>/<cemail>/', buying, name='purchase'),
    path('buyed/<no>/<cons>/<qty>/<amt>/', final, name="final"),
    path('pview/<pno>/<cemail>/', pview, name='pview'),
    path('buyedproducts/<email>/', my_purchase, name="buyedproducts"),
    path('contact/', contact),
    path('about/', about),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)