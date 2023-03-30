
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
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('h/', views.hellow, name='HellowTest'),
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('add/', views.pollcreateform, name='createmodelform'),
    path('add1/', views.pollcreateform, name='add1'),
    path('add2/', views.PollCreateView.as_view(), name='add2')

]
