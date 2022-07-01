import csv
import data.constant as constantes
def creation(name):
    try:
        with open(f'{name}.csv') as archivo:
            print('File Already Exist...')
            formatFile = csv.reader(archivo)
            for lines in formatFile:
                print(lines)
            chose = input('ingrese y para sobrescribir, de lo contrario n :')
            if chose=='y': raise Exception
            archivo.close()
            return {'exist':True,'stop':True}
    except:
        print('creating...')
        with open(f'{name}.csv','w',newline='') as archivo:
            csv.writer(archivo).writerow(constantes.row_info)
            archivo.close()
            print('created successfully')
            return {'created':True,'stop':False}