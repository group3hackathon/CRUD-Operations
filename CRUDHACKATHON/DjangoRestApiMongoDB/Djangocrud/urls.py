
from Djangocrud import views

from django.urls import include, re_path



urlpatterns=[
    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/[0-9]+$',views.departmentApi),

    re_path(r'^employee$',views.EmployeeApi),
    re_path(r'^employee/[0-9]+$',views.EmployeeApi),
]