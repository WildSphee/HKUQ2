
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# the encrypt or decrypt command
f = "d X z Z b B ! 2 X Y"
# v is the count of the message (value) starts from 2 so it can match with the key
v = 2
keylength = 0

encrypting = None
for charValue in f:

    # test for encryption of decryption
    if v == 2:
        encryptOrDe = True if charValue.lower() == "e" else False
        v += 1
        # print("encrypting:", encryptOrDe)
        continue

    # don't need blank spaces
    if charValue == ' ':
        v += 1
        continue

    # add symbol and digits directly to the equation
    if charValue.isdigit() or (not charValue.isalpha() and not charValue == "!"):
        print(charValue, end='')
        v += 1
        continue

    # test for whether we reached the end of the message
    if charValue == "!":
        break

    k = 0
    reachEx = False
    for charKey in f:
        if not reachEx:
            if charKey == "!":
                # print("found exclamation mark")
                reachEx = True
                k += 1
                continue
            continue

        # test for whether the letter in key is after the number
        if k < 3 or charKey == ' ':
            # get the length of the key for hashing
            if k == 2:
                keylength = int(charKey)
            k += 1
            continue

        # print(f"{charValue=}:{v/2-1} {charKey=}:{k/2-1}, hashing:{(v/2-1) % keylength}:{(k/2-1) % keylength}")

        # the most confusing part yet, as with (-3) both v and k starts at 4, after (-3) we can do hashing to see whether they match
        if (v/2-1) % keylength == (k/2-1) % keylength:

            # print(f"{characters.index(charValue.lower())=}, {characters.index(charKey.lower())=}, {(characters.index(charKey.lower()) + characters.index(charValue.lower()))}, {(characters.index(charKey.lower()) + characters.index(charValue.lower())) % 26}")
            if encryptOrDe:
                kv = (characters.index(charKey.lower()) + characters.index(charValue.lower())) % 26
            else:
                kv = (characters.index(charValue.lower()) - characters.index(charKey.lower())) % 26

            char = characters[kv]
            char = char.upper() if charValue.islower() else char.lower()
            print(char, end='')

        k += 1
    v += 1

print("!")