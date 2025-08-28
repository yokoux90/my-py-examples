import baostock as bs
import pandas as pd

from entity.k_daily import KDaily
from entity.k_minute import KMinute
from entity.k_week_month import KWeekMonth
from utilities.query_exception import QueryException


class KHistoryService:

    @classmethod
    def query_history_k_minute(cls, code: str, start: str, end: str, frequency: str, adjust_flag: str) -> list[KMinute]:
        rs = bs.query_history_k_data_plus(
            code=code,
            fields="date,time,code,open,high,low,close,volume,amount,adjustflag",
            start_date=start,
            end_date=end,
            frequency=frequency,
            adjustflag=adjust_flag
        )
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[KMinute] = []
        for j in js:
            ks.append(KMinute(**j))
        return ks

    @classmethod
    def query_history_k_day(cls, code: str, start: str, end: str, adjust_flag: str) -> list[KDaily]:
        rs = bs.query_history_k_data_plus(
            code=code,
            fields="date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST",
            start_date=start,
            end_date=end,
            frequency="d",
            adjustflag=adjust_flag
        )
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[KDaily] = []
        for j in js:
            ks.append(KDaily(**j))
        return ks

    @classmethod
    def query_history_k_week(cls, code: str, start: str, end: str, adjust_flag: str) -> list[KWeekMonth]:
        rs = bs.query_history_k_data_plus(
            code=code,
            fields="date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
            start_date=start,
            end_date=end,
            frequency="w",
            adjustflag=adjust_flag
        )
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[KWeekMonth] = []
        for j in js:
            ks.append(KWeekMonth(**j))
        return ks

    @classmethod
    def query_history_k_month(cls, code: str, start: str, end: str, adjust_flag: str) -> list[KWeekMonth]:
        rs = bs.query_history_k_data_plus(
            code=code,
            fields="date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
            start_date=start,
            end_date=end,
            frequency="m",
            adjustflag=adjust_flag
        )
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[KWeekMonth] = []
        for j in js:
            ks.append(KWeekMonth(**j))
        return ks