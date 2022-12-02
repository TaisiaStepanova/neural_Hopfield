from lib import *

if __name__ == '__main__':

    print("----------MENU----------")
    print("1) Training of neural network\n2) Recognition\n")
    menu = input("Enter number: ")

    if menu == '1':
        folder = input("Enter folder name: ")
        n = input("Enter the length of the vector: ")

        training(int(n), folder)

    elif menu == '2':
        print('Enter filename: ')
        for filename in os.listdir("unidentified"):
            if filename != '.ipynb_checkpoints':
                print('- ', filename)
        filename = input()

        recognition("unidentified/" + filename)
