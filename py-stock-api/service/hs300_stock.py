import baostock as bs
import pandas as pd

from entity.hs300_stock import HS300Stock
from utilities.query_exception import QueryException


class HS300StockService:

    @classmethod
    def query_hs300_stocks(cls) -> list[HS300Stock]:
        rs = bs.query_hs300_stocks()
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[HS300Stock] = []
        for j in js:
            ks.append(HS300Stock(**j))
        return ks
