from django.contrib import admin
from django.urls import path,include
from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = "home"),
    path('create/',views.create,name = "create"),
    path("edit/<int:id>/",views.edit,name = "edit"),
    path("delete/<int:id>/",views.delete,name = "delete"),
    path("accounts/",include("django.contrib.auth.urls")),
]



