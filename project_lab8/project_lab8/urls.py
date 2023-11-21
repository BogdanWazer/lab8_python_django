from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lab8_app.urls')),  # змініть 'supply_department' на фактичну назву вашого додатку
]