"""untitled3 URL Configuration

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
from django.shortcuts import  HttpResponse
from django.shortcuts import HttpResponse,render
from app01 import views
from django.conf import settings
from django.conf.urls.static import static
def index_view(request):

    return render(request , 'log.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', index_view),
    path('login/', views.login),
    path('login/reglink/', views.reglink),
    path('gggg/',views.yanzheng),
    path('login/gggg/', views.yanzheng),
    path('son/', views.son),
    path('me/', views.me),
    path('xiugai/', views.xiugai),
    path('logout/', views.logout),
    path('file/', views.file1),
    path('gggg/',views.yanzheng),
    path('fabu/',views.fabu),
    path('neirong/',views.neirong),
    path('zixun/',views.zixun),
    path('tupian/',views.tupian),
    path('del/',views.dels),
    path('editor/',views.editor),
    path('select/',views.select),
    path('abc/',views.abc),
    path('newlogin/',views.newlogin),
    path('see/',views.see),
    path('look/',views.look),
    path('see2/',views.see2),
    path('to_chat/',views.to_chat),
    path('chat/',views.chat),
    path('test/',views.test),
    path('msg_send/', views.msg_send),
    path('index/',views.index)



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

