from django.shortcuts import render


questions = [
     {
         "name": "q1",
         "question":"Какой оператор вывода на экран?", "answers": [
         {"text":"echo", "is_right": False}, 
         {"text":"write", "is_right": False}, 
         {"text":"print", "is_right": True}
         ]},
     
    {
        "name": "q2",
        "question":"Какой оператор цикла?", "answers": [
         {"text":"echo", "is_right": False}, 
         {"text":"write", "is_right": False}, 
         {"text":"print", "is_right": True}        
    ]}
 ]

def index(request):
    return render(request,'index.html',{"questions": questions})


def check(request):
    #print(request.POST['q1'])
    for q in questions:
        print(request.POST[q["name"]])
        if q["answers"][int(request.POST[q["name"]])-1]["is_right"]:
            print("yes")
        else:
            print("no")
    return render(request,'check.html')