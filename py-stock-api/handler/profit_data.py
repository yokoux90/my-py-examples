from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_profit_data import ReqProfitData
from entity.profit_data import ProfitData
from service.profit_data import ProfitDataService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Profit Data"])

srv = ProfitDataService()


@router.post("/profit_data")
def profit_data(req: Annotated[ReqProfitData, Body(
    example={
        "code": "sh.600000",
        "year": 2018,
        "quarter": 2
    }
)]) -> list[ProfitData]:
    try:
        res = srv.query_profit_data(req.code, req.year, req.quarter)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
