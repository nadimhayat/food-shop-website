
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food_products/', include('food_products.urls')),
    path('about', views.about, name='about_us'),
    path('', views.homepage, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)