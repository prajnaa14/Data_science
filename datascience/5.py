from functools import reduce
with open("C:\\Users\\PRAJNA\\Downloads\\Big_Data\\lorem.txt") as file:
    text=file.read()

target='lorem'

def map(line):
    words=line.strip().split()
    return [(word,1) for word in words if word==target]

def reducer(count1,count2):
    return count1+count2

mapper=[pair for line in text.split('\n') for pair in map(line)]
count=[count for word, count in mapper]
freq=reduce(reducer,count)
print(f"The word {target} repeated {freq} time(s).")