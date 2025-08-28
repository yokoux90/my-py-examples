import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ReqKMinute(BaseModel):
    """
    code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
    start：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
    end：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
    frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写；指数没有分钟线数据；周线每周最后一个交易日才可以获取，月线每月最后一个交易日才可以获取。
    adjustflag：复权类型，默认不复权：3；1：后复权；2：前复权。已支持分钟线、日线、周线、月线前后复权
    """
    code: str
    start: datetime.date
    end: datetime.date
    frequency: Literal["5", "15", "30", "60"] = Field(default="5")
    adjust_flag: str = Field(default="3", title="复权状态", description="1: 后复权、2: 前复权、3: 不复权")

class ReqKDay(BaseModel):
    """
       code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
       start：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
       end：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
       adjustflag：复权类型，默认不复权：3；1：后复权；2：前复权。已支持分钟线、日线、周线、月线前后复权
   """
    code: str
    start: datetime.date
    end: datetime.date
    adjust_flag: str = Field(default="3", title="复权状态", description="1: 后复权、2: 前复权、3: 不复权")

class ReqKWeek(BaseModel):
    """
       code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
       start：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
       end：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
       adjustflag：复权类型，默认不复权：3；1：后复权；2：前复权。已支持分钟线、日线、周线、月线前后复权
   """
    code: str
    start: datetime.date
    end: datetime.date
    adjust_flag: str = Field(default="3", title="复权状态", description="1: 后复权、2: 前复权、3: 不复权")

class ReqKMonth(BaseModel):
    """
       code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
       start：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
       end：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
       adjustflag：复权类型，默认不复权：3；1：后复权；2：前复权。已支持分钟线、日线、周线、月线前后复权
   """
    code: str
    start: datetime.date
    end: datetime.date
    adjust_flag: str = Field(default="3", title="复权状态", description="1: 后复权、2: 前复权、3: 不复权")