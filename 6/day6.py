with open('input') as f:
    packet = f.read()

def find_first_marker(distinct_characters):
    characters = []
    for i, character in enumerate(packet):

        try:
            index = characters.index(character)
            characters = characters[index+1:]
            characters.append(character)

        except ValueError:
            characters.append(character)

        if len(characters) == distinct_characters:
            break
    return i + 1


print(find_first_marker(4))
print(find_first_marker(14))
