from django.urls import path
from .views import *
from django.conf.urls.static import static
from pinteresto import settings

urlpatterns = [
    path('', Index.as_view(), name='detail'),
    path('category/<str:slug>', get_category, name='category'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('detail/<str:slug>', PostView.as_view(), name='detail'),
    path('add-news/', CreateNews.as_view(), name='add_news'),
    path('update-news/<str:slug>', UpdateNews.as_view(), name='update_news'),
    path('delete-news/<str:slug>', DeleteNews.as_view(), name='delete_news'),
    path('home/', home, name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)