import pymysql


class DBUtils():
    """数据库访问基类"""

    def __init__(self) -> None:
        self.__config = {"host": "localhost", "user": "root",
                         "password": "123456",
                         "database": "db_attend_console", "port": 3306, "charset": "utf8"}
        self.__conn = None
        self.__cursor = None

    # 获取数据库的连接
    def getConnection(self):
        if self.__conn != None:
            return self.__conn
        self.__conn = pymysql.connect(**self.__config)
        return self.__conn

    # 执行数据库操作，默认返回字典类型数据
    def execute(self, sql, params=[], ret="dict"):
        result = 0
        try:
            self.__conn = self.getConnection()
            if ret == "dict":
                self.__cursor = self.__conn.cursor(pymysql.cursors.DictCursor)  # 返回字典数据
            else:
                self.__cursor = self.__conn.cursor()  # 返回元组数据
            result = self.__cursor.execute(sql, params)
        except pymysql.DatabaseError as e:
            print(e)
        return result

    # 单条数据查询
    def fetchone(self):
        if self.__cursor:
            return self.__cursor.fetchone()

    # 多条数据查询
    def fetchall(self):
        if self.__cursor:
            return self.__cursor.fetchall()

    # 关闭数据库连接
    def close(self):
        if self.__cursor:
            self.__cursor.close()

        if self.__conn:
            self.__conn.close()

    # 提交事务
    def commit(self):
        if self.__conn:
            self.__conn.commit()

    # 回归事务
    def rollback(self):
        if self.__conn:
            self.__conn.rollback()
