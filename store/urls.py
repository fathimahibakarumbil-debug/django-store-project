# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.login_view, name='login'),      
#     path('register/', views.register_view, name='register'),
#     path('logout/', views.logout_view, name='logout'),
#     path('', views.home, name='home'),
#     path('products/', views.product_list, name='product_list'),
#     path('saved/', views.saved_products, name='saved_products'),  
#     path('add/', views.add_product, name='add_product'),
#     path('edit/<int:pk>/', views.edit_product, name='edit_product'),
#     path('delete/<int:pk>/', views.delete_product, name='delete_product'),
#     path('remove-saved/<int:pk>/', views.remove_saved_product, name='remove_saved_product'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),

# ]



from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('saved/', views.saved_products, name='saved_products'),

    path('add/', views.add_product, name='add_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('remove-saved/<int:pk>/', views.remove_saved_product, name='remove_saved_product'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]