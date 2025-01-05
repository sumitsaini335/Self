from collections import Counter
def learning_01():
    #  count similar elements in a string
    print(" count similar elements in a string")


    # Example string
    string = "abracadabra"

    # Count elements
    counts = Counter(string)

    # Print counts
    print(counts)

# code = learning_01()

def learning_02():

    # Reverse a String
    print("Reverse a String")

    txt = "Hello World"[::-1]
    print(txt)

def learning_03():
    #remove duplicate from string
    print("remove duplicate from string")
    mylist = ["a", "b", "a", "c", "c"]
    mylist = list(dict.fromkeys(mylist))
    print(mylist)

def learning_04():
    #String is a Palindrome
    print("String is a Palindrome")
    c = 0
    s = "madam"

    if s == s[::-1]:

        print(True)
    else:
        print(False)

def learning_05():

    # First Non-Repeating Character
    print("First Non-Repeating Character")

    # st = "swiss"
    #
    # count = Counter(st)
    # char_count = {}
    # print(count)
    # for char in st:
    #     # char_count[char] = char_count.get(char, 0) + 1
    #     if char in char_count:
    #         char_count[char] += 1
    #     else:
    #         char_count[char] = 1
    # print(char_count)
    #
    # for char in st:
    #     if char_count[char] == 1:
    #         print("found",char)
    #         break
    # from collections import Counter

    st = "swiss"

    # Step 1: Count character frequencies
    count = Counter(st)

    # Step 2: Find the first non-repeating character
    for char in st:  # Iterate through characters, not indices
        if count[char] == 1:
            print(char,count[char])  # Print the first non-repeating character
            break
    else:
        print("No non-repeating character found")

def learning_06():

    # rotate an array

    h = ["a",5,5,5,5,5,5,6,6]
    print(h)

    k = 8
    k = k % len(h)

    h = h[-k:] + h[:-k]

    print(h)


def learning_07():

    # reverser a array
    arr = [1,2,3,4,5,6]
    element = 5
    arra = arr[::-1]
    print(arra)
    coutn = Counter(arra)
    print(coutn)

    if element in arra:
        print({element})
    # arra.append("abc")
    a = arr.sort()
    print(a)
    f = arra.sort()
    print(arra)


def learning_08():
    import re

    # add mumerical vaule presnet in a string
    st = "Sumit1000 saini100 good10 morning99"
    # Extract all numbers using a regular expression
    numbers = re.findall(r'\d+', st)

    # Convert the extracted numbers to integers and calculate their sum
    sum_of_numbers = sum(map(int, numbers))

    # Print the result
    print(f"The sum of numerical values in the string is: {sum_of_numbers}")


code = learning_08()