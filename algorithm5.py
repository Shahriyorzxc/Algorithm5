#1
def rangeOfnum(start, end):
    return list(range(start + 1, end))


print(rangeOfnum(2,4))
print(rangeOfnum(5,9))
print(rangeOfnum(2,11))


#2
def isFourLetters(words):
    result = []
    for word in words:
        if len(word) == 4:
            result.append(word)
    return result


print(isFourLetters(["Tomato", "Potato", "Pair"]))
print(isFourLetters(["Kangaroo", "Bear", "Fox"]))
print(isFourLetters(["Ryan", "Kieran", "Jason", "Matt"]))


#3
def firstLast(lst):
    return [lst[0], lst[-1]]


print(firstLast([5, 10, 15, 20, 25]))
print(firstLast(["edabit", 13, "null", "false", "true"]))
print(firstLast(["undefiend", 4, "6", "hello", "null"]))


#4
def get_budgets(lst):
    person_total_budget = 0
    for person in lst:
        person_total_budget += person['budget']
    return person_total_budget


budgetss1 = [
{"name": "John", "age": 21, "budget": 23000 },
{"name": "Steve", "age": 32, "budget": 40000 },
{"name": "Martin", "age": 16, "budget": 2700 }
]

budgetss2 = [
{"name": "John", "age": 21, "budget": 29000 },
{"name": "Steve", "age": 32, "budget": 32000 },
{"name": "Martin", "age": 16, "budget": 1600 }
]

print(get_budgets(budgetss1))
print(get_budgets(budgetss2))
