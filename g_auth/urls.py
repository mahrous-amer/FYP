"""g_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emojiauth import views
from DragPIN import views as vs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='index'),
    path('sign_in/',views.sign_in, name='login'),
    path('emoji/',views.sign_up, name='register'),
    path('DragPIN/',vs.Drag_up, name='Drag_up'),
    path('DragPIN_in/',vs.Drag_in, name='Drag_in'),
    path('EmojiDrag/',views.sign_upp, name='EmojiDrag'),
    path('FeedBack/', views.feedback, name='feedback'),
    path('Auth', views.validate, name='validate'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
