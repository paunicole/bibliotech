from django.urls import path
from .views import employee_views


urlpatterns = [
    path("employee/new", employee_views.employee_create, name="employee-create"),
    path("employee-list", employee_views.employee_list, name="employee-list"),
    path(
        "employee/update/<str:employee_id>",
        employee_views.employee_update,
        name="employee-update",
    ),
]
