print("""
#                                              #
#                  HackTiviste                 #
#                                              #
#                                              #
#       ____+  Wellcom M. Electron  +____      #
#                                              #
#                                              #
#                                              #
Project to remove duplicate letters within texts
************************************************
""")

def cleanWord(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return cleanWord(word[1:])
    return word[0] + cleanWord(word[1:])
    
while True:
    text = input("Enter The Text : ").strip().lower()
    addtext = input("\nDo you want to add text in a new file? (Y,N)").strip().lower()
    clean = cleanWord(text)

    if addtext == 'y':
        namefile = input("\nName File : ")
        namefiletow = namefile + ".txt"
        file = open(namefiletow, 'w')
        file.write(clean)
        file.close()
        print("Done.")

    elif addtext == 'n':
        print("\n" + cleanWord(text))
    print("\n" + "*" * 30 + "\n" )
