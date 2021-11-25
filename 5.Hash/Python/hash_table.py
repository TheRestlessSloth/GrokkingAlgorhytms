import random as rnd

book = dict()
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book)

print(book["avocado"])

phone_book = {}
phone_book["jenny"] = 8675309
phone_book["emergency"] = 911
print(phone_book["jenny"])

voted = {}
voted["tom"] = 10 ##Uncomment to see

value = voted.get("tom")
print(value)

def check_voter(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote")

check_voter("tom")
check_voter("mike")
check_voter("mike")

cache = {}
def get_page(url):
    if cache.get(url):
        print("getting fr cache")
        return cache[url]
    else:
        print("getting fr server")
        data = get_data_from_server(url)
        cache[url] = data
        return data

def get_data_from_server(url):
    data = url + "hehe"
    return data

a = get_page("vk.com")
print(a)
b = get_page("vk.com")
print(b)

#Exercises
#1
phone_book["Esther"] = rnd.randint(70000000,79999999)
phone_book["Ben"] = rnd.randint(70000000,79999999)
phone_book["Bob"] = rnd.randint(70000000,79999999)
phone_book["Dan"] = rnd.randint(70000000,79999999)

print(phone_book)

#2
battery_size = dict()
battery_size["A"] = 1.5
battery_size["AA"] = 1.5
battery_size["AAA"] = 1.5
battery_size["AAAA"] = 1.5
battery_size["B"] = 1.5
battery_size["C"] = 1.5
battery_size["D"] = 1.5
battery_size["3LR12"] = 4.5
battery_size["A23"] = 12
battery_size["PP3"] = 9
battery_size["CR2023"] = 3
battery_size["LR44"] = 1.5

print(battery_size)

#3
authors_book = dict()
authors_book("Maus") = "Art Spiegelman"
authors_book("Fun Home") = "Alison Bechdel"
authors_book("Watchmen") = "Alan Moore"