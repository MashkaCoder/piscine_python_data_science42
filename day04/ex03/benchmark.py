from functools import reduce
import timeit
import sys


def loop(num: int) -> int:
    res = 0
    for i in range(abs(num)+1):
        res += i*i
    return res


def reduce_help(pre_sum: int, num: int):
    return pre_sum + num*num


def reduce_sum(num: int) -> int:
    res = reduce(reduce_help, [i for i in range(abs(num) + 1)])
    return res


def main() -> None:
    available_func = ['loop', 'reduce']
    if sys.argv[1] not in available_func:
        print("Wrong func, available_func:", available_func)
        return
    else:
        if sys.argv[1] == 'reduce':
            f = 'reduce_sum'
        else:
            f = sys.argv[1]
    if int(sys.argv[2]) < 0:
        raise TypeError("The number must be positive")
    stm = f"{f}(n)"
    set_up = f"from __main__ import n, {f}"
    print(timeit.timeit(stmt=stm, setup=set_up, number=int(sys.argv[2])))


if __name__ == "__main__":
    if len(sys.argv) == 4:
        try:
            n = int(sys.argv[3])
            int(sys.argv[2])
            main()
        except ValueError as e:
            print(e)
    else:
        print("Usage: python3 benchmark.py (func) (count)")
