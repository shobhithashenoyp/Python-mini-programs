def palindrome(s):
    rev = ""
    for i in s:
        rev=i+rev
    if rev==s:
        print("Palindrome")
    else:
        print("Not Palindrome")
text = input("Enter a string:")
palindrome(text)