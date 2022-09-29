import timeit

def loop(email:list):
    res = []
    for i in email:
        if i.endswith('@gmail.com'):
            res.append(i)
    return res


def list_comprehension(emails: list):
    res = [i for i in emails if i.endswith('@gmail.com')]
    return res


def main() -> None:
    loop_time = timeit.timeit(stmt='loop(emails)', setup='from __main__ import emails, loop', number=9000000)
    list_time = timeit.timeit(stmt='list_comprehension(emails)', setup='from __main__ import emails, list_comprehension', number=9000000)
    if loop_time < list_time:
        print("it is better to use a loop")
        print(loop_time, 'vs', list_time)
    else:
        print("it is better to use a list comprehension")
        print(list_time, 'vs', loop_time)


if __name__ == "__main__":
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']*5
    main()

