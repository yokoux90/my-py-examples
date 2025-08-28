import baostock as bs
import pandas as pd

from entity.zz500_stock import ZZ500Stock
from utilities.query_exception import QueryException


class ZZ500StockService:

    @classmethod
    def query_zz500_stocks(cls) -> list[ZZ500Stock]:
        rs = bs.query_zz500_stocks()
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[ZZ500Stock] = []
        for j in js:
            ks.append(ZZ500Stock(**j))
        return ks
