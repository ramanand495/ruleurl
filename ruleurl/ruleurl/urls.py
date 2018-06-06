from django.conf.urls import url
from django.contrib import admin
from user_auth import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.user_login,name='user_login'),
    url(r'^logout/',views.user_logout,name='user_logout'),
    url(r'^admin/', admin.site.urls),
]
