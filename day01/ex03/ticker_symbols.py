import sys

def search_by_value_and_by_key(search:str):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    str = ''
    if search.upper() not in STOCKS:
        return ("Unknown ticker")
    else:
        num = STOCKS[search.upper()]
        for key,value in COMPANIES.items():
            if value == search.upper():
                str = key
    return str, num


def main():
    if len(sys.argv) == 2:
        res = search_by_value_and_by_key(sys.argv[1])
        if len(res) == 2:
            print(res[0], res[1])
        else:
            print(res)

if __name__ == "__main__":
    main()