from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'student'
urlpatterns = [
    path('info/', views.info, name='info'),
    path('succeed/', views.succeed, name='succeed'),
    path('update/', views.update, name='update'),
]

router = DefaultRouter()
router.register(r"api/sex", views.SexInfoViewSet)
router.register(r"api/star", views.StarInfoViewSet)
router.register(r"api/geo1", views.Geo1ViewSet)
router.register(r"api/geo2", views.Geo2ViewSet)
router.register(r"api/geo3", views.Geo3ViewSet)
router.register(r"api/geo4", views.Geo4ViewSet)
router.register(r"api/province", views.ProvinceInfoViewSet)
urlpatterns += router.urls
