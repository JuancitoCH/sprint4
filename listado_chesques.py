import csv
from datetime import time

def search(name='',value='',nameCsv="data/data-clients.csv") -> tuple:
    # 'tuple(Boolean,"data;True=>[] ;False=>"" ")'
    """"
    Esta funcion busca en los datos del csv
    se le pasa el valor del nombre del campo a filtrar
    y el valor de ese campo
    retorna una tuple(Boolean,Data)
    filtro exitoso =>returned values:( true ,[data],formatData )
    filtro no exitoso =>returned values: ( false ,'message' )
    """
    fileData=open(f'./{nameCsv}','r')
    csvFile = csv.reader(fileData)
    infoInArray = []
    dataToShow = []
    for i,fila in enumerate(csvFile):
        if i==0 :infoInArray={ value:i for i,value in enumerate(fila)}
        if (infoInArray.get(name)!=None and value == fila[infoInArray.get(name)]):
            dataToShow.append(fila)
    fileData.close()
    if(len(dataToShow)==0): return (False,'no Data Found')
    return (True,dataToShow,infoInArray)



def showOnTerminalCuadro(data,format):
    for key in list(format.keys()):
        print(key,end='   ')
    print('\n')
    for cheque in data:
        for camp in cheque:
            print(camp,end='   ')
        print('\n')



def showOnterminal(data,format):
    'a'


# print(search('NroCheque','0001'))
# print(search('DNI','40998788'))
dataFiltrada=search('DNI','1617591371',"data/data-clients.csv")
if(dataFiltrada[0]==True):
    # showOnTerminalCuadro(dataFiltrada[1],dataFiltrada[2])
    'a'



# NroCheque
# CodigoBanco
# CodigoScurusal
# NumeroCuentaOrigen
# NumeroCuentaDestino
# Valor
# FechaOrigen
# FechaPago
# DNI
# Estado