def To_lower(s):
    n = []
    s = ''
    for i in s:
        a = ord(i) + 32
        n.append((chr(a)))
        
    s = ''.join(x for x in n)
    return s

# n = input("Enter a String")
print(To_lower("AXC"))