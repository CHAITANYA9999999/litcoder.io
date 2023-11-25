def NoPrefixSet(words):
    word_list = words.split(' ')
    word_list.sort()
    isGood = True
    for i in range(len(word_list)-1):
        length = len(word_list[i])
        for j in range(i+1, len(word_list)):
            if word_list[j][:length] != word_list[i]:
                continue
            else:
                if word_list[j]==word_list[i]:
                    continue
                else:
                    isGood = False
                    break
    print('good' if isGood else 'bad')