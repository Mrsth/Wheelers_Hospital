from django.urls.resolvers import URLPattern
from .views import RegisterAPI, LoginAPI, BikeViewset, ServiceRequestFormViewset, BlogViewSet, OurServicesViewset, ChangePasswordView, SendOTPV
from django.urls import path

urlpatterns = [
    path('login', LoginAPI.as_view(), name='login'),
    path('register', RegisterAPI.as_view(), name='register'),
    path('bike', BikeViewset.as_view(), name="bike"),
    path('bike/<int:pk>', BikeViewset.as_view(), name="bikepk"),
    path('service', ServiceRequestFormViewset.as_view(), name='service'),
    path('service/<int:pk>', ServiceRequestFormViewset.as_view(), name='service'),
    path('blog', BlogViewSet.as_view(), name='blog'),
    path('blog/<int:pk>', BikeViewset.as_view()),
    path('ourservices', OurServicesViewset.as_view()),
    path('change_password/<int:pk>', ChangePasswordView.as_view(), name='change_password'),
    # path('otp', SendOTP),
    path('otp/<int:pk>/<int:code>', SendOTPV.as_view()),
    # path('otp/<int:pk>', SendOTPV.as_view()),
    # path('otp/<int:pk>/<int:code>', postOTP.as_view()),
    # path('gpr', getPhoneNumberRegistered.as_view()),
    # path('change_password', ChangePasswordView.as_view(), name='change_password'),
]    