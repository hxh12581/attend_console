from db_utils import DBUtils


class Attend:
    mysql = DBUtils()
    mysql.getConnection()

    @classmethod
    def sign_in(cls, attend_id, attend_name, attend_time, attend_statu):
        strSql = "insert into attend(attend_id,attend_name,attend_time,attend_statu) VALUES (%s, %s, %s, %s)"
        params = [attend_id, attend_name, attend_time, attend_statu]
        cls.mysql.execute(strSql, params=params)
        cls.mysql.commit()

    @classmethod
    def sign_out(cls, attend_id, attend_name, attend_time, attend_statu):
        strSql = "insert into attend(attend_id,attend_name,attend_time,attend_statu) VALUES (%s, %s, %s, %s)"
        params = [attend_id, attend_name, attend_time, attend_statu]
        cls.mysql.execute(strSql, params=params)
        cls.mysql.commit()

    @classmethod
    def select_sign_in(cls, attend_id, attend_statu):
        strSql = "select id,attend_name,attend_time,attend_statu from attend where attend_id =%s and attend_statu = %s "
        params = [attend_id, attend_statu]
        cls.mysql.execute(strSql, params=params)
        return cls.mysql.fetchall()

    @classmethod
    def select_sign_out(cls, attend_id, attend_statu):
        strSql = "select id,attend_name,attend_time,attend_statu from attend where attend_id =%s and attend_statu = %s"
        params = [attend_id, attend_statu]
        cls.mysql.execute(strSql, params=params)
        return cls.mysql.fetchall()

    @classmethod
    def pop_attend(cls, id, attend_id):
        strSql = "DELETE FROM attend WHERE id = %s AND attend_id = %s"
        params = [id, attend_id]
        cls.mysql.execute(strSql, params=params)
        cls.mysql.commit()

    @classmethod
    def select_attend(cls, attend_id):
        strSql = "select * from attend where attend_id = %s"
        params = [attend_id]
        cls.mysql.execute(strSql, params=params)
        return cls.mysql.fetchall()

    @classmethod
    def select_exist_id(cls, id):
        strSql = "select * from attend where id =%s"
        params = [id]
        cls.mysql.execute(strSql, params)
        if cls.mysql.fetchone():
            return True
        elif cls.mysql.fetchone() == None:
            return False
