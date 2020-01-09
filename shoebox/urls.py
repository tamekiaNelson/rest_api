"""shoebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shoebox import views, models
from django.conf.urls import include, url
from rest_framework import routers


admin.site.register(models.Manufacturer)
admin.site.register(models.ShoeType)
admin.site.register(models.ShoeColor)
admin.site.register(models.Shoe)


router = routers.DefaultRouter()
router.register(r'maker', views.ManufactureViews)
router.register(r'style', views.ShoeTypeViews)
router.register(r'color', views.ShoeColorViews)
router.register(r'shoe', views.ShoeViews)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls))
]
