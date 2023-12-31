from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register("hello-viewset", views.HelloViewset, basename="hello-viewset")
router.register("profile", views.UserProfilViewset,)
urlpatterns = [
    path("hello-view/<pk>",  views.HelloApiView.as_view()),
    path("login", views.UserLoginApiView.as_view()),

    path("", include(router.urls))
]
