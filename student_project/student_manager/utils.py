# 检查输入的学号是否符合规则：以s开头
def validate_student_id(sid):
    if not isinstance(sid, str) or not sid.startswith('S'):
        raise ValueError('学号格式错误')
    elif not sid[1:].isdigit():
        raise ValueError('学号格式错误')
    return True

# 提示用户输入成绩，并对成绩进行判断
def input_scores():
    while True:
        chinese_score = input('请输入语文成绩：')
        math_score = input('请输入数学成绩：')
        english_score = input('请输入英语成绩：')
        try:
            chinese_score = int(chinese_score)
            math_score = int(math_score)
            english_score = int(english_score)
            if not 100 >= chinese_score >= 0 or not 100 >= math_score >= 0 or not 100 >= english_score >= 0:
                raise ValueError
            return [chinese_score, math_score, english_score]
        except ValueError:
            print('请输入数字！且分数在0-100以内')
            continue
    return None
