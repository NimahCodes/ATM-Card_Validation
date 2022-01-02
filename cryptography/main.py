from art import art
print(art)


print('What would you like to do?')
print('Encode(Encrypt) or Decode(Decypt)?')
print(f'Select \'Encrypt\' or \'Decrypt\'')
run = 'yes'
while run == 'yes':
    select_task = input('Would you like to Encrypt or Decrypt? ').lower()
    service_input = input('Enter Password (text): ').lower()
    number_loop = int(input('What Range would you like, note: It must be a number: '))
    alphabet_val = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # print(alphabet_val)
    service_input_new = list(service_input)
    encrypt_val = []
    decrypt_val = []
    if select_task == 'encrypt':
        for item in service_input_new:
            if item not in alphabet_val:
                print('Only alphabet is needed.')
                break
            else:
                value = alphabet_val.index(item) + number_loop
                if value > len(alphabet_val):
                    value = value - len(alphabet_val)
                encrypt_val.append(alphabet_val[value])
        hold = ''.join(encrypt_val)
        print(hold)

    elif select_task == 'decrypt':
        for item in service_input_new:
            if item not in alphabet_val:
                print('Only alphabet is needed.')
                break
            else:
                value = alphabet_val.index(item) - number_loop
                if value > len(alphabet_val):
                    value = value + len(alphabet_val)
                decrypt_val.append(alphabet_val[value])
        hold = ''.join(decrypt_val)
        print(hold)
    else:
        print(f'Your are expected to enter Decrypt or Encrypt')
    run = input('Would you like to continue, type \'Yes\' or \'No\' ? ').lower()