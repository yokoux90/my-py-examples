from typing import Annotated

from fastapi import APIRouter, Body, HTTPException


from entity.stock_industry import StockIndustry
from service.stock_industry import StockIndustryService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Stock Industry"])

srv = StockIndustryService()


@router.post("/stock_industry")
def stock_industry() -> list[StockIndustry]:
    try:
        res = srv.query_stock_industry()
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
