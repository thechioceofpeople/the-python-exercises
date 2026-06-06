students = {
    "S001": {"name": "张三", "scores": [88, 92, 85]},
    "S002": {"name": "李四", "scores": [75, 80, 79]},
    "S003": {"name": "王五", "scores": [90, 93, 88]}
}

# 添加学员
def add_student(sid, name, scores):
    if sid in students:
        raise ValueError('学号已存在')
    else:
        students[sid] = {"name": name, "scores": scores}
    return True

# 删除学员
def delete_student(sid):
    if not sid in students:
        raise KeyError('学号不存在')
    else:
        del students[sid]
        return sid

# 展示学员字典
def get_all_students():
    return students