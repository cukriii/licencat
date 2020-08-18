app_name = 'pages_app'

from django.urls import path
from pages_app.views import plots_page_view, home_view, plots

urlpatterns = [
    path('plots/', plots_page_view, name='plots'),
    path('plots/<id>/', plots, name='ploter'),
    path('home/', home_view, name='home'),
]