from django.contrib import admin
from django.urls import path, include
from users_app import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.index, name='index'),
    path('services/', include('dockerimage_app.urls')),
    path('account/', include('users_app.urls')),
    path('contact', users_views.contact, name='contact'),
    path('about', users_views.about, name='about'),

]
