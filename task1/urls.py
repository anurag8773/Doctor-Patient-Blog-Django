from django.urls import path
from task1.views import signin,doctorsignup,home,patientsignup,signout,upload,blog,filter,myblog,myfilter,viewblog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home),
    path('home', home),
    path('signin', signin),
    path('signup/doctor', doctorsignup),
    path('signup/patient', patientsignup),
    path('signout/', signout),
    path('blog/upload/',upload),
    path('blog/',blog),
    path('blog/filter/<str:fl>',filter),
    path('blog/myblog/',myblog),
    path('blog/myblog/filter/<str:fl>',myfilter),
    path('blog/viewblog/<int:bno>',viewblog),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)