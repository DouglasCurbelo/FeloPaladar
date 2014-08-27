from django.conf.urls import patterns, include, url

urlpatterns = patterns('restaurant_cart.views',    
    url(r'^$','get_cart'),
    url(r'^add_plate/(\d+)/$','add_plate_to_cart',name='add_plate_to_cart')
)
