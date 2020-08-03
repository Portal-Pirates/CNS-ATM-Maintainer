from django.conf.urls import url
from django.urls import path
from .views import homepage
from . import views

urlpatterns = [
    path('', homepage, name="homepage"),
    path('qrredirect',views.redirect_to_scan_qr,name="qrredirect"),
    path('show',views.show_data,name="show"),
    path('daily/',views.dig_models_daily_reports,name="daily"),
    path('monthly',views.dig_models_monthly_reports,name="monthly"),
    path('weekly/',views.dig_models_weekly_reports,name="weekly"),
    #path('quaterly',views.dig_models_quaterly_reports,name ="quaterly"),
    path('<created>/',views.detail_daily_report,name = "details"),
    path('weekly/<created>/',views.detail_weekly_report,name = "detailsweekly"),
    #path('sixmonth',views.dig_models_six_month_reports,name="sixmonth"),
    path('yearly',views.dig_models_yearly_reports,name="yearly"),
    path('search',views.search_in_action,name="search"),
    path('fault',views.fault_table_entry_and_prediction,name="fault"),
]
