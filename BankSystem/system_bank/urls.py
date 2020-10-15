from django.urls import path, include
from system_bank import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Bank', views.BankViewSet)
router.register(r'Customer', views.CustomerViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('', views.bank_list),
    path('', views.bank_detail),
    path('', views.customer_list),
    path('', views.customer_detail),   
]


