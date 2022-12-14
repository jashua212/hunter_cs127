
# assignment 36

def computePrice(liquid, size):
    if liquid == 'coffee':
        if size == 'small':
            price = '2.5'
        elif size == 'medium':
            price = '2.75'
        elif size == 'large':
            price = '3.00'
        else:
            price = '-1'
    elif liquid == 'misto':
        if size == 'small':
            price = '3.15'
        elif size == 'medium':
            price = '3.35'
        elif size == 'large':
            price = '3.7'
        else:
            price = '-1'
    elif liquid == 'mocha':
        if size == 'small':
            price = '3.5'
        elif size == 'medium':
            price = '3.8'
        elif size == 'large':
            price = '4.25'
        else:
            price = '-1'
    elif liquid == 'tea':
        if size == 'small':
            price = '2.35'
        elif size == 'medium':
            price = '2.45'
        elif size == 'large':
            price = '2.90'
        else:
            price = '-1'
    else:
        price = '-1'

    return float(price)


def main():
    liquid = input('Enter your beverage: ')
    size = input('Enter your size: ')
    price = computePrice(liquid, size)

    if price == -1:
        price = '-1'

    print(size, 'size', liquid + ':', price)


if __name__ == '__main__':
    main()
