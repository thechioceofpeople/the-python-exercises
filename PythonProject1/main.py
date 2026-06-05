import utlis.validator
import utlis.data_store
import core.manager
import core.calculator
from exceptions.custom_errors import InvalidIDError,ResourceEmptyError

while True:
    print('1.添加成员')
    print('2.查看清单')
    print('3.计算生存天数')
    print('4.退出')
    choice = input('请输入你的选择：')

    if not choice.isdigit() or choice not in ['1', '2', '3', '4']:
        print('请输入正确的数字')
        continue
    elif choice == '4':
        break

    elif choice == '1':
        people_ID = input('请输入成员编号：')
        try:
            utlis.validator.people_check_id(people_ID)
        except InvalidIDError as e:
            print(e)

        people_name = input('请输入成员名称：')
        try:
            utlis.validator.people_check_name(people_name)
        except InvalidIDError as e:
            print(e)

        people_job = input('请输入职位')
        try:
            if isinstance(people_job, str):
                raise InvalidIDError('职位格式错误')
        except InvalidIDError as e:
            print(e)

        utlis.data_store.people[people_ID] = (people_name, people_job)
    elif choice == '2':
        print(utlis.data_store.material)

    elif choice == '3':
        daily_consumption = core.calculator.a
        try:
            tmp = core.manager.calculate_survival_days(utlis.data_store.daily_consumption,daily_consumption)
            print(int(tmp))
        except ResourceEmptyError as e:
            print(e)


