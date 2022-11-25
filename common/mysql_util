import pymysql
import json


class OperateMysql(object):
    def __init__(self):
        # 数据库初始化连接
        self.connect_interface_testing = pymysql.connect(
            # 数据库地址信息
            host="localhost",
            user="root",
            password="root",
            database="test",
            charset='utf8mb4',
        )
        # 创建游标操作数据库
        self.cursor_interface_testing = self.connect_interface_testing.cursor()

    def select_first_data(self, sql):
        """
        查询第一条数据
        """
        try:
            # 执行 sql 语句
            self.cursor_interface_testing.execute(sql)
        except Exception as e:
            print("执行sql异常:%s" % e)
        else:
            # 获取查询到的第一条数据
            first_data = self.cursor_interface_testing.fetchone()
            # print(first_data)
            # 将返回结果转换成 str 数据格式，禁用acsii编码
            first_data = json.dumps(first_data, ensure_ascii=False)
            # self.connect_interface_testing.close()
            return first_data

    def select_all_data(self, sql):
        """
        查询结果集
        """
        try:
            self.cursor_interface_testing.execute(sql)
        except Exception as e:
            print("执行sql异常:%s" % e)
        else:
            first_data = self.cursor_interface_testing.fetchall()
            first_data = json.dumps(first_data, ensure_ascii=False)
            # self.connect_interface_testing.close()
            return first_data

    def del_data(self, sql):
        """
        删除数据
        """
        res = {}
        try:
            # 执行SQL语句
            result = self.cursor_interface_testing.execute(sql)
            # print(result)
            if result != 0:
                # 提交修改
                self.connect_interface_testing.commit()
                res = {'删除成功'}
            else:
                res = {'没有要删除的数据'}
        except:
            # 发生错误时回滚
            self.connect_interface_testing.rollback()
            res = {'删除失败'}
        return res

    def update_data(self, sql):
        """
        修改数据
        """
        try:
            self.cursor_interface_testing.execute(sql)
            self.connect_interface_testing.commit()
            res = {'更新成功'}
        except Exception as e:
            self.connect_interface_testing.rollback()
            res = {'更新删除'}
        return res

    def insert_data(self, sql, data):
        """
        新增数据
        """

        try:
            self.cursor_interface_testing.execute(sql, data)
            self.connect_interface_testing.commit()
            res = {data, '新增成功'}
        except Exception as e:
            res = {'新增失败', e}
        return res

    def conn_close(self):
        # 关闭数据库
        self.cursor_interface_testing.close()


if __name__ == "__main__":
    # ()类的实例化
    om = OperateMysql()

    # 新增
    data = [{'id': 1, 'name': '测试', 'age': 15}, {'id': 2, 'name': '老王', 'age': 10},
            {'id': 3, 'name': '李四', 'age': 20}]
    for i in data:
        i_data = (i['id'], i['name'], i['age'])
        insert_res = om.insert_data(
            """
             INSERT INTO test_student (id,name,age) VALUES (%s,%s,%s)
            """, i_data
        )
        print(insert_res)

    # 查询
    one_data = om.select_first_data(
        """
            SELECT * FROM test_dome;
        """
    )
    # all_data = om.select_all_data(
    #     """
    #     SELECT * FROM test_student;
    #     """
    # )
    print(one_data)
    # # all_data字符串类型的list转list
    # print("查询总数据:%s", len(json.loads(all_data)), "分别是:%s", all_data)
    #
    # # 修改
    # update_data = om.update_data(
    #     """
    #     UPDATE test_student SET name = '王五' WHERE id = 1;
    #     """
    # )
    # print(update_data)
    #
    # # 删除
    # del_data = om.del_data(
    #     """
    #     DELETE FROM test_student WHERE id in (1,2,3);
    #     """
    # )
    # print(del_data)

    # 关闭游标
    om.conn_close()
