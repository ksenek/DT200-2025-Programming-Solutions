##
#secret_message.py

#Variable to store original string
original_message = "kwnwlkicopipxlfanadsdpinogmjnxpltueh sqgqljquynsamstcmsvkwvn svrlxbriuexkpsiesha khramcx gjpdumbujgrcqmmkalv awdsxwzodpvanhfrcsi dvaloetixabkabdetek cpwatrxnzlo kpneruxaoivgaaclcnaeqcweskbkmxqmbpuqoyjzsvj"

#Split the string into a list of characters
secret_message = list(original_message)

message = []

#Extract every fourth character from index 20 to 184
for word in range(20, 184, 4):  
    message.append(secret_message[word])

#Join the characters to form the message
display_message = ''.join(message)

print(display_message)

