from django.urls import path
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_billsent.urls'))

]