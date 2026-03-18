# to uppercase the whole string input from the user

print("Enter your text: ")
lines = []
while True:
    input_text = input()
    if input_text == "":
        break
    else:
        lines.append(input_text.upper())
for line in lines:
    print(line)


# find longest unique substring 

def longest_unique_substring(s):
    seen = {}
    start = 0
    longest = ""

    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        if i - start + 1 > len(longest):
            longest = s[start:i+1]
    return longest
print(longest_unique_substring("aaaabbbbcccc"))


# 
