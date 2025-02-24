#!/ismailmwarumba/bin/env python
from django.urls import path
from django.contrib.auth import views as auth_views
from bambakofi import views
from .views import home,about_us,who_we_are,teaching_learning,staff,news_events,admissions
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('about-us/who-we-are/', who_we_are, name='who_we_are'),
    path('teaching-learning/', teaching_learning, name='teaching_learning'),
    path('staff/', staff, name='staff'),
    path('news-events/', news_events, name='news_events'),
    path('admissions/', admissions, name='admissions'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
