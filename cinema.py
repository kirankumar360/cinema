films = {
    'Temper':[15,5],
    'Power':[10,5],
    'Rrr':[12,5],
    'Ishq':[14,5]
    }

while True:

    choice = input('What film do you want to watch?: ').strip().capitalize()

    if choice in films:
        age = int(input('How old are you?: '))

        if age >= films[choice][0]:


            num_seats = films[choice][1]

            if num_seats >0:             
                print('Enjoy the film...')
                films[choice][1] = films[choice][1]-1
            else:
                print('We are sold out the tickets...')
        else:
            print('You are too young to watch the film...')
    else:
        print('The choice of cinema is not in the list...')
        
        
