import json

def read_db():
    with open('users.json', 'r') as f:
        content_str=f.read()
    content_obj = json.loads(content_str)
    return content_obj


def write_db(content_obj):
    content_str = json.dumps(content_obj)
    with open('users.json', 'w') as f:
        f.write(content_str)  

def add_user(username,chat_id):
    db = read_db()
    проверять
    write_db(db)