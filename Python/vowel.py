
text = input("Enter text: ")
res = ""
for x in text:
    if x in "aeiouAIEOU":
        res+="*"
    else:
        res+=x
print('Modified text: ',res)
