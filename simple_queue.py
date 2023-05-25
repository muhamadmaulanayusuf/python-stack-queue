from collections import deque # import module

queue = deque([1,2,3,4,5])
print('antrian sekarang : ', queue)
 
#menambahakan data antrian
queue.append(6)
print('antrian masuk : ', 6)
print('antrian sekarang : ', queue)

queue.append(7)
print('antrian masuk : ', 7)
print('antrian sekarang : ', queue)

#mengurangi antrian
out = queue.popleft()
print('antrian keluar : ', out)
print('antrian sekarang : ', queue)