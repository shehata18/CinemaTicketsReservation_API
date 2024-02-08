"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from tickets import views 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('guests',views.Viewsets_guest)
router.register('movies', views.Viewsets_movie)
router.register('reservations', views.Viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1 
    path('django/JsonResponseNoModel', views.no_rest_no_model),
    # 2 
    path('django/JsonResponseFromModel', views.no_rest_from_model),
# -----------------------------------------------------------------------------------

    # 3.1 GET POST from REST framework - Function Based View (@api_view)
    path("rest/fbv/", views.FBV_List),
    
    # 3.2 GET PUT DELETE from REST framework - Function Based View (@api_view)
    path("rest/fbv/<int:pk>", views.FBV_pk),
    
# -----------------------------------------------------------------------------------

    # 4.1 GET POST  from REST framework - Class Based View APIView)
    path("rest/cbv", views.CBV_List.as_view()),

    # 4.2 GET PUT DELETE from REST framework - Class Based View (APIView)
    path("rest/cbv/<int:pk>", views.CBV_pk.as_view()),

# -----------------------------------------------------------------------------------

    # 5.1 5.1 mixins list GET POST  from REST framework - Class Based View (mixins)
    path("rest/mixins", views.mixins_list.as_view()),

    # 5.2 GET PUT DELETE from REST framework - Class Based View (mixins)
    path("rest/mixins/<int:pk>", views.mixins_pk.as_view()),

# -----------------------------------------------------------------------------------

    # 6.1 GET POST from REST framework - Class Based View (Generics)
    path("rest/generics", views.generics_list.as_view()),

    # 6.2 GET PUT DELETE from REST framework - Class Based View (Generics)
    path("rest/generics/<int:pk>", views.generics_pk.as_view()),

# -----------------------------------------------------------------------------------

    # 7 Viewsets
    path('rest/viewsets/',include(router.urls)),
# -----------------------------------------------------------------------------------

    # 8 find movie by FBV
    path('fbv/findmovie',views.find_movie),
    
    # 9 New reservation by FBV
    path('fbv/newreservation', views.new_reservation),
]
