from hash import knothash


def get_grid(key: str):
    for i in range(128):
        yield knothash(key + '-' + str(i))


if __name__ == '__main__':
    # first task is to count set bits in the grid
    count = 0

    for row in get_grid('amgozmfv'):
        #print(row.hex())
        for c in row.hex():
            match c:
                case '0':
                    count += 0
                case '1':
                    count += 1
                case '2':
                    count += 1
                case '3':
                    count += 2
                case '4':
                    count += 1
                case '5':
                    count += 2
                case '6':
                    count += 2
                case '7':
                    count += 3
                case '8':
                    count += 1
                case '9':
                    count += 2
                case 'a':
                    count += 2
                case 'b':
                    count += 3
                case 'c':
                    count += 2
                case 'd':
                    count += 3
                case 'e':
                    count += 3
                case 'f':
                    count += 4

    print(count)
