
from django.contrib import admin
from django.urls import path
from drogueria.views import (AltaMedicamento, BuscarMedicamento)


#from blog.views import index as blog_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alta/', AltaMedicamento.as_view()),
    path('buscar', BuscarMedicamento.as_view()),

]
