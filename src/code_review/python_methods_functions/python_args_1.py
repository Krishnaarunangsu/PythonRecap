def how_many_lists(*args):
    name_roll = []
    roll = 1
    for name in args:
        #name_roll.append(name+'-'+roll)
        for student in name:
            print(student)
            name_roll.append(student + '-' + str(roll))
            #roll = roll+1
            roll +=1

    return name_roll

if __name__=="__main__":
    name_roll_list = how_many_lists(['Krishna', 'Jagannath'])
    print(f'The List is{name_roll_list}')
    print('************************************************************')
    name_roll_list=how_many_lists(['Krishna', 'Jagannath'],['Durga','Kali','Chandi'])
    print(f'The List is{name_roll_list}')

