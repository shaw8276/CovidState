import requests
import json

n = input("Enter the state to know covid 19 stats :")


url="https://api.covid19india.org/state_district_wise.json"
response = requests.get(url)
response_info = response.json()
response_json = json.dumps(response.json(),sort_keys=True,indent=4) 

for state, state_data in response_info.items():
    district_info=state_data['districtData']
    district=district_info.keys()

    if state.lower() == n:
        a=0;
        c=0;
        d=0;
        r=0;
        
        for district_name,district_values in district_info.items():
            a=a+(district_values['active'])
            c=c+(district_values['confirmed'])
            d=d+(district_values['deceased'])
            r=r+(district_values['recovered'])
            print('')
            print('-------------------')
            print(f'name:{district_name}')
            print('-------------------')
            print(f' active   :{district_values["active"]}')
            print(f' confiremd:{district_values["confirmed"]}')
            print(f' deceased :{district_values["deceased"]}')
            print(f' recovered:{district_values["recovered"]}')
        print('')
        print('---------------------------------------------------------------------------------')
        print('')
        print('total covid stats for '+n+' are:')
        print('ACTIVE    :',a)
        print('CONFIRMED :',c)
        print('DECEASED  :',d)
        print('RECOVERED :',r)
