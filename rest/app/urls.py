from django.urls import path
from .views import studentlist , studentdetails , studentupdate , studentcreate ,studentdelete


urlpatterns = [
    path("", studentlist, name="list"),
    path("details/<int:id>/",studentdetails,name="details"),
    path("update/<int:id>/", studentupdate, name="update"),
    path("delete/<int:id>/", studentdelete, name="update"),
    path("create/", studentcreate, name="create")
]