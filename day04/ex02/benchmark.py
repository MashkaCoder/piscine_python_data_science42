import timeit
import sys


def loop(email: list) -> list:
    res = []
    for i in email:
        if i.endswith('@gmail.com'):
            res.append(i)
    return res


def list_comprehension(email: list) -> list:
    res = [i for i in email if i.endswith('@gmail.com')]
    return res


def help_fun(email: str) -> str:
    if email.endswith('@gmail.com'):
        return email


def map_list(email: list) -> map:
    res = map(help_fun, email)
    return res


def filter_list(email: list) -> filter:
    res = filter(help_fun, email)
    return res


def main() -> None:
    available_func = ['loop', 'list_comprehension', 'map', 'filter']
    if sys.argv[1] not in available_func:
        print("Wrong func, available_func:", available_func)
        return
    else:
        if sys.argv[1] == 'map':
            f = 'map_list'
        elif sys.argv[1] == 'filter':
            f = 'filter_list'
        else:
            f = sys.argv[1]
    try:
        int(sys.argv[2])
    except ValueError as e:
        raise e
    stm = f"{f}(emails)"
    set_up = f"from __main__ import emails, {f}"
    print(timeit.timeit(stmt=stm, setup=set_up, number=int(sys.argv[2])))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']*5
            main()
        except ValueError as e:
            print(e)
    else:
        print("Usage: python3 benchmark.py (func) (count)")