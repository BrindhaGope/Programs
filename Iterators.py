# TO PRINT TOP TEN NUMBERS USING ITERATOR
class Topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:  # FOR FOR LOOP
            val = self.num
            self.num += 1
            return val
        else:
            raise stopIteration  # FOR FOR LOOP


val = Topten()
print(val.__next__())  # USING ITERATION
print(next(val))

for i in val:  # USING FOR LOOP
    print(i)


# USING GENERATORS FETCH TOP TEN VALUES
def topten():
    yield 1
    yield 2
    yield 3
    yield 4

values = topten()

print(next(values))
print(next(values))

for i in values:
    print(i)


# FETCH TOPTEN SQUARE VALUES USING GENERATOR AND FOR LOOP
def topten():
   for n in range(1,11):
       if n<=10:
           sq=n*n
           yield sq

values=topten()

for i in values:
    print(i)

# TO FETCH TOPTEN SQUARE VALUES USING GENERATORS AND WHILE LOOP
def topten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topten()

for i in values:
    print(i)
