from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]



path('cart/', views.cart_view, name='cart'),
path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),


from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('signup/', views.signup_view, name='signup'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('signup/', views.signup_view, name='signup'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # ✅ this ensures 'login' is included
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
