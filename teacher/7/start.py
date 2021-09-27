# question = [
#     "Какой оператор вывода на экран?",
#     "Какой оператор цикла?"
# ]

# options = [
#     ["echo", "write", "print"],
#     ["for", "loop", "fuck"]
#     ]

questions = [
     {"question":"Какой оператор вывода на экран?", "answers": [
         {"text":"echo", "is_right": False}, 
         {"text":"write", "is_right": False}, 
         {"text":"print", "is_right": True}
         ]},
     
    {"question":"Какой оператор цикла?", "answers": [
         {"text":"echo", "is_right": False}, 
         {"text":"write", "is_right": False}, 
         {"text":"print", "is_right": True}        
    ]}
 ]




for q in questions:
    print(q["question"])
    for opt in q["answers"]:
        print(opt["text"]) 
    answer = input()

