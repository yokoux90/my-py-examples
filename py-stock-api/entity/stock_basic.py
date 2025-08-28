from pydantic import BaseModel, Field


class StockBasic(BaseModel):
    """
    证券基本资料
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    code_name: str | None = Field(default=None, title="证券名称")
    ipoDate: str | None = Field(default=None, title="上市日期")
    outDate: str | None = Field(default=None, title="退市日期")
    type: str | None = Field(default=None, title="证券类型",
                             description="1：股票，2：指数，3：其它，4：可转债，5：ETF")
    status: str | None = Field(
        default=None, title="上市状态", description="1：上市，0：退市")
