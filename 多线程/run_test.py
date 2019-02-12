# encoding: utf-8
import sys

import datetime

from jobs import test_job, test_get_url

PY3 = sys.version_info[0] == 3

if PY3:
    import concurrent.futures as futures
else:
    import concurrent.futures as futures


def PoolExecutor(*args, **kwargs):
    all_times = 0
    success_times = 0
    fail_times = 0
    pool_executor = futures.ProcessPoolExecutor
    if kwargs.get('pool_type', None) == 'process':
        pass
    elif kwargs.get('pool_type', None) == 'thread':
        pool_executor = futures.ThreadPoolExecutor

    max_workers = kwargs.get('max_workers', None)
    # max_workers = int(max_workers) if max_workers else None

    run_times_per_worker = kwargs.get('run_times_per_worker', 1)

    job_args = list(kwargs.get('job_args', []))

    start_time = datetime.datetime.now()

    all_execute_time = 0
    success_execute_time = 0

    with pool_executor(max_workers=max_workers) as executor:
        executor_dict = dict((executor.submit(kwargs.get('job_name'), *(job_args[times])), times+1)
                             for times in range(len(job_args)))
        # print(executor_dict)
        for future in futures.as_completed(executor_dict):
            times = executor_dict[future]
            if future.exception() is not None:
                print('times: %s, generated an exception: %s, args: %s' % (times, future.exception(), job_args[times-1]))
                fail_times += 1
            elif not future.result()[2]:
                print('times: %s, has an failed result: %s, args: %s' % (times, future.result(), job_args[times-1]))
                fail_times += 1
            else:
                print("times: %s, success. args: %s, res: %s" % (times, job_args[times-1], future.result()))
                success_times += 1
                success_execute_time += future.result()[1][0] * 1000 * 1000 + future.result()[1][1]
            all_times += 1

        future = executor.submit(kwargs.get('job_name'), "sds")
        print(future.result())
        print('all times: %s' % all_times)
        print('success times: %s' % success_times)
        print('fail times: %s' % fail_times)

        print('average success job execute time: %s microseconds' % (success_execute_time/success_times))

    end_time = datetime.datetime.now()
    print("all job execute time: %s seconds" % (end_time-start_time).seconds)


def PoolExecutor2(*args, **kwargs):
    pool_executor = futures.ProcessPoolExecutor
    if kwargs.get('pool_type') == 'process':
        pass
    elif kwargs.get('pool_type') == 'thread':
        pool_executor = futures.ThreadPoolExecutor

    max_workers = kwargs.get('max_workers', None)
    max_workers = int(max_workers) if max_workers else None

    run_times = kwargs.get('run_times_per_worker', 1)
    run_times2 = max_workers if max_workers else 4

    with pool_executor(max_workers=max_workers) as executor:
        executor_dict = dict((executor.submit(kwargs.get('job_name'), times), times + 10) for times in range(run_times * run_times2))
        print(executor_dict)
        for future in futures.as_completed(executor_dict):
            times = executor_dict[future]
            if future.exception() is not None:
                print('%r generated an exception: %s' % (times, future.exception()))
            else:
                print("runtime: %s, res: %s"%(times, future.result()))

        future = executor.submit(kwargs.get('job_name'), "sds")
        print(future.result())


def ThreadExecutor(*args, **kwargs):
    max_workers = kwargs.get('max_workers', None)
    max_workers = int(max_workers) if max_workers else None

    with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future = executor.submit(kwargs.get('job_name'), "sds")
        print(future.result())


def ThreadExecutor2(*args, **kwargs):
    max_workers = kwargs.get('max_workers', None)
    max_workers = int(max_workers) if max_workers else None

    data = [1, 2, 4, 5, 6, 7, 8, 10]
    with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for future in executor.map(kwargs.get('job_name'), data):
            print(future)


def ProcessExecutor(*args, **kwargs):
    max_workers = kwargs.get('max_workers', None)
    max_workers = int(max_workers) if max_workers else None

    with futures.ProcessPoolExecutor as executor:
        pass


if __name__ == "__main__":

    list_size = 10000
    list_many_of_args = [['arg1', i+1] for i in range(list_size)]
    exec_dict = {
        # 'pool_type': 'thread',
        'pool_type': 'process',
        'max_workers': 1,
        'run_times_per_worker': 4,
        'job_name': test_get_url,
        # 'job_name': testjob,
        'job_args': list_many_of_args
    }
    PoolExecutor(**exec_dict)
    # ThreadExecutor(**exec_dict)
    # ThreadExecutor2(**exec_dict)
