from textblob import TextBlob
import pyttsx3


engine = pyttsx3.init()
engine.say("Hello, my dear worker! Did you celebrate 1st May already? We hope you had a great day of work. It's time to submit your employee wellness statement: ")
engine.runAndWait()


print("Enter your employee wellness statement: ")
phrase = input( ">")
blob = TextBlob(phrase)
while blob.sentiment.polarity < 0.5:
    engine.say("That was not positive at all.Please try again and be more positive next time. Be happy, don't fake it!")
    engine.runAndWait()
    print("More positive, please!")
    phrase = input (">")
    blob = TextBlob(phrase)
    

print ("We appreciate you too!")
engine.say("Thank you my dear worker! We are happy that you are happy!")
engine.runAndWait()
