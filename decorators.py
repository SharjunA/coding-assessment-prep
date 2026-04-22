def security_guard(func):
    def wrapper(person):
        if person == 'VIP':
            print("Access granted to VIP.")
            func(person)
        else:
            print("Access denied. Only VIPs are allowed.")
    return wrapper

@security_guard
def enter_party(person):
    print(f"🎉 Welcome to the party, {person}!")

@security_guard
def enter_pool(person):
    print(f"🏊 Enjoy the pool, {person}!")