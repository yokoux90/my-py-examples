from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_required_reserve_ratio_data import ReqRequiredReserveRatioData
from entity.required_reserve_ratio_data import RequiredReserveRatioData
from service.required_reserve_ratio_data import RequiredReserveRatioDataService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Required Reserve Ratio Data"])

srv = RequiredReserveRatioDataService()


@router.post("/required_reserve_ratio_data")
def required_reserve_ratio_data(req: Annotated[ReqRequiredReserveRatioData, Body(
    example={
        "start_date": "2015-01-01",
        "end_date": "2017-12-31",
        "year_type": "0"
    }
)]) -> list[RequiredReserveRatioData]:
    try:
        res = srv.query_required_reserve_ratio_data(
            start=req.start_date, end=req.end_date, yt=req.year_type)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
