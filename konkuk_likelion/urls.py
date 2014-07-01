from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'promo_likelion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'konkuk_likelion.views.index'),
    url(r'^apply/', 'konkuk_likelion.apply.views.apply'),
    url(r'^admin/', include(admin.site.urls)),
    
)
