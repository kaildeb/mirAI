

queries = ["hello", "who's the best waifu", "sing tokyo", "tell me a story", "meal prep"]

responses = ["Hi there, welcome back! I've missed you hehehe~", "I am of course? I'll let you guess why...", "NYA ITCHI NII SAAAAN", "You and your AI waifu lived happy together!", "How about I just cook you something, mmm?"]

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









