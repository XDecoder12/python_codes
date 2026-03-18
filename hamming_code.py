print("Hamming-Code Error Detection and Correction")

def calc_parity_bits(m):
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def place_parity_bits(data, r):
    j = 0 #parity position counter
    k = 1 #data bit index
    m = len(data)
    new_string = ''
    for i in range(1, m + r + 1):
        if i == 2 ** j:
            new_string = new_string + '0'
            j += 1
        else:
            new_string = new_string + data[-k]
            k += 1
    return new_string[::-1]

def calculate_parity(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i):
                val = val ^ int(arr[-j])
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr

def detect_error(arr, r):
    n = len(arr)
    error_pos = 0
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i):
                val = val ^ int(arr[-j])
        error_pos += val * (10 ** i)
    return int(str(error_pos), 2) #Binary to integer

data = input("Enter data bits: ")
m = len(data)
r = calc_parity_bits(m)
arr = place_parity_bits(data, r)
hamming_code = calculate_parity(arr, r)

print()
print("Generated Hamming Code:", hamming_code)

print()
received = input("Enter received code: ")

error_pos = detect_error(received, r)

print()
if error_pos == 0:
    print("No error detected")
else:
    print("Error detected at position:", error_pos)
    corrected = list(received)
    if corrected[-error_pos] == '0':
        corrected[-error_pos] = '1'
    else:
        corrected[-error_pos] = '0'
    corrected = "".join(corrected)

    print()
    print("Corrected code:", corrected)