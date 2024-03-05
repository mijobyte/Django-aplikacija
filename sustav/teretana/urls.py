from django.urls import path
from . import views
from teretana.views import *

app_name = 'teretana'  # here for namespacing of urls.

urlpatterns = [
    path('',views.Home, name="Home"),
    path('signup',views.signup,name="singup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('enroll',views.enroll,name="enroll"),
    path('dashboard',views.Dashboard,name="dashboard"),
    path('adminhome',views.AdminHome,name="adminhome"),
    path('user_list',UsersListView.as_view(), name='user_list'),
    path('addnewuser',views.UsersCreateView.as_view(), name='add_user'),  
    path('updateuser/<int:pk>', views.UsersUpdateView.as_view(), name='update_user'),  
    path('deleteuser/<int:id>', views.destroyuser, name='delete_user'),
    path('plan_list',PlanList.as_view(), name='plan_list'),
    path('addnewplan',views.PlanCreateView.as_view(), name='add_plan'),  
    path('updateplan/<int:pk>', views.PlanUpdateView.as_view(), name='update_plan'),  
    path('deleteplan/<int:id>', views.destroyplan, name='delete_plan'),
    path('trener_list',TrenerList.as_view(), name='trener_list'),
    path('addnewtrener',views.TrenerCreateView.as_view(), name='add_trener'),  
    path('updatetrener/<int:pk>', views.TrenerUpdateView.as_view(), name='update_trener'),  
    path('deletetrener/<int:id>', views.destroytrener, name='delete_plan'),
    path('pretplatnik_list',PretplatnikList.as_view(), name='pretplatnik_list'),
    path('addnewpretplatnik',views.PretplatnikCreateView.as_view(), name='add_pretplatnik'),  
    path('updatepretplatnik/<int:pk>', views.PretplatnikUpdateView.as_view(), name='update_pretplatnik'),  
    path('deletepretplatnik/<int:id>', views.destroypretplatnik, name='delete_pretplatnik'),
    path('oznaka_list',OznakaList.as_view(), name='oznaka_list'),
    path('addnewoznaka',views.OznakaCreateView.as_view(), name='add_oznaka'),  
    path('updateoznaka/<int:pk>', views.OznakaUpdateView.as_view(), name='update_oznaka'),  
    path('deleteoznaka/<int:id>', views.destroyoznaka, name='delete_oznaka'),
]