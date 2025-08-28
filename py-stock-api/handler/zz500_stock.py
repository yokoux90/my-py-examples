from typing import Annotated

from fastapi import APIRouter, Body, HTTPException


from entity.zz500_stock import ZZ500Stock
from service.zz500_stock import ZZ500StockService
from utilities.query_exception import QueryException

router = APIRouter(tags=["ZZ500 Stock"])

srv = ZZ500StockService()


@router.post("/zz500_stock")
def zz500_stock() -> list[ZZ500Stock]:
    try:
        res = srv.query_zz500_stocks()
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
