import pandas as pd

def get_data():
    db = pd.read_csv('C:\\Ashu\\Python\\General\\Zip_Codes\\data\\zipcodes.csv')
    db.head()

    df = db[['ZIP', 'CITY', 'STATE', 'COUNTY']]
    df.head(7)

    args = input('Query the database by entering a command, or type \"-h\" for a list of commands or \"-e\" to exit\nquery: ')
    arglist = args.split()
    
    if arglist[0] == '-h' or arglist[0] == '-e':
        arglist.append('NULL')
    elif arglist[0] == '-z':
        arglist[1] = str(arglist[1])

    if '\'' in arglist[1]:
        arglist[1] = arglist[1].replace('\'', ';')
    
    while len(arglist) != 2:
        args = input('Sorry. Invalid request.\nQuery the database by entering a command, or type \"-h\" for a list of commands or \"-e\" to exit\nquery: ')
        arglist = args.split()
        if arglist[0] == '-h' or arglist[0] == '-e':
            arglist.append('NULL')
        elif arglist[0] == '-z':
            arglist[1] = str(arglist[1])

        if '\'' in arglist[1]:
            arglist[1] = arglist[1].replace('\'', ';')

    arglist[1] = arglist[1].upper()

    console(args, arglist, df)

def console(args, arglist, df):
    while '-e' not in args:
        if len(arglist) == 2:
            if arglist[0] == '-ci':
                print(find_city(df, arglist))
            elif arglist[0] == '-co':
                print(find_county(df, arglist))
            elif arglist[0] == '-h':
                print('\nHELP REFERENCE:\n')
                print('-ci \t <city> \t Returns \"<county>, <state>, <zip>\" of the corresponding city')
                print('-co \t <county> \t Returns \"<city>, <state>, <zip>\" of the corresponding county')
                print('-h \t\t\t Prints help reference')
                print('-e \t\t\t Exits program')
                print('-s \t <state> \t Returns \"<city>, <county>, <zip>\" of the corresponding state')
                print('-z \t <zip> \t\t Returns \"<city>, <county>, <state>\" of the corresponding zip')
            elif arglist[0] == '-s':
                print(find_state(df, arglist))
            elif arglist[0] == '-z':
                print(find_zip(df, arglist))
        else:
            print('\nWARNING:\n')
            print('Please enter exactly three command line arguments (number given: %d)' % len(arglist))
            print('\nHELP REFERENCE:\n')
            print('-ci \t <city> \t Returns \"<county>, <state>, <zip>\" of the corresponding city')
            print('-co \t <county> \t Returns \"<city>, <state>, <zip>\" of the corresponding county')
            print('-h \t\t\t Prints help reference')
            print('-e \t\t\t Exits program')
            print('-s \t <state> \t Returns \"<city>, <county>, <zip>\" of the corresponding state')
            print('-z \t <zip> \t\t Returns \"<city>, <county>, <state>\" of the corresponding zip')
        
        get_data()
    exit()

def find_city(df, arglist):
    ret_val = ''
    for i in range(len(df)):
        if df.CITY[i] == arglist[1]:
            ret_val += '{0}, {1}, {2}\n'.format(df.COUNTY[i], df.STATE[i], df.ZIP[i])
    return ret_val

def find_county(df, arglist):
    ret_val = ''
    for i in range(len(df)):
        if df.COUNTY[i] == arglist[1]:
            ret_val += '{0}, {1}, {2}\n'.format(df.CITY[i], df.STATE[i], df.ZIP[i])
    return ret_val

def find_state(df, arglist):
    ret_val = ''
    for i in range(len(df)):
        if df.STATE[i] == arglist[1]:
            ret_val += '{0}, {1}, {2}\n'.format(df.CITY[i], df.COUNTY[i], df.ZIP[i])
    return ret_val

def find_zip(df, arglist):
    ret_val = ''
    for i in range(len(df)):
        if str(df.ZIP[i]) == arglist[1]:
            ret_val += '{0}, {1}, {2}\n'.format(df.CITY[i], df.COUNTY[i], df.STATE[i])
    return ret_val

if __name__ == '__main__':
    get_data()