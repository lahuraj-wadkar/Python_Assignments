#***************************************************************************************************
#                     Check if character is Vowel or Consonent                                     
#***************************************************************************************************

def isVowel(val):
    vowel = ["a", "e", "i", "o", "u"]
    for char in vowel:
        if(val == char):
            return True
    return False
def main():
    val = input("Enter character :")
    if (isVowel(val)):
        print("Entered character :", val, "is vowel")
    else:
        print("Entered character :", val, "is consonent")

if(__name__ == "__main__"):
    main()