from django.urls import path
from .views import HomeBackGroudListView ,KayqimasinListView,blogListView,flightsListView,staysListView,LOGINListView,IndexDetalView,register_request,login_request,logout_request,homegroudDetal,ApranqnerDetal

urlpatterns = [
    path('',HomeBackGroudListView.as_view(),name = 'home2'),
    path('<int:id>/', IndexDetalView.as_view(), name='index_detail'),
    path('home2/<int:id>/',homegroudDetal.as_view(),name='gr_detal'),
    path('/<int:id>/',ApranqnerDetal.as_view(),name='apranq_detal'),
    path('aboutus/',KayqimasinListView.as_view(),name='aboutus'),
    path('blog/',blogListView.as_view(),name='blog'),
    path('flights/',flightsListView.as_view(),name ='flights'),
    path('stays/',staysListView.as_view(),name='stays'),
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name = 'logout'),
    path('login/',LOGINListView.as_view(),name='login')

]