from pydantic import BaseModel, Field


class PerformanceExpressReport(BaseModel):
    """
    季频公司业绩快报
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    performanceExpPubDate: str | None = Field(default=None, title="业绩快报披露日")
    performanceExpStatDate: str | None = Field(default=None, title="业绩快报统计日期")
    performanceExpUpdateDate: str | None = Field(
        default=None, title="业绩快报披露日(最新)")
    performanceExpressTotalAsset: str | None = Field(
        default=None, title="业绩快报总资产")
    performanceExpressNetAsset: str | None = Field(
        default=None, title="业绩快报净资产")
    performanceExpressEPSChgPct: str | None = Field(
        default=None, title="业绩每股收益增长率")
    performanceExpressROEWa: str | None = Field(
        default=None, title="业绩快报净资产收益率ROE-加权")
    performanceExpressEPSDiluted: str | None = Field(
        default=None, title="业绩快报每股收益EPS-摊薄")
    performanceExpressGRYOY: str | None = Field(
        default=None, title="业绩快报营业总收入同比")
    performanceExpressOPYOY: str | None = Field(
        default=None, title="业绩快报营业利润同比")
