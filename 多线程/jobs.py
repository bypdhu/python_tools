# encoding: utf-8
import datetime
import requests
import time

def testjob(*args):
    start_time = datetime.datetime.now()
    time.sleep(2)
    print(args)
    end_time = datetime.datetime.now()

    return args, [(end_time - start_time).seconds, (end_time - start_time).microseconds], True
    # return time.ctime(), args, (end_time - start_time).seconds


def test_get_url(*args):
    start_time = datetime.datetime.now()

    url = 'http://10.99.70.52:5555/health'
    res = requests.get(url)

    res_code = res.status_code == 200
    end_time = datetime.datetime.now()
    # if res.status_code != 200:
    #     raise Exception
    return args, [(end_time - start_time).seconds, (end_time - start_time).microseconds], res_code
