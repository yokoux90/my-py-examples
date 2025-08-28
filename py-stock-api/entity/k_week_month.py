import datetime
from typing import Annotated

from pydantic import BaseModel, Field, BeforeValidator

from .validators import parse_date


class KWeekMonth(BaseModel):
    code: str = Field(..., title="证券代码", description="格式: sh.600000。sh: 上海，sz: 深圳")
    date:  Annotated[datetime.date, BeforeValidator(parse_date)] = Field(..., title="交易所行情日期", description="格式: YYYY-MM-DD")
    open: float = Field(..., title="今开盘价格", description="精度: 小数点后4位; 单位: 人民币元")
    high: float = Field(..., title="最高价", description="精度: 小数点后4位; 单位: 人民币元")
    low: float = Field(..., title="最低价", description="精度: 小数点后4位; 单位: 人民币元")
    close: float = Field(..., title="今收盘价", description="精度: 小数点后4位; 单位: 人民币元")
    volume: int = Field(default=0, title="成交数量", description="单位: 股")
    amount: float = Field(..., title="成交金额", description="精度: 小数点后4位; 单位: 人民币元")
    adjustFlag: int = Field(default=3, alias="adjustflag", title="复权状态", description="1: 后复权、2: 前复权、3: 不复权")
    turn: float = Field(..., title="换手率",
                        description="精度: 小数点后6位; 单位: %; [指定交易日的成交量(股)/指定交易日的股票的流通股总股数(股)]*100%")
    pctChg: float = Field(..., title="涨跌幅（百分比）", description="精度: 小数点后6位; 日涨跌幅=[(指定交易日的收盘价-指定交易日前收盘价)/指定交易日前收盘价]*100%")


    def to_json(self) -> dict:
        return {
            "code": self.code,
            "date": self.date.strftime("%Y-%m-%d"),
            "open": f"{self.open:.4f}",
            "high": f"{self.high:.4f}",
            "low": f"{self.low:.4f}",
            "close": f"{self.close:.4f}",
            "volume": self.volume,
            "amount": f"{self.amount:.4f}",
            "adjust_flag": self.adjustFlag,
            "turn": f"{self.turn:.6f}",
            "pct_chg": f"{self.pctChg:.6f}"
        }