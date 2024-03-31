from db_utils import DBUtils


class Account:
    mysql = DBUtils()
    mysql.getConnection()

    # def __init__(self, employ_id, employ_name, employ_pwd):
    #     self.employ_id = employ_id
    #     self.employ_name = employ_name
    #     self.employ_pwd = employ_pwd

    @classmethod
    def login(cls, employ_name, employ_pwd, employ_id):
        check_sql = "SELECT employ_name, employ_pwd FROM account WHERE employ_id = %s"
        check_params = [employ_id]
        cls.mysql.execute(check_sql, check_params)
        result = cls.mysql.fetchone()
        if result is None:
            print("登录失败,员工号不存在")
            return False
        elif result['employ_name'] == employ_name and result['employ_pwd'] == employ_pwd:
            print("登录成功！")
            return True
        else:
            print("用户名或密码错误")
            return False

    @classmethod
    def regist(cls, employ_id, employ_name, employ_pwd):
        check_sql = "SELECT * FROM employee WHERE employ_id = %s"
        check_params = [employ_id]
        cls.mysql.execute(check_sql, check_params)
        # existing_employee有值则存在已经注册过的员工号，反之则无;
        if cls.mysql.fetchone():
            print("员工号已存在，请重新输入。")
            return
        elif cls.mysql.fetchone() is None:
            strSql1 = "INSERT INTO account (employ_id, employ_name, employ_pwd) VALUES (%s, %s, %s)"
            params1 = [employ_id, employ_name, employ_pwd]
            cls.mysql.execute(strSql1, params1)
            cls.mysql.commit()
            strSql2 = "INSERT INTO employee (employ_id, employ_name) VALUES (%s, %s)"
            params2 = [employ_id, employ_name]
            cls.mysql.execute(strSql2, params2)
            cls.mysql.commit()
            print("注册成功")
