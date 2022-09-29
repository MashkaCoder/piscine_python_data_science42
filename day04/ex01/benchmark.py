import timeit


def loop(email: list) -> list:
    res = []
    for i in email:
        if i.endswith('@gmail.com'):
            res.append(i)
    return res


def list_comprehension(email: list) -> list:
    res = [i for i in email if i.endswith('@gmail.com')]
    return res


def help_map(email: str) -> str:
    if email.endswith('@gmail.com'):
        return email


def map_list(email: list) -> map:
    res = map(help_map, email)
    return res


def main() -> None:
    loop_time = timeit.timeit(stmt='loop(emails)', setup='from __main__ import emails, loop', number=900000)
    list_time = timeit.timeit(stmt='list_comprehension(emails)', setup='from __main__ import emails, list_comprehension', number=900000)
    map_time = timeit.timeit(stmt='map_list(emails)', setup='from __main__ import emails, map_list', number=900000)
    min_time = min(loop_time, map_time, list_time)
    sort_time = sorted([loop_time, list_time, map_time])
    if min_time == loop_time:
        type = "loop"
    elif min_time == list_time:
        type = 'list comprehension'
    else:
        type = 'map'
    print(f"it is better to use a {type}")
    print(sort_time[0], 'vs', sort_time[1], 'vs', sort_time[2])


if __name__ == "__main__":
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']*5
    main()


