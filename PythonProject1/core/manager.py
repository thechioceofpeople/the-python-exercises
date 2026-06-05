import exceptions.custom_errors
# 用于计算总生存天数
def calculate_survival_days(consumption,day):
    if consumption == 0:
        raise exceptions.custom_errors.ResourceEmptyError('资源不足')

    tmp = consumption/day
    return tmp