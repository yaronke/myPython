# vowels = 0
# consonants = 0
#
# for letter in "supercalifragilisticexpioalidocious":
#     if letter.lower() in "aeiou":
#         vowels = vowels + 1
#     elif letter == " ":
#         pass
#     else:
#         consonants = consonants +1
#
# print("There are {} vowels".format(vowels))
# print("There are {} consonants".format(consonants))


# students = {
#     "male": ["Tom", "Charlie", "Harry", "Frank"],
#     "Female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
# }
#
# for key in students.keys():
#     for name in students[key]:
#         if "d" in name:
#             print(name)

evenNumber = [x for x in range(1, 101) if x % 3 == 0]
print(evenNumber)