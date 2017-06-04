from django.conf.urls import url
import views
urlpatterns=[
    url('^$',views.index),
    url('^login/$',views.login),
    url('^register/$',views.register),
    url('^register2/$',views.register2),
    url('^login2/$',views.login2),
    url('^site/$',views.site),
    url('^user_center_info.html/$',views.user_center_info),
    url('^user/site/$',views.site),

]