from django.urls import path,include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



# router = routers.SimpleRouter()
# router.register(r'articles', views.ArticleList,basename='Article')
# router.register(r'tags', views.TagList,basename='Tag')
# router.register(r'ArticleSource', views.SourceList,basename='Source')

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:articleId>', views.details, name='details'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/articles', views.ArticleList.as_view(), name='articleApi'),
    re_path('api/articles/(?P<date>.+)/$', views.ArticleByDate.as_view(),name='articleByDateApi'),
    re_path('api/articles/(?P<tag>.+)/$', views.ArticleByTag.as_view(),name='articleByTagApi'),
    path('api/tags', views.TagList.as_view(), name='tagApi'),
    path('api/sources', views.SourceList.as_view(), name='sourceApi'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]