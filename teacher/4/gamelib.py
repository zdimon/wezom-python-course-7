
def make_deck():
    deck = []
    faces = ["diamond", "heart", "spade", "clubs"]
    ranks = [2,3,4,5,6,7,8,9,10]
    for face in faces:
        for rank in ranks:
            name = '%s-%s.png' % (face,rank)
            card = {
                "name": name,
                "rank": rank
            }
            deck.append(card)
    return deck


