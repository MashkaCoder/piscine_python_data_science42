import sys

def search_by_key(company: str) -> str:
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
    comp = ''
    for val in COMPANIES:
        if company.capitalize() == val:
            comp = COMPANIES[val]
    if comp == '':
        return "Unknown company"
    for val in STOCKS:
        if comp == val:
            return STOCKS[val]

def main():
    if len(sys.argv) == 2:
        print(search_by_key(sys.argv[1]))


if __name__ == "__main__":
    main()