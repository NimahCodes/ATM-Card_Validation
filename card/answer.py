def card_validation(number):
    test= str(number)
    integer = list(test)
    new_num=list(reversed(integer))
    index_list=[]
    odd_list=[]
    even_list=[]
    answer_list=[]
    
    for number in range(len(new_num)+1):
        index_list.append(number)

    pi=0
    while pi< len(new_num):
        if index_list[pi]%2!=0:
            odd_list.append(int(new_num[pi])*2)
        else:
            even_list.append(int(new_num[pi]))
        pi+=1
    for fig in odd_list:
        if len(str(fig)) >1:
            test = list(str(fig))
            answer_list.append(int(test[0]))
            answer_list.append(int(test[1]))
        else:
            answer_list.append(fig)
    # print(answer_list)
    odd_sum= sum(answer_list)
    # print(odd_sum)
    even_sum= sum(even_list)
    # print(even_sum)
    total_sum=odd_sum+even_sum
    # print(total_sum)
    if total_sum%10==0:
        print('card is valid')
        if len(test) == 13 or len(test) == 16 or test[0] == '4':
            print('VISA CARD')
        elif len(test) == 16 and test[0] == '5' or test[1] in ['1', '2', '3', '4', '5']:
            print('MASTERCARD')
        elif len(test) == 15 and test[0] == '3' or test[1] in ['4','7']:
            print('AMEX')
    else:
        print('card is invalid')

card_validation(input('Enter Your Card Number: '))