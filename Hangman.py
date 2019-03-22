#import the random word
from random_word import RandomWords

r=RandomWords()
word = str.upper(r.get_random_word(hasDictionaryDef="true",minCorpusCount=5000 ))
wordlen = len(word)

#build the hangman board
hangman = {1:'_____', 2: '|    |', 3: '|' , 4: '|' , 5: '|', 6: '|'}

#hangman wrong guess changes to the board
hangmanWrong = {1: '|    0', 2: '|    |',3:'|   /|',4: '|   /|\\',5: '|   /',6:'|   / \\'}

#losing board
endGame = {1:'_____', 2: '|    |', 3: '|    0' , 4: '|   /|\\' , 5: '|   / \\', 6: '|'}

#display the board
def theBoard():
    print(hangman[1])
    print(hangman[2])
    print(hangman[3])
    print(hangman[4])
    print(hangman[5])
    print(hangman[6])

#build the spaces under the board
#create a list with the number of spaces equal to the number of letters in the word
disword = 0
spaces = []
for characters in word:
    space = [' ___ ']
    disword = disword + 1
    spaces = space + spaces

#display the spaces from the list as a string
def printspaces():
    spacecount = 0
    spaceprint = ''
    for items in spaces:
        if spaces[spacecount] == '___':
            makespace = spaces[spacecount]
            spaceprint = spaceprint + makespace
        else:
            makespace = spaces[spacecount]
            spaceprint = spaceprint + makespace
            spacecount = spacecount + 1
    print(spaceprint)


    
#start the game, display the board and spaces
theBoard()
print('\n \n')
printspaces()

#prompt the user for a letter
guessno = 3
guesswrong = 1
while True:
    #end the game if the man has been hanged
    if hangman == endGame:
        print('\n' +'You have lost.  Sorry!')
        print('The word was ' + word)
        break
    #if there are no more spaces the game has been won
    elif str(' ___ ') not in spaces:
        print('You have won.  Congratulations!')
        break
    elif hangman != endGame:
        guess = str.upper(input('Please pick a letter: '))
        #validate for 1 letter guess
        if len(guess) > 2:
            print('Please only enter 1 letter')
        #wrong guess, fill the board in with body parts in sequence
        elif guess not in word:
            #for rows on the board with multiple possible positions (arms, legs)
            #replace the dictionary item with each body part in order
            if (guesswrong >= 2 and guesswrong <=3) or guesswrong == 5:
                hangman[guessno] = hangmanWrong[guesswrong]
                guesswrong = guesswrong + 1
                theBoard()
                print('\n \n')
                printspaces()
            else:
                hangman[guessno] = hangmanWrong[guesswrong]
                guesswrong = guesswrong + 1
                guessno = guessno + 1
                theBoard()
                print('\n \n')
                printspaces()
        elif guess in word:
            letterCount = word.count(guess)
            #if there is only one instance of the letter, add to spaces with the letter in place
            if letterCount < 2:
                result = word.find(guess)
                newSpace = ' _'+word[result]+'_ '
                spaces[result] = newSpace
                theBoard()
                print('\n \n')
                printspaces()
            #if there are more than one instance of a letter, find the positions of the letter, for each position replace 'spaces' with that letter
            elif letterCount > 1:
                occurrences = word.count(guess)
                indices = [i for i, a in enumerate(word) if a == guess]
                letterFill = []
                indicesIndex = 0
                for letter in indices:
                   newSpace = ' _'+word[indices[indicesIndex]]+'_ '
                   spaces[indices[indicesIndex]] = newSpace
                   indicesIndex = indicesIndex + 1
                theBoard()
                print('\n \n')
                printspaces()
        
            
        








