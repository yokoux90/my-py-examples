from pydantic import BaseModel, Field


class OperationData(BaseModel):
    """
    季频营运能力
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    pubDate: str | None = Field(default=None, title="公司发布财报的日期")
    statDate: str | None = Field(default=None, title="财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30")
    NRTurnRatio: str | None = Field(default=None, title="应收账款周转率(次)",
                                    description="营业收入/[(期初应收票据及应收账款净额+期末应收票据及应收账款净额)/2]")
    NRTurnDays: str | None = Field(default=None, title="应收账款周转天数(天)",
                                   description="季报天数/应收账款周转率(一季报：90天，中报：180天，三季报：270天，年报：360天)")
    INVTurnRatio: str | None = Field(default=None, title="存货周转率(次)",
                                     description="营业成本/[(期初存货净额+期末存货净额)/2]")
    INVTurnDays: str | None = Field(default=None, title="存货周转天数(天)",
                                    description="季报天数/存货周转率(一季报：90天，中报：180天，三季报：270天，年报：360天)")
    CATurnRatio: str | None = Field(default=None, title="流动资产周转率(次)",
                                    description="营业总收入/[(期初流动资产+期末流动资产)/2]")
    AssetTurnRatio: str | None = Field(default=None, title="总资产周转率",
                                       description="营业总收入/[(期初资产总额+期末资产总额)/2]")
