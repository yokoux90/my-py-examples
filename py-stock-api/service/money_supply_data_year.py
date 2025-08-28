import baostock as bs
import pandas as pd

from entity.money_supply_data_year import MoneySupplyDataYear
from utilities.query_exception import QueryException


class MoneySupplyDataYearService:

    @classmethod
    def query_money_supply_data_year(cls, start: str, end: str) -> list[MoneySupplyDataYear]:
        rs = bs.query_money_supply_data_year(
            start_date=start,
            end_date=end
        )
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[MoneySupplyDataYear] = []
        for j in js:
            ks.append(MoneySupplyDataYear(**j))
        return ks
