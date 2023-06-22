

customer = ['type', 0, 0, 0, 0]  # customer[type, sum2pay, bags, meals, price]

budget = ['Budget', 500]  # tickettypes as [type,  cost]
economy = ['Economy', 750]
vIP = ['VIP', 2000]

bag = 200  # bag [int2pay]
meal = 150


print('Ticket types: \n'
      f'1: {budget[0]} \t ({budget[1]:>4}kr) \n'
      f'2: {economy[0]} \t ({economy[1]:>4}kr) \n'
      f'3: {vIP[0]} \t \t ({vIP[1]:>4}kr) \n')


# input validation
while(True):
    choose = input('Input ticket type >> ')

    # if choose x,  write x to customer
    if choose == '1':
        customer[0] = budget[0]  # save ticket types
        customer[1] = budget[1]  # add ticket cost 2 sum2pay
        customer[4] = budget[1]  # save ticket cost

        # break while loop
        break

    elif choose == '2':
        customer[0] = economy[0]
        customer[1] = economy[1]
        customer[4] = economy[1]

        break
    elif choose == '3':
        customer[0] = vIP[0]
        customer[1] = vIP[1]
        customer[4] = vIP[1]
        break

        # not valid option start over
    else:
        print(choose, 'is not a valid input \n')


while(True):

    print('\n Currently you have: \n '
          f'\t{customer[2]} bag(s) registered \n'
          f'\t{customer[3]} meal(s) registered \n'
          "\n" +
          'Here are your options \n'
          '1: Add bag (max 1) \n'
          '2: Add meal (max 1) \n'
          '3: remove bag \n'
          '4: remove meal \n'
          '5: Finalize ticket \n')

    choose = input('Your choice >> ')

    if choose == '1':

        if(customer[2] == 0):  # check number of bags, max is 1
            customer[1] = customer[1]+bag  # add cost 2 sum2pay
            customer[2] = 1  # add 1 bag 2 customer
        else:
            print('Error too many bags', "\n")

    elif choose == '2':

        if(customer[3] == 0):
            customer[1] = customer[1]+meal
            customer[3] = 1
        else:
            print('Error too many meals', "\n")

    elif choose == '3':
        if(customer[2] == 1):  # check number of bags,  min is 0
            customer[1] = customer[1]-bag  # substract cost 2 sum2pay
            customer[2] = 0  # make bags = 0
        else:
            print('Error you cant have less than 0 bags', "\n")

    elif choose == '4':
        if(customer[3] == 1):
            customer[1] = customer[1]-meal
            customer[3] = 0
        else:
            print('Error you cant have less than 0 meals', "\n")

    elif choose == '5':
        print(f'Receipt:  \n'
              f'Ticket :{customer[4]:>5}kr')
        if(customer[2] == 1):
            print(f'Bag    :{bag:>5}kr')

        if(customer[3] == 1):
            print(f'Meal   :{meal:>5}kr')

        print('        -------')
        print(f'Total  :{customer[1]:>5}kr')

        break
    else:
        print(choose, 'is not a valid input \n')
