from django.urls import path

from . import views

app_name = 'notetaker'
urlpatterns = [
    path('', views.index, name='index'),
    path('note/<int:pk>/', views.NoteView.as_view(), name='note_details'),
    path('doneTodo/<int:todo_id>/', views.doneTodo),
    path('addNote/', views.addNote),
    path('deleteNote/<int:note_id>/', views.deleteNote),
    path('updateTodo/<int:todo_id>/', views.updateTodo, name='update_todo'),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo),
    path('addTodo/', views.addTodo),
]