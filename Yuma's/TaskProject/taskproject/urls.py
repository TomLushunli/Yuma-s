from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import RedirectView

from taskapp.urls import router as blog_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskapp.urls')),
    url(r'^posts/',include(blog_router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=[re_path(r'^.*$',RedirectView.as_view(url='/posts/')),]