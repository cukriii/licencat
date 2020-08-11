app_name = 'pages_app'

from django.urls import path
from pages_app.views import plots_page_view
from pages_app.views import home_view

urlpatterns = [
    path('plots/', plots_page_view, name='plots'),
    path('home/', home_view, name='home'),
    path('upload_files', upload_files, name= 'upload )
]