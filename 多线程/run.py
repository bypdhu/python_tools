# encoding: utf-8

import datetime

from jobs import test_job, test_get_url
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
    run_times_per_worker = kwargs.get('run_times_per_worker', 1)
    job_args = list(kwargs.get('job_args', []))

    start_time = datetime.datetime.now()
    all_execute_time = 0
    success_execute_time = 0

    with pool_executor(max_workers=max_workers) as executor:
        executor_dict = dict((executor.submit(kwargs.get('job_name'), *(job_args[times])), times + 1)
                             for times in range(len(job_args)))
        # print(executor_dict)
        for future in futures.as_completed(executor_dict):
            times = executor_dict[future]
            if future.exception() is not None:
                print('times: %s, generated an exception: %s, args: %s'
                      % (times, future.exception(), job_args[times - 1]))
                fail_times += 1
            elif not future.result()[2]:
                print('times: %s, has an failed result: %s, args: %s' % (times, future.result(), job_args[times - 1]))
                fail_times += 1
            else:
                print("times: %s, success. args: %s, res: %s" % (times, job_args[times - 1], future.result()))
                success_times += 1
                success_execute_time += future.result()[1][0] * 1000 * 1000 + future.result()[1][1]
            all_times += 1

        future = executor.submit(kwargs.get('job_name'), "sds")
        print(future.result())
        print('all times: %s' % all_times)
        print('success times: %s' % success_times)
        print('fail times: %s' % fail_times)

        print('average success job execute time: %s microseconds' % (success_execute_time / success_times))

    end_time = datetime.datetime.now()
    print("all job execute time: %s seconds" % (end_time - start_time).seconds)


def run_job_with_pool_executor():
    list_size = 10000
    list_many_of_args = [['arg1', i + 1] for i in range(list_size)]
    exec_dict = {
        # 'pool_type': 'thread',
        'pool_type': 'process',
        'max_workers': 1,
        'run_times_per_worker': 4,
        'job_name': test_get_url,
        # 'job_name': test_job,
        'job_args': list_many_of_args
    }
    PoolExecutor(**exec_dict)


if __name__ == "__main__":
    run_job_with_pool_executor()
