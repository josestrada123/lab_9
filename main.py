# Sydney's encoder + main

def encoder(num):
    num = list(num)
    encoded_list = []
    for i in range(len(num)):
        encrypted_num = int(num[i]) + 3
        if int(num[i]) == 7:
            encrypted_num = 0
        elif int(num[i]) == 8:
            encrypted_num = 1
        elif int(num[i]) == 9:
            encrypted_num = 2
        encrypted_num_string = str(encrypted_num)
        encoded_list.append(encrypted_num_string)
    return "".join(encoded_list)

def decoder(num):
    num = list(num)
    decoded_list=[]
    for term in list(num):
        if int(term) == 2:
            decoded_list.append("9")
        elif int(term) == 1:
            decoded_list.append("8")
        elif int(term) == 0:
            decoded_list.append("7")
        else:
            decoded_list.append(str(int(term)-3))
    return "".join(decoded_list)



if __name__ == "__main__":
    encoded = ""
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print("Your encoded password is", encoded,"and the original password is", decoder(encoded))
        elif option == 3:
            break
