import configparser

parser = configparser.ConfigParser()
parser.read('..//config//config.ini')
# parser.read('config.ini')
print('Narayan')
for sect in parser.sections():
    print('Section:', sect)
    for k, v in parser.items(sect):
        print(' {} = {}'.format(k, v))
    print()
