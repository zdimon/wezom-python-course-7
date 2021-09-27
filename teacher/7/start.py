# question = [
#     "Какой оператор вывода на экран?",
#     "Какой оператор цикла?"
# ]

# options = [
#     ["echo", "write", "print"],
#     ["for", "loop", "fuck"]
#     ]

questions = [
     {"question":"Какой оператор вывода на экран?", "answers": ["echo", "write", "print"]},
     
    {"question":"Какой оператор цикла?", "answers": ["for", "loop", "fuck"]}
 ]




for q in questions:
    print(q["question"])
    for opt in q["answers"]:
        print(opt) 
    answer = input()

