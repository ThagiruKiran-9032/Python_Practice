age = 25
has_ticket = True
is_banned = False

if age >= 18 and has_ticket:
    print("and: The customer can enter")

if age < 18 or not has_ticket:
    print("or: The customer needs permission or a ticket")
else:
    print("or: The customer passes the basic check")

if not is_banned:
    print("not: The customer is not banned")
