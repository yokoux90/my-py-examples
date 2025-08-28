from pydantic import BaseModel, Field


class ProfitData(BaseModel):
    """
    季频盈利能力
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    pubDate: str | None = Field(default=None, title="公司发布财报的日期")
    statDate: str | None = Field(default=None, title="财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30")
    roeAvg: str | None = Field(default=None, title="净资产收益率(平均)(%)", description="归属母公司股东净利润/[(期初归属母公司股东的权益+期末归属母公司股东的权益)/2]*100%")
    npMargin: str | None = Field(default=None, title="销售净利率(%)", description="净利润/营业收入*100%")
    gpMargin: str | None = Field(default=None, title="销售毛利率(%)", description="毛利/营业收入*100%=(营业收入-营业成本)/营业收入*100%")
    netProfit: str | None = Field(default=None, title="净利润(元)")
    epsTTM: str | None = Field(default=None, title="每股收益", description="归属母公司股东的净利润TTM/最新总股本")
    MBRevenue: str | None = Field(default=None, title="主营营业收入(元)")
    totalShare: str | None = Field(default=None, title="总股本")
    liqaShare: str | None = Field(default=None, title="流通股本")
