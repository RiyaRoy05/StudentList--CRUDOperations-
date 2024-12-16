from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path('',views.index,name="index"),
    path('second',views.second),

    path('Contact',views.contact),
    path('handleC',views.hContact),

    path('update/<int:id>',views.updateS),
    path('hUpdate/<int:id>',views.hsUp),

    path('hDel/<int:id>',views.hdel),

    path('Details/<int:id>',views.detail),
]
