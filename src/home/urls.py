
from django.conf.urls import url
from .views import HomeView, AjaxHomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^ajax/$', AjaxHomeView.as_view(), name='ajax_home')
]
