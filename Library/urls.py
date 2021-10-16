from django.contrib import admin
from django.db import router
from django.urls import path
from books.views import BookViewSet
from editorials.views import EditorialViewSet
from autors.views import AutorViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('editorials',EditorialViewSet)
router.register('autors',AutorViewSet)
router.register('books',BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
]+router.urls
