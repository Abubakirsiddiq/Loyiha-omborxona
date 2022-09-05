from django.urls import path
from rest_framework import permissions
from asosiy.views import *
from statapp.views import *
from userapp.views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Bu loyiha Omborlar  uchun",
      contact=openapi.Contact(email="Nabiyev Abubakirsiddiq: <nabiyevabubakirsiddiq@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('token-ber/', TokenObtainPairView.as_view(), name='token_olish'),
    path('token-yangi/', TokenRefreshView.as_view(), name='token_yangilash'),
    path('ombor/', OmborAPIView.as_view()),
    path('clientlar/', ClientlarAPIView.as_view()),
    path('client/<int:pk>/', ClientAPIView.as_view()),
    path('mahsulotlar/', MahsulotlarAPIView.as_view()),
    path('mahsulot/<int:pk>/', MahsulotAPIView.as_view()),
    path('statslar/', StatslarAPIView.as_view()),
    path('stats/<int:pk>/', StatsAPIView.as_view())
]

