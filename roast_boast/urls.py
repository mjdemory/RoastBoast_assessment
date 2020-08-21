"""roast_boast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from homepage.views import index, create_post_view, boast_view, roast_view, upvote_view, downvote_view, sortbyvote_view

urlpatterns = [
    path('', index, name="homepage"),
    path('create_post_view/', create_post_view, name="create_post"),
    path('boast_view/', boast_view, name="boast"),
    path('roast_view/', roast_view, name="roast"),
    path('upvote_view/<int:upvote_id>/', upvote_view, name="upvote"),
    path('downvote_view/<int:downvote_id>/', downvote_view, name="downvote"),
    path('sortbyvote_view/', sortbyvote_view, name="sortbyvote"),
    # path('delete_post_view<str:')
    path('admin/', admin.site.urls),
]
