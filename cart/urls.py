from django.conf.urls import patterns, include, url

urlpatterns = patterns('ecomstore.cart.views',
    url(r'^$', 'views.show_cart', { 'template_name': 'cart/cart.html' }, 
    	name='show_cart'),
    # url(r'^$','products.views.product_list'),
)
