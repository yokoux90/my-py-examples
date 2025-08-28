from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_dividend_data import ReqDividendData
from entity.dividend_data import DividendData
from service.dividend_data import DividendDataService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Dividend Data"])

srv = DividendDataService()


@router.post("/dividend_data")
def dividend_data(req: Annotated[ReqDividendData, Body(
    example={
        "code": "sh.600000",
        "year": "2018",
        "yearType": "report"
    }
)]) -> list[DividendData]:
    try:
        res = srv.query_dividend_data(req.code, req.year, req.yearType)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
