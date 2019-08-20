import requests
import csv
import json

#Resquest to banxico's api change rate fix
try:
    response = requests.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF60653/datos', 
    headers={
        'Bmx-Token': '4dd474b2ab133983dd703942c7b08f114db49aae7afa6fe4e1ae1d01803ea728'
    })

    #Response jsonized
    change_rate_response =  response.json()
    print(change_rate_response["bmx"]["series"][0]['datos'])
    print(change_rate_response.keys())
    print(type(change_rate_response))

    print(len(change_rate_response["bmx"]["series"][0]['datos']))



    #Create the csv writer object

    csv_writer =  csv.writer(open(r"//192.168.1.38/2. DATOS FUENTE/BI/Extracciones Web/daily_exchange_rate.csv", "w"), delimiter=",", lineterminator='\n')

    count = 0
    header =['Fecha','Parasolventarobligaciones']
    csv_writer.writerow(header)
    for row_change_rate_fix in change_rate_response["bmx"]["series"][0]['datos']:
        row = [row_change_rate_fix['fecha'],row_change_rate_fix['dato']]
        print(row)
        csv_writer.writerow(row)

except Exception as e:
    print(e)


    




#repository = json_response['items'][0]
#print(f'Repository name: {repository["name"]}')  # Python 3.6+
#print(f'Repository description: {repository["description"]}')