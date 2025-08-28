from pydantic import BaseModel, Field


class GrowthData(BaseModel):
    """
    季频成长能力
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    pubDate: str | None = Field(default=None, title="公司发布财报的日期")
    statDate: str | None = Field(default=None, title="财报统计的季度的最后一天, 比如2017-03-31, 2017-06-30")
    YOYEquity: str | None = Field(default=None, title="净资产同比增长率",
                                    description="(本期净资产-上年同期净资产)/上年同期净资产的绝对值*100%")
    YOYAsset: str | None = Field(default=None, title="总资产同比增长率",
                                   description="(本期总资产-上年同期总资产)/上年同期总资产的绝对值*100%")
    YOYNI: str | None = Field(default=None, title="净利润同比增长率",
                                     description="(本期净利润-上年同期净利润)/上年同期净利润的绝对值*100%")
    YOYEPSBasic: str | None = Field(default=None, title="基本每股收益同比增长率",
                                    description="(本期基本每股收益-上年同期基本每股收益)/上年同期基本每股收益的绝对值*100%")
    YOYPNI: str | None = Field(default=None, title="归属母公司股东净利润同比增长率",
                                    description="(本期归属母公司股东净利润-上年同期归属母公司股东净利润)/上年同期归属母公司股东净利润的绝对值*100%")
