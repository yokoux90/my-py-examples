from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_money_supply_data_month import ReqMoneySupplyDataMonth
from entity.money_supply_data_month import MoneySupplyDataMonth
from service.money_supply_data_month import MoneySupplyDataMonthService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Money Supply Data Month"])

srv = MoneySupplyDataMonthService()


@router.post("/money_supply_data_month")
def money_supply_data_month(req: Annotated[ReqMoneySupplyDataMonth, Body(
    example={
        "start_date": "2015-01-01",
        "end_date": "2017-12-31"
    }
)]) -> list[MoneySupplyDataMonth]:
    try:
        res = srv.query_money_supply_data_month(req.start_date, req.end_date)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
