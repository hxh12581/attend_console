from db_utils import DBUtils


# 分页查询工具类
# 获取请假表的分页数据
def getleavePageList(leave_id,currentPage, pageSize):
    dbConn = DBUtils()
    sql = 'select * from `leave` where 1=1 and leave_id=%s'
    params = [leave_id]
    # 添加分页机制
    sql += " limit %s,%s"  # 开始页数/页数
    startRow = int((currentPage - 1) * pageSize)
    params.append(startRow)
    params.append(pageSize)  # 保存分页的参数，每页显示多少行
    resultSet = None
    try:
        dbConn.execute(sql, params)
        resultSet = dbConn.fetchall()
    except Exception as e:
        print(e)
    finally:
        dbConn.close()
    return resultSet


# 获取请假表的数据总页数
def getleaveTotalCount():
    dbConn = DBUtils()
    total = None
    sql = 'select count(*) as total from `leave` where 1=1'
    params = []
    try:
        dbConn.execute(sql, params)
        total = dbConn.fetchone()
    except Exception as e:
        print(e)
    finally:
        dbConn.close()
    return total


# 获取考勤表的分页数据
def getattendPageList(attend_id,currentPage, pageSize):
    dbConn = DBUtils()
    sql = 'select * from `attend` where 1=1 and attend_id=%s'
    params = [attend_id]
    # 添加分页机制
    sql += " limit %s,%s"  # 开始页数/页数
    startRow = int((currentPage - 1) * pageSize)
    params.append(startRow)
    params.append(pageSize)  # 保存分页的参数，每页显示多少行
    resultSet = None
    try:
        dbConn.execute(sql, params)
        resultSet = dbConn.fetchall()
    except Exception as e:
        print(e)
    finally:
        dbConn.close()
    return resultSet


# 获取考勤表的数据总页数
def getattendTotalCount():
    dbConn = DBUtils()
    total = None
    sql = 'select count(*) as total from `attend` where 1=1'
    params = []
    try:
        dbConn.execute(sql, params)
        total = dbConn.fetchone()

    except Exception as e:
        print(e)
    finally:
        dbConn.close()
    return total
