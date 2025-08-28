import baostock as bs
import pandas as pd

from entity.stock_basic import StockBasic
from utilities.query_exception import QueryException


class StockBasicService:

    @classmethod
    def query_stock_basic(cls, code: str) -> list[StockBasic]:
        rs = bs.query_stock_basic(code=code)
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[StockBasic] = []
        for j in js:
            ks.append(StockBasic(**j))
        return ks
