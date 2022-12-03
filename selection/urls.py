from django.urls import path

from selection import views


urlpatterns = [
   path('', views.SelectionListView.as_view(), name='selections'),
   # path("<int:pk>/update/", views.UserUpdateView.as_view(), name="update_user"),
   # path("<int:pk>/delete/", views.UserDeleteView.as_view(), name="delete_user"),
   path('<int:pk>/', views.SelectionDetailView.as_view(), name='detail_selection'),
   path('create/', views.SelectionCreateView.as_view(), name='create_selection'),
   # path('token/', TokenObtainPairView.as_view(), name='get_user_token'),
   # path('token/refresh/', TokenRefreshView.as_view(), name='refresh_user_token'),
]