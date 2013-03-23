from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.views.generic import ListView
from apps.irgat.models import Atar

from apps.irgat.views import atar_yap

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'irgatimolurmusun.views.home', name='home'),
    # url(r'^irgatimolurmusun/', include('irgatimolurmusun.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',      atar_yap),
    url(r'^atarlar$', ListView.as_view(
                           queryset=Atar.objects.aktif(),
                           template_name="irgat/atar_list.html",
                           paginate_by = 5)),
)

