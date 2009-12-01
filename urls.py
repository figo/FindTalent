from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
  # Example:
  # ( r'^FindTalent/', include( 'FindTalent.foo.urls' ) ),

  # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
  # to INSTALLED_APPS to enable admin documentation:
  # ( r'^admin/doc/', include('django.contrib.admindocs.urls' ) ),

  # Uncomment the next line to enable the admin:
  # ( r'^admin/', include( admin.site.urls ) ),
  ( r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.STATIC_DOC_ROOT } ),
  ( r'^error/$', 'common.views.error' ),
)

urlpatterns += patterns( 'account',
  ( r'^$',                  'views.login'   ),
  ( r'^account/login/$',    'views.login'   ),
  ( r'^account/sign_in/$',  'views.signin'  ),
  ( r'^account/sign_up/$',  'views.signup'  ),
  ( r'^account/sign_out/$', 'views.signout' ),
)

urlpatterns += patterns( 'show',
  ( r'^show/$', 'views.show' ),
)

urlpatterns += patterns( 'search',
  ( r'^search/$', 'views.search' ),
)
