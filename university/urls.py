from django.urls import path
from .views import *

urlpatterns = [

    path('', about_us, name='about_us'),
    path('blog/', blog, name='blog'),
    path('organization/', organizations, name='organizations'),
    path('contact_us/', contact_us, name='contact_us'),
    path('login/', logins, name='login'),
    path('member/', member, name='member'),
    path('create/', create, name='create'),
    path('update/', update, name='update'),

    path('sign_up/', registerPage, name='sign_up'),
    path('sign_in/', loginPage, name='sign_in'),
    path('log_out/', logoutPage, name='log_out'),


    path('<int:pk>', NewsDetailView.as_view(), name='DetailView'),
    path('<int:pk>/update', UpdateView.as_view(), name='UpdateView'),
    path('<int:pk>/delete', DeleteView.as_view(), name='DeleteView')


]