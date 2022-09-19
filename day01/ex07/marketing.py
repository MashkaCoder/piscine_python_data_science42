import sys

def call_center() -> list:
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    res = list(set(clients) - set(recipients))
    return res

def potential_clients() -> list:
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    res = list(set(participants) - set(clients))
    return res

def loyalty_program() -> list:
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    res = list(set(clients) - set(participants))
    return res

def main(search: str) -> None:
    if search == "call_center":
        call = call_center()
        print(call)
    elif search == "potential_clients":
        potential = potential_clients()
        print(potential)
    elif search == "loyalty_program":
        loyalty = loyalty_program()
        print(loyalty)
    else:
        raise ValueError("Wrong name")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            main(sys.argv[1])
        except ValueError as e:
            print(e)