#Write a program to detect spam messages.
'''Make a lot of money,buy now,subscribe this,click this'''
p1="Make a lot of money"
p2="Buy Now"
p3="Subscribe this"
p4="Click this"
msg=input("Enter a message for your customer:-")

if((p1 in msg)or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("SCAM ALLERT!")
else:
    print("THIS IS SAFE")
