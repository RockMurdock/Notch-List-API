"""notchlist URL Configuration

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
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from notchlistApi.models import *
from notchlistApi.views import *
from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', Users, 'user')
router.register(r'beers', Beers, 'beer')
router.register(r'wines', Wines, 'wine')
router.register(r'cocktails', Cocktails, 'cocktail')
router.register(r'glasswares', Glasswares, 'glassware')
router.register(r'beer_serving_styles', Beer_Serving_Styles, 'beer_serving_style')
router.register(r'drink_styles', Drink_Styles, 'drink_style')
router.register(r'cocktail_ingredients', Cocktail_Ingredients, 'cocktail_ingredient')
router.register(r'ingredients', Ingredients, 'ingredient')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
