
# from django.contrib import admin
# from django.urls import path
# from app.views import register_page , login_page

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('register/', register_page , name='register_page'),
#     path('login/', login_page , name='login_page'),
# ]



from django.contrib import admin
from django.urls import path
from app.views import register_page , logout_page , home , login_page , detail_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('register/',register_page, name='register_page'),
    path('login/',login_page , name='login_page'),
    path('logout/',logout_page , name='logout_page'),
   
    path('detail_page/<int:id>',detail_page , name='detail_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
