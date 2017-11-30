


### 测试结果
linux 4核8G

#### concurrent.futures 中的 ProcessPoolExecutor 和 ThreadPoolExecutor
    max_workers=4, 执行10000次job(调用GET请求, 毫秒级别)。
    ProcessPoolExecutor 用时11s
    ThreadPoolExecutor 用时36s

#### ProcessPoolExecutor 的 max_workers 不同
    执行10000次job(调用GET请求, 毫秒级别)。
    max_workers=1,      总用时 40s     每个任务用时 4220 microseconds
    max_workers=2,      总用时 19s     每个任务用时 4312 microseconds
    max_workers=3,      总用时 14s
    max_workers=4,      总用时 11s     每个任务用时 4681 microseconds
    max_workers=None,   总用时 11s
    max_workers=5,      总用时 10s
    max_workers=6,      总用时 9s
    max_workers=7,      总用时 9s
    max_workers=8,      总用时 8s      每个任务用时 6987 microseconds
    max_workers=10,     总用时 8s
    max_workers=20,     总用时 8s
    max_workers=100,    总用时 8s      每个任务用时 76758 microseconds
    
> 可以看出: 对于4核的机器，max_workers约为8及以后，性能不再提升。
> 但是，对于一个任务的执行， 在max_workers大于4以后，消耗时间逐渐增加。
> 结论: 对于ProcessPoolExecutor， max_workers可以设置为cpu核数的一到两倍。既可以保证总的时间较短，每个任务的执行时间也不会有明显增加。
