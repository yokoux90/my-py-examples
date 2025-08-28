import baostock as bs
import pandas as pd

from entity.sz50_stock import SZ50Stock
from utilities.query_exception import QueryException


class SZ50StockService:

    @classmethod
    def query_sz50_stocks(cls) -> list[SZ50Stock]:
        rs = bs.query_sz50_stocks()
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[SZ50Stock] = []
        for j in js:
            ks.append(SZ50Stock(**j))
        return ks
