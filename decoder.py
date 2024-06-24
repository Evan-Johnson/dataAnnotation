def decode(message_file):
    file = open(message_file, 'r')

    with open(message_file, 'r') as file:
        lines = file.readlines()
    # lines = ['3 love', '6 computers', '2 dogs', '4 cats', '1 i', '5 you']
    sortedList = getNums(lines)

    pyramid = makePyramid(sortedList)

    getWords = findEnd(pyramid, sortedList)

    return ' '.join(getWords)
    

def getNums(lines):
    nums_wrds = []
    for line in lines:
        number, word = line.strip().split()
        nums_wrds.append((int(number), word))
    
    nums_wrds.sort()
    return nums_wrds

def makePyramid(sortedList):
    n = 1
    end_index = []
    while len(end_index) == 0 or end_index[-1] < len(sortedList):
        if len(end_index) == 0:
            end_index.append(n)
        else:
            end_index.append(end_index[-1] + n)

        n += 1

    return end_index

def findEnd(pyramid, sortedList):
    words = []
    for index in pyramid:
        if index <= len(sortedList):
            words.append(sortedList[index-1][1])

    return words

message = decode('coding_qual_input.txt')
print(message)