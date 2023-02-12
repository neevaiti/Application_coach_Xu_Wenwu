from django.contrib import admin
from django.urls import path, include
from coach_Xu_Wenwu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coach_Xu_Wenwu.urls'))
]
