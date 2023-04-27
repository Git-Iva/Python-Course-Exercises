#Check if a tweet is short enough to be posted
# It is assumed the standard tweet is 140 characters long 
#Otherwise print that the tweet is too long to be posted

tweet = input("Enter your tweet here: ")
if len(tweet) <= 140: 
    print(f"That {len(tweet)} characters will work")
else:
    print(f"Your {len(tweet)} tweet is {len(tweet)- 140} characters too long!")
