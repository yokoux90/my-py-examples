from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_cash_flow_data import ReqCashFlowData
from entity.cash_flow_data import CashFlowData
from service.cash_flow_data import CashFlowDataService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Cash Flow Data"])

srv = CashFlowDataService()


@router.post("/cash_flow_data")
def cash_flow_data(req: Annotated[ReqCashFlowData, Body(
    example={
        "code": "sh.600000",
        "year": 2018,
        "quarter": 2
    }
)]) -> list[CashFlowData]:
    try:
        res = srv.query_cash_flow_data(req.code, req.year, req.quarter)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
