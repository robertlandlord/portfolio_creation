
from . import views
from personal import views as personal_views
from django.urls import re_path


urlpatterns = [
    re_path(r'^$',  personal_views.index, name='index'),
    re_path(r'^addstock/$', views.AddStockFormView.as_view(), name='add_stock'), #url for addstock, put it with portfolio stuff
    re_path(r'^findstock/$', views.FindStockFormView.as_view(), name='find_stock'), #url for findstock
    re_path(r'^getstockinfo/$', views.GetStockInfoFormView.as_view(), name='get_stock_info'), #url for get stock info
    re_path(r'^liquidate/$',views.LiquidateFormView.as_view(),name='liquidate'), #liquidating portfolio
    re_path(r'^api/chart/data/returns/$', views.ReturnChartData.as_view(), name='api-chart-data-returns'), #below are all info-sending JSON apis
    re_path(r'^api/chart/data/markowitz/$', views.MarkowitzChartData.as_view(), name='api-chart-data-markowitz'),
    re_path(r'^api/chart/data/returntable/$', views.ReturnTableData.as_view(), name='api-return-data'),
    re_path(r'^api/chart/data/returnrank/$', views.ReturnRankingData.as_view(), name='api-return-data'),
    re_path(r'^api/chart/data/earnings/$', views.EarnerRankingData.as_view(), name='api-earnings-data'),
    ]
