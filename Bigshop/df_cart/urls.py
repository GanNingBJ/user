from django.conf.urls import url
import views
from models import *

urlpatterns=[
    url('^$',views.list),
    url('^add(\d+)_(\d+)/$',views.add),
    url('^delete/$',views.delete),
    url('^count_change/$',views.count_change),
    url('^order/$',views.order),

]
