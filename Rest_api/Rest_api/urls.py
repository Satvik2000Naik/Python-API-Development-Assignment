
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/', views.bookList.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
