# 用函数检查ID是否时正确格式，且不能包含数字
import exceptions.custom_errors
import utlis.data_store

# 检查用户名格式
def people_check_id(people_id):
    if not isinstance(people_id, str):
        # 判断是否为字符串
        raise exceptions.custom_errors.InvalidIDError('id格式错误')

    elif not people_id.startswith('MISSION-'):
        # 检查开头格式是否正确
        raise exceptions.custom_errors.InvalidIDError('id开头格式错误')

    elif len(people_id) <= 9:
        # 检查长度是否正确
        raise exceptions.custom_errors.InvalidIDError('id长度错误')

    elif people_id in utlis.data_store.people:
        # 检查唯一性
        raise exceptions.custom_errors.InvalidIDError('id已存在')

    elif not people_id[8:].isdigit():
        # 检查数字部分是否是纯数字
        raise exceptions.custom_errors.InvalidIDError('id后面格式错误')

    else:
        return True

# 检查名字格式
def people_check_name(people_name):
    for i in people_name:
        if i.isdigit():
            raise exceptions.custom_errors.InvalidIDError('名字错误')
    return True
