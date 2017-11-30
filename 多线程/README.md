


### 测试结果
linux 4核8G

#### concurrent.futures 中的 ProcessPoolExecutor 和 ThreadPoolExecutor
    max_workers=4, 执行10000次job(调用GET请求, 毫秒级别)。
    ProcessPoolExecutor 用时11s
    ThreadPoolExecutor 用时36s

#### ProcessPoolExecutor 的 max_workers 不同
    执行10000次job(调用GET请求, 毫秒级别)。
    max_workers=1,      用时 40s
    max_workers=2,      用时 19s
    max_workers=3,      用时 14s
    max_workers=4,      用时 11s
    max_workers=None,   用时 11s
    max_workers=5,      用时 10s
    max_workers=6,      用时 9s
    max_workers=7,      用时 9s
    max_workers=8,      用时 8s
    max_workers=10,     用时 8s
    max_workers=20,     用时 8s
    max_workers=100,    用时 8s
    
> 可以看出: 对于4核的机器，max_workers约为8及以后，性能不再提升。
> 结论: 对于ProcessPoolExecutor， max_workers可以设置为cpu核数的两倍。