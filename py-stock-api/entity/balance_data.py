from pydantic import BaseModel, Field


class BalanceData(BaseModel):
    """
    季频偿债能力
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    pubDate: str | None = Field(default=None, title="公司发布财报的日期")
    statDate: str | None = Field(
        default=None, title="财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30")
    currentRatio: str | None = Field(default=None, title="流动比率",
                                     description="流动资产/流动负债")
    quickRatio: str | None = Field(default=None, title="速动比率",
                                   description="(流动资产-存货净额)/流动负债")
    cashRatio: str | None = Field(default=None, title="现金比率",
                                  description="(货币资金+交易性金融资产)/流动负债")
    YOYLiability: str | None = Field(default=None, title="总负债同比增长率",
                                     description="(本期总负债-上年同期总负债)/上年同期中负债的绝对值*100%")
    liabilityToAsset: str | None = Field(default=None, title="资产负债率",
                                         description="负债总额/资产总额")
    assetToEquity: str | None = Field(default=None, title="权益乘数",
                                      description="资产总额/股东权益总额=1/(1-资产负债率)")
