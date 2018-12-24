from yahoo_fin.stock_info import *
import datetime as dt
import quandl
stock = 'qqq'
week_ago = '01/01/2017'
today = dt.date.today().strftime('%m-%d-%Y')
data = get_data(stock, start_date=week_ago, end_date=today, index_as_date=True)


quandl.ApiConfig.api_key = 'fLUd1xbG8hjz3vMutU_s'
today = dt.date.today().strftime('%m-%d-%Y')
week_ago = (dt.date.today() - dt.timedelta(days=7)).strftime('%m-%d-%Y')
checker = quandl.get_table('WIKI/PRICES', ticker=stock,
                        qopts={'columns': ['date', 'ticker', 'adj_close']},
                        date={'gte': '2016-1-1', 'lte': dt.datetime.today().strftime('%Y-%m-%d')},
                        paginate=True)



print(checker)