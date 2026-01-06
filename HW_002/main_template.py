from shape import Shape

def main():
    shape = []
    x = ''  # Initialize x to enter the loop
    while x != '5':
        print('Menu')
        print('1. Add a shape')
        print('2. Update a shape')
        print('3. Delete a shape')
        print('4. Display all shapes')
        print('5. Exit')
        x = input('Enter your choice: ')
        
        if x == '5':
            print('Exiting...')
            break
        else:
            print('Invalid choice! Please enter a number between 1 and 5.')

if __name__ == '__main__':
    main()
