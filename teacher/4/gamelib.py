
def make_deck():
    deck = []
    faces = ["0", "1", "2", "3"]
    ranks = [2,3,4,5,6,7,8,9,10]
    for face in faces:
        for rank in ranks:
            name = '%s_%s.svg' % (face,rank)
            card = {
                "name": name,
                "rank": rank
            }
            deck.append(card)
    return deck


