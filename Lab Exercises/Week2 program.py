# Class work

while True:
    inp = input('\nEnter Your Name: ')
    if inp == 'Done':  # Enter "Done" to exit
        break
    else:
        print('\nWelcome', inp, '!')  # print Welcome + User Name
        try:
            cel = input('\nEnter Value in Celcius Degree:')  # input degree celcius value
            fahren = (9 / 5 * float(cel)) + 32  # formula to calculate temperature in fahrenheit
            # print all values
            print('\n User Name:', inp, '\n', 'Temperature(Celcius): ', cel, '\n', 'Temperature(Fahrenheit):', fahren,
                  '\n\n************************\n')
        except ValueError:
            print('Enter a number')

print('\nBroke out of loop')

