if __name__ == '__main__':
    n = int(raw_input())

    width = 2*n + 1
    def print_rhombus(nb_whitespace, level):
        whitespace = ' '*nb_whitespace
        stratified = [str(i) for i in range(level)]
        ascending = [0]*(2*level)
        ascending[::2], ascending[1::2] = stratified, ' '*level

        ascending = ''.join(ascending)
        descending = ascending[::-1]

        print whitespace + ascending + str(level) + descending

        if level == n:
            return

        print_rhombus(nb_whitespace-2, level+1)

        print whitespace + ascending + str(level) + descending

    print_rhombus(2*n, 0)
