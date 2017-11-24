# /usr/bin/env python
# -*- encoding: utf-8 -*-

# MySQLdb use in python2, not in python3
# python 2/3 use pymysql or mysqlclient

import pymysql
from copy import deepcopy

from datetime import datetime

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 3306
DEFAULT_CHARSET = 'utf8m64'
DEFAULT_CURSOR_CLASS = pymysql.cursors.DictCursor


class MysqlWrapper(object):
    def __init__(self, **kwargs):
        self.config = deepcopy(kwargs)
        self._set_default_config()
        self.connection = pymysql.connect(**self.config)

    def _set_default_config(self):
        self.config.setdefault('host', DEFAULT_HOST)
        self.config.setdefault('port', DEFAULT_PORT)
        # self.config.setdefault('charset', DEFAULT_CHARSET)
        self.config.setdefault('cursorclass', DEFAULT_CURSOR_CLASS)

    def conn(self):
        return self.connection

    def close(self):
        self.connection.close()


def query_test(**conf):
    mywrapper = MysqlWrapper(**conf)
    conn = mywrapper.conn()
    try:
        with conn.cursor() as cursor:
            sql = 'select user_id, user, pass, time from table1'
            cursor.execute(sql)
            # result = cursor.fetchone()
            # result = cursor.fetchall()
            result = cursor.fetchmany(3)
            print(result)
    except:
        pass
    finally:
        conn.close()


def insert_test(**conf):
    mywrapper = MysqlWrapper(**conf)
    conn = mywrapper.conn()
    try:
        with conn.cursor() as cursor:
            sql = 'insert into table1 (user_id, user, pass, time) values (%(user_id)s, %(user)s, %(pass)s, %(time)s)'
            sql_value = {
                'user_id': 22,
                'user': 'bian22',
                'pass': 'bian22pass',
                'time': datetime.now()
                # 'time': datetime.now()
            }

            cursor.execute(sql, sql_value)
            conn.commit()
    except:
        pass
    finally:
        conn.close()


if __name__ == '__main__':
    conf = {
        'host': '10.99.70.38',
        'user': 'root',
        'password': 'root',
        'db': 'test1'
    }
    # query_test(**conf)
    # insert_test(**conf)

    print(str(datetime.now()))