def checkAnagram(str1,str2):
    if sorted(str1)==sorted(str2):
        print("Anagram")
    else:
        print("Not anagram")
str1=input("Enter the first word: ")
str2=input("Enter the second word: ")
checkAnagram(str1,str2)

