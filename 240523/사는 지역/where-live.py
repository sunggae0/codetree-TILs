class Person:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

def get_person_with_latest_name(people):
    # Sort the people by name in descending order
    people.sort(key=lambda x: x.name, reverse=True)
    # The person with the latest name will be the first after sorting
    return people[0]

# Read the number of people
n = int(input())

# Read the details of each person
people = []
for _ in range(n):
    details = input().split()
    name = details[0]
    addr = details[1]
    city = details[2]
    person = Person(name, addr, city)
    people.append(person)

# Get the person with the latest name
latest_person = get_person_with_latest_name(people)

# Print the details of the person with the latest name
print(f"name {latest_person.name}")
print(f"addr {latest_person.addr}")
print(f"city {latest_person.city}")