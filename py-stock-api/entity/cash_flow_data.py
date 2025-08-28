from pydantic import BaseModel, Field


class CashFlowData(BaseModel):
    """
    季频现金流量
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    pubDate: str | None = Field(default=None, title="公司发布财报的日期")
    statDate: str | None = Field(
        default=None, title="财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30")
    CAToAsset: str | None = Field(default=None, title="流动资产除以总资产")
    NCAToAsset: str | None = Field(default=None, title="非流动资产除以总资产")
    tangibleAssetToAsset: str | None = Field(default=None, title="有形资产除以总资产")
    ebitToInterest: str | None = Field(default=None, title="已获利息倍数",
                                       description="息税前利润/利息费用")
    CFOToOR: str | None = Field(default=None, title="经营活动产生的现金流量净额除以营业收入")
    CFOToNP: str | None = Field(default=None, title="经营性现金净流量除以净利润")
    CFOToNP: str | None = Field(default=None, title="经营性现金净流量除以营业总收入")
