import datetime
from typing import Annotated

from pydantic import BaseModel, Field, BeforeValidator

from .validators import parse_datetime, parse_date


class KMinute(BaseModel):
    code: str = Field(..., title="证券代码", description="格式: sh.600000。sh: 上海，sz: 深圳")
    date: Annotated[datetime.date, BeforeValidator(parse_date)] = Field(..., title="交易所行情日期", description="格式: YYYY-MM-DD")
    time: Annotated[datetime.datetime, BeforeValidator(parse_datetime)] = Field(..., title="交易所行情时间", description="格式: YYYYMMDDHHMMSSsss")
    open: float = Field(..., title="今开盘价格", description="精度: 小数点后4位; 单位: 人民币元")
    high: float = Field(..., title="最高价", description="精度: 小数点后4位; 单位: 人民币元")
    low: float = Field(..., title="最低价", description="精度: 小数点后4位; 单位: 人民币元")
    close: float = Field(..., title="今收盘价", description="精度: 小数点后4位; 单位: 人民币元")
    volume: int = Field(default=0, title="成交数量", description="单位: 股")
    amount: float = Field(..., title="成交金额", description="精度: 小数点后4位; 单位: 人民币元")
    adjustFlag: int = Field(default=3, alias="adjustflag", title="复权状态", description="1: 后复权、2: 前复权、3: 不复权")


    def to_json(self) -> dict:
        return {
            "code": self.code,
            "date": self.date.strftime("%Y-%m-%d"),
            "time": self.time.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "open": f"{self.open:.4f}",
            "high": f"{self.high:.4f}",
            "low": f"{self.low:.4f}",
            "close": f"{self.close:.4f}",
            "volume": self.volume,
            "amount": f"{self.amount:.4f}",
            "adjust_flag": self.adjustFlag.value
        }