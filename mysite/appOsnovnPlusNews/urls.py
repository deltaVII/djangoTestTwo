from django.urls import path, include
from . import views
# основные ссылки
# написанные мной
urlpatterns = [
    path('main',views.man),
    path('form',views.form),
    path('post',views.post),
    path('posts/<int:post_id>/', views.idPosts),
]
# уже готовые
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),\
]
