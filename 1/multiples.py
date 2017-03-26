def print_list(list):
    for i in list:
        print(i, end=' ')
    print('\n\n')
def multiples(number, limit):
    return list(range(limit)[::number])

def main():
    inputs = 3, 5
    limit = 1000
    for i in inputs:
        print('Multiples of ' + str(i))
        print_list(multiples(i, limit))
main()
