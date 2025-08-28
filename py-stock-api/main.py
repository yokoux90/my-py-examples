import handler
import baostock as bs

from fastapi import FastAPI

# Login BaoStock
bs.login()

app = FastAPI()

# K线数据
app.include_router(handler.k_history.router)
# 除权除息信息
app.include_router(handler.dividend_data.router)
# 复权因子信息
app.include_router(handler.adjust_factor.router)
# 季频盈利能力
app.include_router(handler.profit_data.router)
# 季频营运能力
app.include_router(handler.operation_data.router)
# 季频成长能力
app.include_router(handler.growth_data.router)
# 季频偿债能力
app.include_router(handler.balance_data.router)
# 季频现金流量
app.include_router(handler.cash_flow_data.router)
# 季频杜邦指数
app.include_router(handler.dupont_data.router)
# 季频公司业绩快报
app.include_router(handler.performance_express_report.router)
# 季频公司业绩预告
app.include_router(handler.forecast_report.router)
# 证券基本资料
app.include_router(handler.stock_basic.router)
# 行业分类
app.include_router(handler.stock_industry.router)
# 存款利率
app.include_router(handler.deposit_rate_data.router)
# 贷款利率
app.include_router(handler.loan_rate_data.router)
# 存款准备金率
app.include_router(handler.required_reserve_ratio_data.router)
# 货币供应量
app.include_router(handler.money_supply_data_month.router)
# 上证50成分股
app.include_router(handler.sz50_stock.router)
# 沪深300成分股
app.include_router(handler.hs300_stock.router)
# 中证500成分股
app.include_router(handler.zz500_stock.router)
