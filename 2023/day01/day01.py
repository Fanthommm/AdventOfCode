import re

def writtenToInt(string):
    writtenNumbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    numDict = list(zip(range(0,10), writtenNumbers))

    for num in numDict:
        while num[1] in string:
            index = string.find(num[1])
            string = list(string)
            string[index] = string[index]+str(num[0])
            string = "".join(string)

    return string

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    total = 0
    i=0
    for word in lines:
        i+=1
        word = word.rstrip()

        # PART 1:
        # word = re.findall("\d", word)

        # PART 2:
        newWord = writtenToInt(word)
        print(f"{word} > {newWord}")
        
        word = re.findall("\d", newWord)

        if len(word) == 1:
            num = word[0]
            num += num
        else:
            num = ""
            num += word[0]
            num += word[-1]

        print(f"Number n°{i} : {num}")
        total += int(num)

    print(f"TOTAL = {total}")    

main()
