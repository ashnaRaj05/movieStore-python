from django.urls import path
from . import views
app_name= 'movieapp'
urlpatterns = [
    path("home/", views.usblog, name='home'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('genres/<int:cat_id>/', views.genre_detail, name='genre_detail'),
    path('add/', views.snippet_detail, name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('addreview/<int:id>/',views.add_review,name="add_review"),
    path('editreview/<int:movie_id>/<int:review_id>',views.edit_review,name="edit_review"),
    path('deletereview/<int:movie_id>/<int:review_id>',views.delete_review,name="delete_review"),

]
