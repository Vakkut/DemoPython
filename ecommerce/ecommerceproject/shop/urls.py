
from django.urls import path
from . import views
app_name='shop'
from ecommerceproject import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.allProductCat,name='allProductCat'),
    path('<slug:c_slug>/',views.allProductCat,name='products by category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatedetail')
]
