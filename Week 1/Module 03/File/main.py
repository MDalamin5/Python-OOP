# . csv comma separated value
# .txt text file

# with open('message.txt', 'w') as file:
#     file.write('HEllo how are you')

with open('message.txt', 'r') as file:
    text = file.read()
    print(text)