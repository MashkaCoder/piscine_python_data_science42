import timeit
import random
from collections import Counter


def loop(num: int) -> int:
    res = 0
    for i in range(abs(num)+1):
        res += i*i
    return res


def reduce_help(pre_sum: int, num: int):
    return pre_sum + num*num


def create_dict(list_ran: list) -> dict:
    key = set(list_ran)
    res = dict.fromkeys(key, 0)
    for key in list_ran:
        res[key] += 1
    return res


def my_top(list_ran: list) -> dict:
    dictic = create_dict(list_ran)
    sort_tup = sorted(dictic.items(), key=lambda x: -x[1])
    sort_dic = dict(sort_tup)
    top = {}
    i = 10
    while i > 0:
        try:
            key, value = sort_dic.popitem()
        except KeyError:
            break
        else:
            top[key] = value
            i -= 1
    return top


def main() -> None:
    print("my function:", timeit.timeit(stmt='create_dict(list_rand)', setup='from __main__ import list_rand, create_dict', number=1))
    print("Counter:", timeit.timeit(stmt='Counter(list_rand)', setup='from __main__ import list_rand, Counter', number=1))
    print("my top:", timeit.timeit(stmt='my_top(list_rand)', setup='from __main__ import list_rand, my_top', number=1))
    print("Counter's top:", timeit.timeit(stmt='Counter(list_rand).most_common(10)', setup='from __main__ import list_rand, Counter', number=1))


if __name__ == "__main__":
    list_rand = [random.randint(0, 100) for i in range(1000000)]
    main()
