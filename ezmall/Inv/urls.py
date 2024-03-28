from django.urls import path
from .import views

urlpatterns =[
    path('', views.dashboard,name='Home'),
    path('courses/', views.Courses,name='Courses'),
    path('student/<str:pk_test>/',views.Student,name='Student'),
    path('', views.index),
    path('add/', views.add_person),
    path('<path:remaining_url>/', views.catch_all_view),
    path('Inv/',views.index, name="Inv"),
    path('show/',views.get_all_person)
]
