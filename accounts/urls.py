from django.conf.urls import url
from accounts import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^signup', csrf_exempt(views.SignUp.as_view())),
    url(r'^session', views.Session.as_view()),
]
