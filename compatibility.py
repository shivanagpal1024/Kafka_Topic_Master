import os
from os import listdir
from string import join
import requests
import json
import sys
import re

BASE_PATH='./topics'
DEV_SCHEMA_REGISTRY_URL='http://kaas-test-schema-registry-a.optum.com/config/'
PROD_SCHEMA_REGISTRY_URL='http://kaas-prod-schema-registry-a.optum.com/config/'

#################################################################
#                      FindCompatability                        #
#################################################################

def FindCompatability(source_file, env):
    arr_header = []
    headers = {'Content-Type': 'application/json'}
    with open(source_file) as f:
        # skip first line of column names
        csv_header = f.readline()
        arr_header = csv_header.split(',')
        for i in range(len(arr_header)) :
              arr_header[i] = re.sub('[^A-Za-z]+','', arr_header[i])
        csv_header = ','.join(arr_header)
        if csv_header.find('compatibility') != -1 :            
            com_col = list(csv_header.split(',')).index('compatibility')
            for line in f:
                columns = line.split(',')
                compatibility = columns[com_col].strip()
                if (compatibility):
                    print('PUT ' + env + columns[0] + '-key\n{\n\t"compatibility": "' + compatibility +'"\n}'  )
                    content_body = {'compatibility': compatibility}
                    key_request = requests.put(
                        env + columns[0] + '-key',
                        data=json.dumps(content_body),
                        headers=headers
                    )
                    print(key_request)
                    print('PUT ' + env + columns[0] + '-value\n{\n\t"compatibility": "' + compatibility +'"\n}'  )
                    key_response = key_request.json()
                    value_request = requests.put(
                        env + columns[0] + '-value',
                        data=json.dumps(content_body),
                        headers=headers
                    )
                    print(value_request)
                    value_response = value_request.json()
                    

#################################################################
#                            Main                               #
#################################################################

if __name__ == '__main__':
    file = sys.argv[1]
    env = sys.argv[2]
    if (env == 'prod'):
        env_url = PROD_SCHEMA_REGISTRY_URL
    elif (env == 'dev'):
        env_url = DEV_SCHEMA_REGISTRY_URL
    else:
        env_url = ''
        print('Invalid environment provided...')
        sys.exit() 
    print('Checking for compatibility updates in file: ' + file + ' in the ' + env + ' environment...')
    FindCompatability(file, env_url)
