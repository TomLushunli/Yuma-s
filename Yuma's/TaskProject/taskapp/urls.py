from django.urls import path
from .views import  listfunc, detailfunc, BoardCreate,CommentView
urlpatterns = [

    path('', listfunc, name='list'),
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('create', BoardCreate.as_view(), name='create'),
    path('comment/<int:pk>/',CommentView.as_view(),name='comment'),


]


from rest_framework import routers
from .views import UserViewSet, EntryViewSet


router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)