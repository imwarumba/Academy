#!/ismailmwarumba/bin/env python
from django.urls import path
from django.contrib.auth import views as auth_views
from bambakofi import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
    path('',views.about, name='about'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
