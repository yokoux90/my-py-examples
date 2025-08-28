import baostock as bs
import pandas as pd

from entity.operation_data import OperationData
from utilities.query_exception import QueryException

class OperationDataService:

    @classmethod
    def query_operation_data(cls, code: str, year: int, quarter: int) -> list[OperationData]:
        rs = bs.query_operation_data(
            code=code,
            year=year,
            quarter=quarter
        )
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[OperationData] = []
        for j in js:
            ks.append(OperationData(**j))
        return ks