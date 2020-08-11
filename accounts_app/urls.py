app_name = 'accounts_app'

from django.urls import path
from accounts_app.views import login_view


urlpatterns = [
    path('login/', login_view, name='login'),
]