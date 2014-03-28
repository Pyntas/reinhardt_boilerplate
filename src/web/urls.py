from django.conf.urls import patterns, url, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


#Site
site_urlpatterns = patterns('web.views',
    url(r'^$', TemplateView.as_view(template_name='web/index.html')),
)


urlpatterns = i18n_patterns('',
    url(r'^', include(site_urlpatterns)),
)
