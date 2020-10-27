import shelve

with shelve.open("word_count_data") as word_count_shelf:

    # items = [(v, k) for k, v in word_count_shelf.items()]
    # items.sort()
    # items.reverse()  # so largest is first
    # items = [(k, v) for v, k in items]
    #
    # print(items)

    for item in word_count_shelf:
        try:
            print(item + " " + str(word_count_shelf.get(item)))
        except EOFError:
            print(item + " What the fuckasdf")