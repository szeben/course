from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListCreateCourses.as_view(), name = 'course_list'),
    url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroyCourses.as_view(), name = 'course_detail')
]