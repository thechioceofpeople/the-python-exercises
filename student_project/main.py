from student_manager import *

while True:
    print('1.添加学生')
    print('2.删除学生')
    print('3.查询学生平均分')
    print('4.显示最高分学生')
    print('5.显示排名')
    print('6.查看所有学生')
    print('7.退出')
    choice = input('请输入你的选择：')
    if not choice.isdigit():
        print('无效选项')
        continue
    elif not choice in ['1', '2', '3', '4', '5', '6', '7']:
        print('无效选项')
        continue

    elif choice == '1':
        sid = input('请输入学号：')
        name = input('请输入姓名：')
        try:
            validate_student_id(sid)
            tmp = input_scores()
            add_student(sid, name, tmp)
        except ValueError as e:
            print(e)
            continue

    elif choice == '2':
        sid = input('请输入学号：')
        try:
            tmp = delete_student(sid)
            print(f'删除{tmp}成功！')
        except KeyError as e:
            print(e)
            continue

    elif choice == '3':
        sid = input('请输入学号：')
        tmp = average_score(sid)
        if not tmp:
            print('学号不存在')
            continue
        else:
            print(f'{tmp[0]}的平均分是{tmp[1]}')

    elif choice == '4':
        tmp = top_student()
        print(f'平均分最高的学生是：{tmp}')

    elif choice == '5':
        tmp = rank_all()
        print('平均分排名为：',tmp)

    elif choice == '6':
        tmp = get_all_students()
        print(tmp)
