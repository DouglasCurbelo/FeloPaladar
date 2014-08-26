from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$','Web.views.home')
    url(r'^$','products.views.product_list'),
    (r'^restaurant_cart/', include('restaurant_cart.urls')),	
)
