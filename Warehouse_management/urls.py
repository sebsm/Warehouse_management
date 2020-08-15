"""
Definition of urls for Warehouse_management.
"""

from django.contrib import admin
from django.urls import path, include
#from login_logout.views import WMLogin, WMLogout, WMAuth
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
 #path('', views.home, name='home'),
    #path('home/', views.home, name='home'),
    #path('contact/', views.contact, name='contact'),
    #path('about/', views.about, name='about'),
    #path('login/', WMAuth, name= 'login'),
    #path('logout/', WMLogout, name='logout'),
    #path('login_logout/', include('login_logout.urls')),
urlpatterns = [
    #path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls'), name ='home'),
    
]



if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)