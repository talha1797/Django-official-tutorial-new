from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:question_id>/add_choice",views.add_choice, name="add_choice"),
    path("<int:question_id>/added", views.adding_user_choice, name="adding_user_choice"),
    path("/add_Question",views.add_question, name="add_Question"),
    path("/adding_user_question",views.adding_user_question, name="adding_user_question"),
    path("<int:question_id>/edit_question",views.edit_question, name="edit_question"),
    path("<int:question_id>/user_edit_question",views.user_edit_question, name="user_edit_question")
    
] 
