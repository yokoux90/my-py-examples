import datetime

from pandas.errors import InvalidIndexError

from constant.adjust_flag import AdjustFlag
from constant.trade_status import TradeStatus


def parse_date(dt:str) -> datetime.date:
    fmt: str = "%Y-%m-%d"
    parsed = datetime.datetime.strptime(dt, fmt).date()
    return parsed

def parse_datetime(dt:str) -> datetime.datetime:
    fmt: str = "%Y%m%d%H%M%S%f"
    parsed = datetime.datetime.strptime(dt, fmt)
    return parsed

def parse_adjust_flag(idx: int) -> AdjustFlag:
    match idx:
        case 1:
            return AdjustFlag.BackwardAdjustment
        case 2:
            return AdjustFlag.ForwardAdjustment
        case 3:
            return AdjustFlag.NoAdjustment
        case _:
            raise InvalidIndexError()

def parse_trade_status(idx: int) -> TradeStatus:
    match idx:
        case 0:
            return TradeStatus.Normal
        case 1:
            return TradeStatus.Suspend
        case _:
            raise InvalidIndexError()