from db_utils import DBUtils
from datetime import datetime


class Leave:
    mysql = DBUtils()
    mysql.getConnection()


    @classmethod
    def select_exist_id(cls,id):
        strSql = "select * from  `leave` where id =%s"
        params = [id]
        cls.mysql.execute(strSql, params)
        if cls.mysql.fetchone():
            return True
        elif cls.mysql.fetchone()==None:
            return False


    # 添加操作
    @classmethod
    def add_leave(cls, leave_id, leave_name, leave_statu_reason, leave_statu, leave_stime, leave_etime):
        strSql = "INSERT INTO `leave` (leave_id,leave_name,leave_statu_reason,leave_statu,leave_stime,leave_etime) VALUES (%s, %s, %s, %s, %s, %s)"
        params = [leave_id, leave_name, leave_statu_reason, leave_statu, leave_stime, leave_etime]
        cls.mysql.execute(strSql, params)
        cls.mysql.commit()

    # 显示操作
    @classmethod
    def select_leave(cls):
        strSql = "select * from `leave`"
        cls.mysql.execute(strSql)
        return cls.mysql.fetchall()

    # 删除操作
    @classmethod
    def pop_leave(cls, id):
        strSql = "delete from `leave` where id = %s"
        cls.mysql.execute(strSql, [id])
        cls.mysql.commit()

    # 修改请假信息
    @classmethod
    def update_leave(cls, id=None, leave_statu_reason=None, leave_stime=None, leave_etime=None):
        strSql = "update `leave` set leave_statu_reason= %s, leave_stime= %s,leave_etime= %s where id = %s  "
        cls.mysql.execute(strSql, params=[leave_statu_reason, leave_stime, leave_etime, id])
        cls.mysql.commit()

    @classmethod
    def update_leave_statu(cls, id, leave_statu):
        strSql = "update `leave` set leave_statu = %s where id = %s  "
        cls.mysql.execute(strSql, params=[leave_statu, id])
        cls.mysql.commit()
