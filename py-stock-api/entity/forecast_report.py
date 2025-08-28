from pydantic import BaseModel, Field


class ForecastReport(BaseModel):
    """
    季频公司业绩预告
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    profitForcastExpPubDate: str | None = Field(default=None, title="业绩预告发布日期")
    profitForcastExpStatDate: str | None = Field(
        default=None, title="业绩预告统计日期")
    profitForcastType: str | None = Field(default=None, title="业绩预告类型")
    profitForcastAbstract: str | None = Field(default=None, title="业绩预告摘要")
    profitForcastChgPctUp: str | None = Field(
        default=None, title="预告归属于母公司的净利润增长上限(%)")
    profitForcastChgPctDwn: str | None = Field(
        default=None, title="预告归属于母公司的净利润增长下限(%)")
