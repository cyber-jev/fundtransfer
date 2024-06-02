from django.urls import path
from .views import CreateUserView, FundUserView, ListUsersView


urlpatterns = [
    path("users/create/", CreateUserView.as_view(), name="create-user"),
    path("users/fund/", FundUserView.as_view(), name="fund-user"),
    path("users/list/", ListUsersView.as_view(), name="list-users"),
]
