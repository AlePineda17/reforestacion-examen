from django.urls import path
from fincas import views


app_name = 'fincas'

urlpatterns = [
    path('index/<int:user_id>', views.index, name='index'),
    path('create_property/<int:user_id>', views.create_property, name='create_property'),
    path('edit_property/<int:user_id>', views.edit_property, name='edit_property'),
    path('delete_property/<int:user_id>', views.delete_property, name='delete_property'),
    path('create_plot/<int:user_id>/<int:property_id>', views.create_plot, name='create_plot'),
    path('property_plots/<int:user_id>/<int:property_id>', views.property_plots, name='property_plots'),
    path('edit_plot/<int:user_id>/<int:plot_id>', views.edit_plot, name='edit_plot'),
    path('delete_plot/<int:user_id>/<int:plot_id>', views.delete_plot, name='delete_plot'),
    path('create_tree/<int:user_id>/<int:property_id>/<int:plot_id>', views.create_tree, name='create_tree'),
    path('plot_trees/<int:user_id>/<int:property_id>/<int:plot_id>', views.plot_trees, name='plot_trees'),
    path('edit_tree/<int:user_id>/<int:property_id>/<int:tree_id>', views.edit_tree, name='edit_tree'),
    path('delete_tree/<int:user_id>/<int:property_id>/<int:plot_id>', views.delete_tree, name='delete_tree'),
]
