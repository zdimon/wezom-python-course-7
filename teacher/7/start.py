# question = [
#     "Какой оператор вывода на экран?",
#     "Какой оператор цикла?"
# ]

# options = [
#     ["echo", "write", "print"],
#     ["for", "loop", "fuck"]
#     ]



questions = [
     {
         "question":"Какой оператор вывода на экран?", "answers": [
         {"text":"echo", "is_right": False}, 
         {"text":"write", "is_right": False}, 
         {"text":"print", "is_right": True}
         ]},
     
    {
        "question":"Какой оператор цикла?", "answers": [
         {"text":"echo", "is_right": False}, 
         {"text":"write", "is_right": False}, 
         {"text":"print", "is_right": True}        
    ]}
 ]



for q in questions:
    print(q["question"])
    q["do"]()
    cnt = 1
    for opt in q["answers"]:
        #print(str(cnt) + ' '+opt["text"]) 
        print(f'{cnt}. {opt["text"]}') 
        cnt = cnt + 1
    answer = int(input())
    if q["answers"][answer-1]["is_right"]:
        print('yes')
        # import pdb; pdb.set_trace()
    else:
        print('no')

