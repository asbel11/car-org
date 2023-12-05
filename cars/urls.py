from django.urls import path
from .views import CarsUpdateView,CarsCreateView,CarsDetailView,CarsDeleteView,HomePageView,AboutPageView,ShopPageView,CarsPageView

urlpatterns = [
path("", HomePageView.as_view(), name="home"),
path("cars", CarsPageView.as_view(), name="cars"),
path("about",AboutPageView.as_view(),name="about"),
path("shop",ShopPageView.as_view(),name="shop"),
path("post/new/", CarsCreateView.as_view(), name="post_new"),
path("post/<int:pk>/", CarsDetailView.as_view(), name="post_detail"),
path("post/<int:pk>/delete/", CarsDeleteView.as_view(), name="post_delete"),
path("post/<int:pk>/edit/", CarsUpdateView.as_view(), name="post_edit"),
]


