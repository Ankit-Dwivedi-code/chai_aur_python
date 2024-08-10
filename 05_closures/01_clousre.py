
def square(num):
    def actual(n):
        return n ** num
    return actual

a = square(2)
print(a(5))