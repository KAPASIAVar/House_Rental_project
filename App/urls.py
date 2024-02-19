"""
URL configuration for App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from member import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('',views.Login,name='login'),
    path('home/',views.home,name='home'),
    path('houses/',views.houses,name='houses'),
    path('add_house/',views.add_house,name='add_house'),
    path('tenant/',views.Tenant,name='tenant'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('add_tenent/',views.add_tenent,name='add_tenent'),
    path('tenant_details/<int:Id>/',views.Tenant_details,name='tenant_details'),
    path('tenant_payment/<int:Id>/<str:name>/',views.Tenant_payment,name='tenant_payment'),
    path('payment_page/',views.Payment_page,name='payment_page'),
    path('add_payment/',views.add_payment,name='add_payment'),
    path('house_tenant/<str:Id>/',views.house_tenant,name='house_tenant'),
    path('checkout/<int:Id>/<str:name>/',views.checkout,name='checkout'),
    path('old_records/',views.old_records,name='old_records'),
    path('old_record_data/<int:Id>/',views.old_record_data,name='old_record_data'),
    path('Old_payment/<int:Id>/',views.old_payment,name='Old_payment'),
    path('Dues/',views.Dues,name='Dues'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)