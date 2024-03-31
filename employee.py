from db_utils import DBUtils


class Employee:
    mysql = DBUtils()
    mysql.getConnection()

    @classmethod
    def add_employee(cls, employ_dp, employ_age, employ_gender, employ_Phone, employ_id):
        strSql = "update employee set employ_dp = %s,employ_age= %s, employ_gender= %s,employ_Phone= %s where employ_id = %s "
        params = [employ_dp, employ_age, employ_gender, employ_Phone, employ_id]
        cls.mysql.execute(strSql, params)
        cls.mysql.commit()

    @classmethod
    def pop_employee(cls, employ_id):
        strSql = "delete from employee where employ_id = %s"
        cls.mysql.execute(strSql, [employ_id])
        cls.mysql.commit()
        strSql = "delete from attend where attend_id = %s"
        cls.mysql.execute(strSql, [employ_id])
        cls.mysql.commit()
        strSql = "delete from `leave` where leave_id = %s"
        cls.mysql.execute(strSql, [employ_id])
        cls.mysql.commit()
        strSql = "delete from account where employ_id = %s"
        cls.mysql.execute(strSql, [employ_id])
        cls.mysql.commit()

    @classmethod
    def update_employee(cls, employ_name, employ_dp, employ_age, employ_gender, employ_Phone, employ_id):
        strSql = "update employee set employ_name = %s,employ_dp = %s,employ_age= %s, employ_gender= %s,employ_Phone= %s where employ_id = %s  "
        cls.mysql.execute(strSql, params=[employ_name, employ_dp, employ_age, employ_gender, employ_Phone, employ_id])
        cls.mysql.commit()

    @classmethod
    def select_employee(cls, employ_id):
        strSql = "select * from employee where employ_id = %s"
        cls.mysql.execute(strSql, [employ_id])
        return cls.mysql.fetchall()
