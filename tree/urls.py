from . import views
from django.urls import path


urlpatterns = [
    path('', views.treeMakingFirstInsertion, name='index'),
    path('allTrees',views.allTrees,name="alltreeView"),
    path('deleteTree',views.deleteTree,name="deleteTreeView"),
    path('treeElementInsertion',views.treeElementInsertion,name="treeElementInsertion"),
    path('treeMakingFirstInsertion',views.treeMakingFirstInsertion,name="treeMakingFirstInsertion"),

]