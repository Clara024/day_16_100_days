print ("Complete the Quote")
counter = 1
while True:
    quote = input ("One good turn _________ another:")
    if quote == "deserves":
        print ("That is correct")
        break
    else:
        print ("That's wrong")
        counter += 1

print ("You got the answer in",counter,"attempts")
print ("Thanks for playing!!")