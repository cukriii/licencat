app_name = "plots_graphs_app"
from plots_graphs import views
from django.urls import path


urlpatterns = [
    #path('plts/', product_plot_view, name='product_plot_view'),
    path('/showimage/', views.plot_make_view(), name='showimage'),
]