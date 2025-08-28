from enum import Enum


class AdjustFlag(Enum):
    # 后复权
    BackwardAdjustment = 1
    # 前复权
    ForwardAdjustment = 2
    # 不复权(Default)
    NoAdjustment = 3


