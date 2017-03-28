def hapax_legomena(ranking):
    return [word for word, frequency in ranking if frequency == 1]


def half_of_text(ranking):
    size = sum([frequency for _, frequency in ranking])

    counter = 0
    words = []
    for word, frequency in ranking:
        words.append(word)
        if counter + frequency > size / 2:
            break
        counter += frequency

    return words
