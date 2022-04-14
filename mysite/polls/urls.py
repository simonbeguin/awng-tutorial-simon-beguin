from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('form', views.get_name, name='form'),
    path('thanks', views.print_thanks, name = 'thanks'),
    path('base', views.print_base, name = 'base'),
    path('basechild', views.print_base_child, name = 'base_child'),
]
