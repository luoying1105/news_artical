from django.conf.urls import url
from . import views
import django.contrib.auth.views as auth_views   #不这样做汇报错
urlpatterns = [
    # 用DJANGO默认的来组建
    url(r'^login/$',
        auth_views.login,
        name='login'),
    url(r'^logout/$',
        auth_views.logout,
        name='logout'),
    url(r'^logout-then-login/$',
        auth_views.logout_then_login,
        name='logout_then_login'),
    # url(r'^login/$', views.user_login, name='login'),
]
