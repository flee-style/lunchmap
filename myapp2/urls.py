from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lunchmap/',include('lunchmap.urls')),
    path('accounts/',include('account.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',RedirectView.as_view(url='/lunchmap/')),
]
