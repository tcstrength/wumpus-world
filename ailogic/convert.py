st = "3, 5"
temp = st.split(',')
x = int(temp[0])
y = int(temp[1])
s = ""
arrMove = []
if(x - 1 >= 0):
    s = chr(x - 1 + 48) + ',' + chr(y + 48)
    arrMove.append(s)
if(x + 1 <= 9):
    s = chr(x + 1 + 48) + ',' + chr(y + 48)
    arrMove.append(s)
if(y - 1 >= 0):
    s = chr(x + 48) + ',' + chr(y + 1 + 48)
    arrMove.append(s)
if(y + 1 <= 9):
    s = chr(x + 48) + ',' + chr(y - 1 + 48)
    arrMove.append(s)

print(s)
print(arrMove)