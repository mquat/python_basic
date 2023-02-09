class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __getitem__(self, index):
        #start를 시/분/초로 나눠야 함. 만약 몫이 24면 0으로 다시 넘어가야 함
        hour = (self.start+index) // 3600 % 24
        min = (self.start+index) // 60 % 60
        sec = (self.start+index) % 60
        #start < stop일 때까지 start를 00:00:00에 맞게 return 
        if index < self.stop - self.start:
            return '{0:02d}:{1:02d}:{2:02d}'.format(hour,min,sec)
        #else, return error
        else:
            raise IndexError


start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')
