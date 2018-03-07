from django.conf.urls import url
from django.contrib import admin

from first import views

urlpatterns = [
    url(r'^.*', views.IndexPageView.as_view(), name='index'),
    # url(r'^admin/', admin.site.urls),
    # url(r'^products/$', views.product_list),
    # url(r'^products/(?P<pk>[0-9]+)$', views.product_detail),
    url(r'^families/$', views.family_list.as_view()),
    url(r'^families/(?P<pk>[0-9]+)$', views.family_detail.as_view()),
    url(r'^locations/$', views.location_list.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)$', views.location_detail.as_view()),
    url(r'^transactions/$', views.transaction_list.as_view()),
    url(r'^transactions/(?P<pk>[0-9]+)$', views.transaction_detail.as_view()),
    url(r'^preparation/', views.ExamList.as_view()),
]