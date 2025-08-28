from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_growth_data import ReqGrowthData
from entity.growth_data import GrowthData
from service.growth_data import GrowthDataService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Growth Data"])

srv = GrowthDataService()


@router.post("/growth_data")
def growth_data(req: Annotated[ReqGrowthData, Body(
    example={
        "code": "sh.600000",
        "year": 2018,
        "quarter": 2
    }
)]) -> list[GrowthData]:
    try:
        res = srv.query_growth_data(req.code, req.year, req.quarter)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
