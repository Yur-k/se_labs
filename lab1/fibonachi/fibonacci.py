

def get_fibonacci_row(number):
    f_seq = []
    f0, f1, f2 = 0, 1, 1
    f_seq = [f0, f1, f2]
    for i in range(2, number):
        f_sum = f1 + f2
        f_seq.append(f_sum)
        f1 = f2
        f2 = f_sum
    return f_seq

def get_fibonacci_value(number):
    fib_list = get_fibonacci_row(number)
    return fib_list[-1]


def main():
    fib_row = get_fibonacci_row(40)
    fib_num = get_fibonacci_value(25)

    print(fib_row)
    print(fib_num)

if __name__ == '__main__':
    main()