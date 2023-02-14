def factorial(n):
    def fact_iter(product, counter):
        return product if counter > n else fact_iter(counter * product, counter + 1)

    return fact_iter(1, 1)


if __name__ == '__main__':

    # create table with columns a-j
    # each column holds 10 numbers
    # each list increments to 10 by 1 using the function range((i , (i + 10)))
    n_table = {
        'a': [x for x in range(1, 11)],
        'b': [x for x in range(11, 21)],
        'c': [x for x in range(21, 31)],
        'd': [x for x in range(31, 41)],
        'e': [x for x in range(41, 51)],
        'f': [x for x in range(51, 61)],
        'g': [x for x in range(61, 71)],
        'h': [x for x in range(71, 81)],
        'i': [x for x in range(81, 91)],
        'j': [x for x in range(91, 101)]
    }

    # create factorial table using n of columns in n_table
    factorial_table = {
        'a': [factorial(x) for x in n_table.get('a')],
        'b': [factorial(x) for x in n_table.get('b')],
        'c': [factorial(x) for x in n_table.get('c')],
        'd': [factorial(x) for x in n_table.get('d')],
        'e': [factorial(x) for x in n_table.get('e')],
        'f': [factorial(x) for x in n_table.get('f')],
        'g': [factorial(x) for x in n_table.get('g')],
        'h': [factorial(x) for x in n_table.get('h')],
        'i': [factorial(x) for x in n_table.get('i')],
        'j': [factorial(x) for x in n_table.get('j')],
    }

    # zip up individual table list into a single new list
    # &
    # create an enumerator to iterate through the new list
    fact_table_iter = enumerate(zip(*factorial_table.values()))

    # print out factorial table
    print("Factorial Table 1-100")
    for index, column in fact_table_iter:
        print(f"{index + 1:2}! = {column[0]:16}\t\t\t"
              f"{index + 11}! = {column[1]:32}\t\t\t"
              f"{index + 21}! = {column[2]:42}\t\t\t"
              f"{index + 31}! = {column[3]:62}\t\t\t"
              f"{index + 41}! = {column[4]:82}\t\t\t"
              f"{index + 51}! = {column[5]:102}\t\t\t"
              f"{index + 61}! = {column[6]:122}\t\t\t"
              f"{index + 71}! = {column[7]:144}\t\t\t"
              f"{index + 81}! = {column[8]:166}\t\t\t"
              f"{index + 91:3}! = {column[9]:188}\t\t\t")
