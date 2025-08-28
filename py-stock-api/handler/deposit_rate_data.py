from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_deposit_rate_data import ReqDepositRateData
from entity.deposit_rate_data import DepositRateData
from service.deposit_rate_data import DepositRateDataService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Deposit Rate Data"])

srv = DepositRateDataService()


@router.post("/deposit_rate_data")
def deposit_rate_data(req: Annotated[ReqDepositRateData, Body(
    example={
        "start": "2015-01-01",
        "end": "2017-12-31"
    }
)]) -> list[DepositRateData]:
    try:
        res = srv.query_deposit_rate_data(req.start, req.end)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
