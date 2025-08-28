from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_balance_data import ReqBalanceData
from entity.balance_data import BalanceData
from service.balance_data import BalanceDataService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Balance Data"])

srv = BalanceDataService()


@router.post("/balance_data")
def balance_data(req: Annotated[ReqBalanceData, Body(
    example={
        "code": "sh.600000",
        "year": 2018,
        "quarter": 2
    }
)]) -> list[BalanceData]:
    try:
        res = srv.query_balance_data(req.code, req.year, req.quarter)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
