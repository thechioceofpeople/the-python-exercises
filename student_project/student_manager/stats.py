from . import data

# 计算学生的平均分
def average_score(sid):
    if sid not in data.students:
        return None
    else:
        tmp = data.students[sid]['scores']
        tmp = round(sum(tmp) / len(tmp),1)
        return data.students[sid]['name'], tmp # 元组的核心标志是逗号，可以删除括号（不然系统提示冗余）

# 最高平均分
def top_student():
    if len(data.students) == 0:
        return None
    else:
        tmp = max(data.students.items(), key=lambda x: sum(x[1]['scores']) / len(x[1]['scores']))
        return tmp[0],tmp[1]['name']

# 平均分排列
def rank_all():
    student_list = []
    if len(data.students) == 0:
        return None
    else:
        for k, v in data.students.items():
            tmp = round(sum(v['scores']) / len(v['scores']), 1)
            student_list.append((k, v['name'], tmp))
    student_list.sort(key=lambda x: x[2], reverse=True)
    return student_list
