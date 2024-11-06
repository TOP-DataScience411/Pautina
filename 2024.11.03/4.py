def simple_numbers(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2

n = int(input())

print(len([i for i in range(int('1' + '0' * (n-1)), int('1' + '0' * (n))) if simple_numbers(i)]))

#3
#143