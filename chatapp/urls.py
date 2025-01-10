from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Changed to root URL
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('chat/', include('chat.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''The line static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) sets up a URL route in your Django application that allows users to access media files stored on the server. When a user accesses a URL that starts with MEDIA_URL, Django will serve the corresponding file from the directory specified by MEDIA_ROOT. This is particularly useful for handling user-uploaded content, such as images or documents, during development.'''