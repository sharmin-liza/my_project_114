# in, not, not in, is, is not 
# >, <, >=, <=, ==, !==
# and, or

a = 1

if a > 5:
    print( '5 er besi')
    print('koto besi ke jane')
elif a > 3:
    print('olpo boro')
elif a == 2:
    print('ekdom dui er soman soman')
else:
    print('onno kichu')
boss = False
# if boss is not True:
#     print('tel er bakso niye astesi boss re tell dio')
# else: 
#     print('lunch er pore asen')
if boss is not True:
    print('we will boycott him')
else:
    print("boss is a good man. we should support him")
    
coin='tail'

if boss==True:
    print('our boss is joss')
    if coin=='tail':
        print('winning')
    else:    
        print('bowling')   
        if 5>3 or boss!=True:
            print('do something') 

            if 8%2 == 0 and 5%2==1:
                print('even number it is')
else:
    print('you are a bad boss')
