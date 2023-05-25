stack = [1,2,3,4,5]
print('tumpukan sekarang : ',stack)

#Memasukkan data baru
stack.append(6)
print('tumpukan masuk : ',6)
print('tumpukan sekarang : ',stack)

stack.append(7)
print('tumpukan masuk : ',7)
print('tumpukan sekarang : ',stack)

#Mengeluarkan data
out = stack.pop() 
print('tumpukan keluar : ',out)
print('tumpukan sekarang : ',stack)