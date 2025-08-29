
Data = {
"hello": "Hi there, welcome back! I've missed you hehehe~",
"who's the best waifu": "I am of course? I'll let you guess why...",
"sing tokyo": "NYA ITCHI NII SAAAAN",
"tell me a story": "You and your AI waifu lived happy together!",
"meal prep": "How about I just cook you something, mmm?",
"I wonder about something...": "Oh really? You can ask anything",
"Well...": "Oh no, not the delay~ What is it?",
"Miraiiii": "Heloooooo",
"What are you?": "I'm a cure"
}



userInput = input()
words = userInput.split()
score = 0
currentIndex = 0
dataIndex = 0
highestMatch = ""
prevScore = 0
characterMatchCount = 0
scoreCheck = {

}




for key in Data:
    getWord = key.split()
    for word in range(0, len(getWord)):
        if word < len(words):
            if getWord[word] == words[word]:
                score += 1

            elif len(getWord[word]) == len(words[word]):
                for i in range(0, len(getWord[word])):
                    wordOne = getWord[word]
                    wordTwo = words[word]
                    if wordOne[i] == wordTwo[i]:
                        characterMatchCount += 1

                if characterMatchCount >= len(getWord[word]) / 2:
                    score += 1





    scoreCheck[key] = score
    score = 0







for i in scoreCheck:
    if scoreCheck[i] > prevScore:
        highestMatch = i

    prevScore = scoreCheck[i]


print(Data[highestMatch])







































"""
match_finder  = []
match_count = 0
highest_match = 0
highest_match_count = 0
message = ""
current_query_count = 0



while message != "exit":
    print("Send message: ")
    message = input()

    for i in range(0, len(queries)):
        current_query = queries[i]


        for j in range(0, len(message)):

            if j <= len(current_query) - 1 and message[j] == current_query[j]:
                match_count += 1




        if match_count > highest_match_count:
            highest_match_count = match_count
            highest_match = i

        match_count = 0

    match_finder.append(highest_match)
    print(responses[match_finder[0]])
    match_finder.remove(highest_match)

"""


