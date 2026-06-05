# 用于抛出自定义异常
class InvalidIDError(Exception):
    """id错误异常"""
    pass


class ResourceEmptyError(Exception):
    """物资不足异常"""
    pass
