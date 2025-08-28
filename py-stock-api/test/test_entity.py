import datetime
import json

import baostock as bs
from pandas.errors import InvalidIndexError

from rich.pretty import pprint
import pandas as pd

from constant.adjust_flag import AdjustFlag
from entity.k_minute import KMinute


def test_login():
    lg = bs.login()
    print(lg.error_code)
    print(lg.error_msg)

def test_a_k():
    lg = bs.login()
    print(lg.error_code)
    print(lg.error_msg)

    rs = bs.query_history_k_data_plus("sh.600000",
                                      "date,time,code,open,high,low,close,volume,amount,adjustflag",
                                      start_date='2024-07-01', end_date='2024-07-02',
                                      frequency="15", adjustflag="3")
    print('query_history_k_data_plus respond error_code:' + rs.error_code)
    print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    js = result.to_dict(orient='records')
    # pprint(js)
    ks = []
    for j in js:
        print(j)
       # ks.append(KMinute(**j))
    pprint(ks)


def test_dt():
    t = "20240701100000000"
    pprint(datetime.datetime.strptime(t, "%Y%m%d%H%M%S%f"))

def test_parse_k_minute():
    obj = {'date': '2024-07-01', 'time': '20240701100000000', 'code': 'sh.600000', 'open': '8.2200', 'high': '8.2600', 'low': '8.2100', 'close': '8.2500', 'volume': '4708600', 'amount': '38809648.0000', 'adjustflag': '3'}
    k = KMinute(**obj)
    pprint(k)
    pprint(k.to_json())
