def even_fib_sum(n):
    first = -1
    second = 1
    third = first + second
    even_sum = 0
    for i in range(n):
        first = second
        second = third
        third = first + second
        if third % 2 == 0:
            even_sum += third
    return even_sum

if __name__ == "__main__":
    limit = 4000
    print(even_fib_sum(limit))
