import sys

from datetime import datetime
from employee import Employee
from account import Account
from leave import Leave
from attend import Attend
from pagination_tool import getleavePageList, getattendPageList
from pagination_tool import getleaveTotalCount, getattendTotalCount


class Utilities:
    # 类属性存储登录状态下员工号
    login_user_id = None
    # 类属性存储登录状态下员工姓名
    login_user_name = None

    @classmethod
    def index(cls):
        print("-----------------------------------------------------")
        print("欢迎使用员工考勤管理系统V1.0!")
        print("1-账号管理")
        print("2-考勤管理")
        print("3-请假管理")
        print("4-退出系统")
        print("-----------------------------------------------------")
        cls.choose()

    @classmethod
    def choose(cls):
        index = int(input("输入你要使用的系统功能:"))
        if index == 1:
            # 账号管理功能
            cls.employee()
        elif index == 2:
            # 考勤功能
            cls.attend()
        elif index == 3:
            # 请假功能
            cls.leave()
        elif index == 4:
            # 退出系统
            cls.login_user_id = None
            cls.login_user_name = None
            sys.exit()
        else:
            print("输入错误,请重新输入")
            cls.choose()

    # 登录注册功能
    @classmethod
    def account(cls):
        """
        :登录注册功能的实现
        :author:何晓辉
        :time:2024.3.26
        :return:
        """
        print("-----------------------------------------------------")
        print("员工考勤管理系统")
        print("1-账号登录  2-注册账号")
        print("-----------------------------------------------------")

        def is_continue():
            answer = input("继续操作吗？")
            if answer == 'y':
                cls.account()
            elif answer == 'n':
                print("返回首页")
                cls.index()
            else:
                print("输入不规范，请重新输入！")
                is_continue()

        index = int(input("输入你要使用的功能:"))
        # 登录
        if index == 1:
            employ_id = input("请输入您的员工号")
            employ_name = input("请输入您的用户名")
            employ_pwd = input("请输入您的密码")
            # 存取登录用户的员工号
            if Account.login(employ_name, employ_pwd, employ_id):
                cls.login_user_id = employ_id
                cls.login_user_name = employ_name
                cls.index()
            else:
                print("员工号重复或用户名、密码错误！请重新输入")
                cls.account()
        # 注册
        elif index == 2:
            employ_id = input("请输入您的员工号")
            employ_name = input("请输入您的用户名")
            employ_pwd = input("请输入您的密码")
            Account.regist(employ_id, employ_name, employ_pwd)
            is_continue()
        else:
            print("输入不规范，请重新输入！")
            is_continue()

    # 账号管理功能
    @classmethod
    def employee(cls):
        """
        :账户管理功能的实现
        :author:何晓辉
        :time:2024.3.18
        :更新:2024.3.26
        :return:
        """

        def is_continue():
            answer = input("继续操作吗？")
            if answer == 'y':
                cls.employee()
            elif answer == 'n':
                print("返回首页")
                cls.index()
            else:
                print("输入错误，请重新输入！")
                is_continue()

        print("-----------------------------------------------------")
        print("欢迎使用账号管理功能")
        print("1-补充账号信息  2-注销账号信息  3-修改账号信息  4-查询账号信息  5-退出系统  6-返回系统首页")
        print("-----------------------------------------------------")
        index = int(input("输入你要使用的功能:"))
        if index == 1:
            # 增加员工账号信息
            employ_id = cls.login_user_id
            employ_dp = input("请你补全您的部门信息:")
            employ_age = int(input("请你补全您的年龄:"))
            employ_gender = input("请你补全您的性别:")
            employ_Phone = input("请你补全您的电话号:")
            Employee.add_employee(employ_dp, employ_age, employ_gender, employ_Phone, employ_id)
            print("补全成功！")
            is_continue()
        elif index == 2:
            # 注销账号并且关于账号的一切信息都将被删除
            Employee.pop_employee(cls.login_user_id)
            print("注销成功！")
            cls.login_user_id = None
            cls.login_user_name = None
            sys.exit()
        elif index == 3:
            # 修改员工账号信息
            employ_name = input("请你输入修改的员工姓名:")
            employ_dp = input("请你输入修改的部门信息:")
            employ_age = int(input("请你输入修改的员工年龄:"))
            employ_gender = input("请你输入修改的员工性别:")
            employ_Phone = input("请你输入修改的员工电话号:")
            Employee.update_employee(employ_name, employ_dp, employ_age, employ_gender, employ_Phone,
                                     cls.login_user_id)
            print("修改成功！")
            is_continue()
        elif index == 4:
            # 查询员工账号信息
            list = Employee.select_employee(cls.login_user_id)
            print(
                "工号" + "\t" + "\t" + "姓名" + "\t" + "\t" + "部门" + "\t" + "\t" + "年龄" + "\t" + "\t" + "性别" + "\t" + "\t" + "电话号")
            for i in list:
                print(str(i.get('employ_id')) + "\t", end="")
                print(str(i.get('employ_name')) + "\t", end="")
                print(str(i.get('employ_dp')) + "\t", end="")
                print(str(i.get('employ_age')) + "\t", end="")
                print(str(i.get('employ_gender')) + "\t", end="")
                print(str(i.get('employ_Phone')) + "\t")
            is_continue()
        elif index == 5:
            print("已退出系统！")
            cls.login_user_id = None
            cls.login_user_name = None
            sys.exit()
        elif index == 6:
            print("返回首页！")
            Utilities.index()
        else:
            print("输入不规范，请重新输入！")
            is_continue()

    # 员工考勤管理功能
    @classmethod
    def attend(cls):
        """
        :员工考勤管理功能的实现
        :author:何晓辉
        :time:2024.3.26
        :return:
        """

        def is_continue():
            answer = input("继续操作吗？")
            if answer == 'y':
                cls.attend()
            elif answer == 'n':
                print("返回首页")
                cls.index()
            else:
                print("输入错误，请重新输入！")
                is_continue()

        print("-----------------------------------------------------")
        print("欢迎使用考勤管理功能")
        print("1-签到  2-签退  3-打印签到表 4-打印签退表 5删除考勤记录 6查看考勤纪录 7-退出系统 8-返回系统首页")
        print("-----------------------------------------------------")
        index = int(input("输入你要使用的功能:"))
        if index == 1:
            attend_id = cls.login_user_id
            attend_name = cls.login_user_name
            attend_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Attend.sign_in(attend_id, attend_name, attend_time, '已签到')
            print("签到成功！")
            is_continue()
        elif index == 2:
            attend_id = cls.login_user_id
            attend_name = cls.login_user_name
            attend_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Attend.sign_out(attend_id, attend_name, attend_time, '已签退')
            print("签退成功！")
            is_continue()
        elif index == 3:
            list = Attend.select_sign_in(cls.login_user_id, attend_statu='已签到')
            print("序号" + "\t" + "姓名" + "\t" + "\t" + "\t" + "签到时间" + "\t" + "\t" + "\t" + "考勤状态")
            for i in list:
                print(str(i.get('id')) + "\t", end="")
                print(str(i.get('attend_name')) + "\t", end="")
                print(str(i.get('attend_time')) + "\t", end="")
                print(str(i.get('attend_statu')) + "\t")
            is_continue()
        elif index == 4:
            list = Attend.select_sign_out(cls.login_user_id, attend_statu='已签退')
            print("序号" + "\t" + "姓名" + "\t" + "\t" + "签退时间" + "\t" + "\t" + "\t" + "考勤状态")
            for i in list:
                print(str(i.get('id')) + "\t", end="")
                print(str(i.get('attend_name')) + "\t", end="")
                print(str(i.get('attend_time')) + "\t", end="")
                print(str(i.get('attend_statu')) + "\t")
            is_continue()
        elif index == 5:
            attend_id = cls.login_user_id
            id = input("请输入您要删除的考勤纪录序号")
            if Attend.select_exist_id(id):
                Attend.pop_attend(id, attend_id)
                is_continue()
            else:
                print("删除无效,不存在考勤纪录")
                is_continue()
            is_continue()
        elif index == 6:
            # 1.分页显示请假信息
            currentPage = 1  # 当前页
            pageSize = 5
            totalPage = 0  # 总页数

            while True:
                attendList = getattendPageList(cls.login_user_id, currentPage, pageSize)
                # 每页数据
                totalCount = getattendTotalCount().get('total')
                # 所有记录数
                if totalCount % pageSize == 0:
                    totalPage = totalCount // pageSize
                    # 总页数
                else:
                    totalPage = totalCount // pageSize + 1
                print(
                    "序号" + "\t" + "工号" + "\t" + "\t" + "员工姓名" + "\t" + "\t" + "\t" + "时间" + "\t" + "\t" + "\t" + "考勤状态")
                # print(attendList)
                for i in attendList:
                    print(str(i.get('id')) + "\t", end="")
                    print(str(i.get('attend_id')) + "\t", end="")
                    print(str(i.get('attend_name')) + "\t", end="")
                    print(str(i.get('attend_time')) + "\t", end="")
                    print(str(i.get('attend_statu')) + "\t")
                print("1.首页 2.上一页 3.下一页 4.尾页 5.退出查询")
                option = input("请输入选项：")
                if option == '1':
                    currentPage = 1
                elif option == '2':
                    if currentPage > 1:
                        currentPage -= 1
                elif option == '3':
                    if currentPage >= totalPage:
                        print("已经是最后一页")
                    else:
                        currentPage += 1
                elif option == '4':
                    currentPage = totalPage
                elif option == '5':
                    cls.attend()
            # Attend.select_attend(cls.login_user_id[0])
            # is_continue(cls)
        elif index == 7:
            print("已退出系统！")
            cls.login_user_id = None
            cls.login_user_name = None
            sys.exit()
        elif index == 8:
            print("返回首页！")
            Utilities.index()
        else:
            print("输入不规范，请重新输入！")
            is_continue()

    # 员工请假功能
    @classmethod
    def leave(cls):
        """
        :员工请假功能的实现
        :author:莫潮靖(修改) 张宁(增加) 吴建宇(删除) 唐京华(查询)
        :time:2024.3.26 上午
        :更新：何晓辉 2024.3.26.下午
        :return:
        """

        def is_continue():
            answer = input("继续操作吗？")
            if answer == 'y':
                cls.leave()
            elif answer == 'n':
                print("返回首页")
                cls.index()
            else:
                print("输入错误，请重新输入！")
                is_continue()

        print("-----------------------------------------------------")
        print("欢迎使用请假销假功能")
        print("1-显示记录  2-请假  3-修改请假信息 4-销假 5-删除记录 6-退出系统  7-返回系统首页")
        print("-----------------------------------------------------")
        index = int(input("输入你要使用的功能:"))
        if index == 1:
            # 1.分页显示请假信息
            currentPage = 1  # 当前页
            pageSize = 5
            totalPage = 0  # 总页数
            # 功能循环
            while True:
                leaveList = getleavePageList(cls.login_user_id, currentPage, pageSize)
                totalCount = getleaveTotalCount().get('total')
                if totalCount % pageSize == 0:
                    totalPage = totalCount // pageSize
                else:
                    totalPage = totalCount // pageSize + 1

                # 输出内容
                print(
                    "序号" + "\t" + "工号" + "\t" + "\t" + "姓名" + "\t" + "\t" + "请假事由" + "\t" + "状态" + "\t" + "\t" + "\t" + "开始时间" + "\t" + "\t" + "\t" + "\t" + "结束时间")
                # print(attendList)
                for i in leaveList:
                    print(str(i.get('id')) + "\t", end="")
                    print(str(i.get('leave_id')) + "\t", end="")
                    print(str(i.get('leave_name')) + "\t", end="")
                    print(str(i.get('leave_statu_reason')) + "\t", end="")
                    print(str(i.get('leave_statu')) + "\t", end="")
                    print(str(i.get('leave_stime')) + "\t", end="")
                    print(str(i.get('leave_etime')) + "\t")
                print("1.首页 2.上一页 3.下一页 4.尾页 5.退出查询")
                option = input("请输入选项：")
                if option == '1':
                    currentPage = 1
                elif option == '2':
                    if currentPage > 1:
                        currentPage -= 1
                elif option == '3':
                    if currentPage >= totalPage:
                        print("已经是最后一页")
                    else:
                        currentPage += 1
                elif option == '4':
                    currentPage = totalPage
                elif option == '5':
                    cls.leave()
            # Leave.select_leave()
            # is_continue(cls)
        elif index == 2:
            leave_statu_reason = input("请输入你要添加的请假原因(因公请假/因私请假)：")
            leave_stime = input("请输入你要添加的请假开始时间：")
            leave_etime = input("请输入你要添加的请假结束时间：")
            Leave.add_leave(cls.login_user_id, cls.login_user_name, leave_statu_reason, '已请假', leave_stime,
                            leave_etime)
            is_continue()
        elif index == 3:
            Leave.select_leave()
            id = input("请你输入修改的请假编号:")
            leave_statu_reason = input("请输入你要修改的请假原因(因公请假/因私请假)：")
            leave_stime = input("请输入你要修改的请假开始时间")
            leave_etime = input("请输入你要修改的请假结束时间")
            if Leave.select_exist_id(id):
                Leave.update_leave(id, leave_statu_reason, leave_stime, leave_etime)
                is_continue()
            else:
                print("修改无效,不存在请假编号")
                is_continue()
            is_continue()
        elif index == 4:
            Leave.select_leave()
            id = input("请你输入销假的编号:")
            if Leave.select_exist_id(id):
                Leave.update_leave_statu(id, '已销假')
            else:
                print("销假无效,不存在编号")
                is_continue()
            is_continue()
        elif index == 5:
            Leave.select_leave()
            id = input("请你输入删除的记录编号:")
            if Leave.select_exist_id(id):
                Leave.pop_leave(id)
                is_continue()
            else:
                print("删除无效,不存在记录编号")
                is_continue()
            is_continue()
        elif index == 6:
            print("已退出系统！")
            cls.login_user_id = None
            cls.login_user_name = None
            sys.exit()
        elif index == 7:
            print("返回首页！")
            cls.index()


# 主函数窗口
if __name__ == '__main__':
    util = Utilities()
    util.account()
