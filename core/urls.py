from django.conf.urls import url
from django.urls import path
from .views import homepage
from . import views

urlpatterns = [
    path('', homepage, name="homepage"),
    path('qrredirect',views.redirect_to_scan_qr,name="qrredirect"),
    path('scan',views.video_feed,name="scan"),
    path('daily/',views.dig_models_daily_reports,name="daily"),
    path('monthly',views.dig_models_monthly_reports,name="monthly"),
    path('weekly',views.dig_models_weekly_reports,name="weekly"),
    path('quaterly',views.dig_models_quaterly_reports,name ="quaterly"),
    path('<slug>/',views.detail_daily_report,name = "details"),
    path('sixmonth',views.dig_models_six_month_reports,name="sixmonth"),
    path('yearly',views.dig_models_six_month_reports,name="yearly"),

]
