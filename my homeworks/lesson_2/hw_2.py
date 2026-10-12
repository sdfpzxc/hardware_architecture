A, B, C = 12, 9, 7 # 1100, 1001, 0111

res1 = (~(A & B)) | (~(A | C))
res2 = (A & B) | ((~B) & C)
res3 = (A & B) | (~C)

# берем младшие 4 бита, для этого используем масочку
mask = 0b1111
print(f"1: {res1 & mask} (биты: {bin(res1 & mask)})")
print(f"2: {res2 & mask} (биты: {bin(res2 & mask)})")
print(f"3: {res3 & mask} (биты: {bin(res3 & mask)})")
