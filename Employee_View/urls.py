from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home_page,name="Home_Page"),
    path('Add',views.Add_Page,name="Add_Page"),
    path('Remove',views.Remove_Page,name="Remove_Page"),
    path('Filter',views.Filter_Page,name="Filter_Page"),
    path('All',views.All_Page,name="All_Page"),

]