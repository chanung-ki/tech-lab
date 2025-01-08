from django.urls import path
from .apis import get_user_detail

urlpatterns = [
    path('<id>', get_user_detail, name='get_user_detail'),
]