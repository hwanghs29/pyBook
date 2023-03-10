from django.urls import path
from . import views
#
app_name = 'polls'
urlpatterns = [
     # path(r'^polls/$', views.index, name='index'),
     # path(r'^polls/?P<question_id>\d+)$', views.detail, name='detail'),
     # path(r'^polls/?P<question_id>\d+)/vote/$', views.vote, name='vote'),
     # path(r'^polls/?P<question_id>\d+)/results/$', views.results, name='results'),

    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

