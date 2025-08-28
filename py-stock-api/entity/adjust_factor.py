from pydantic import BaseModel, Field


class AdjustFactor(BaseModel):
    """
    复权因子信息
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    dividOperateDate: str | None = Field(default=None, title="除权除息日期")
    foreAdjustFactor: float | None = Field(default=None, title="向前复权因子",
                                           description="除权除息日前一个交易日的收盘价/除权除息日最近的一个交易日的前收盘价")
    backAdjustFactor: float | None = Field(default=None, title="向后复权因子",
                                           description="除权除息日最近的一个交易日的前收盘价/除权除息日前一个交易日的收盘价")
    adjustFactor: float | None = Field(default=None, title="本次复权因子")
