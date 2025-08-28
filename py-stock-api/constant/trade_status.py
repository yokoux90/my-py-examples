from enum import Enum

class TradeStatus(Enum):
    # 正常交易
    Normal = 0
    # 停牌
    Suspend = 1