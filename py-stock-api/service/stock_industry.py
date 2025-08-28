import baostock as bs
import pandas as pd

from entity.stock_industry import StockIndustry
from utilities.query_exception import QueryException


class StockIndustryService:

    @classmethod
    def query_stock_industry(cls) -> list[StockIndustry]:
        rs = bs.query_stock_industry()
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[StockIndustry] = []
        for j in js:
            ks.append(StockIndustry(**j))
        return ks
