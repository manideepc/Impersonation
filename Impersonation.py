import requests
import pandas as pd
import simplejson as json
import logging
import time
import pandas as pd
from numpy import nan
import math
file_name='IDM-5370.csv'
df=pd.read_csv('/Users/manideep/Desktop/'+file_name)
#print(type(df['...the following Users are to be impersonated'].values))
Impersonators =list(set(df.iloc[::,1].tolist()))
#Impersonating =list(set(df['...the following Users are to be impersonated'].values))
Impersonating =list(set(df.iloc[::,3].tolist()))
Impersonators = [item for item in Impersonators if not(pd.isnull(item)) == True]
Impersonating = [item for item in Impersonating if not(pd.isnull(item)) == True]
print('Total no of users:',len(Impersonating)+len(Impersonators))
Inactive_users=[]
Invalid_users=[]
restricted_users=[]
start = time.time()
print()
for i in (Impersonators):
    i=i.lower()
    if i.endswith(**Domain Name**)==False:
        Invalid_users.append(i)
        Impersonators.remove(i)
for i in (Impersonating):
    i=i.lower()
    if i.endswith(**Domain Name**)==False:
        Invalid_users.append(i)
        Impersonating.remove(i)

print('Process Started..')
logging.basicConfig(filename="/Users/manideep/Desktop/"+file_name[:-4]+".log",
                    format='%(asctime)s %(message)s ',
                    filemode='w')
# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


for i in Impersonators:

            response = requests.get(**Web Service End Point**)
            if response.status_code==200 :
                    response_data = json.loads(response.text)
                    if response_data['Active']==1:
                        print('.', end='')
                        #pass
                    elif response_data['Active']==-1:
                        print('!', end='')
                        logger.debug(i+'-'+response_data['Message'])
                        Inactive_users.append(i)
                        #print()
            else:
                    logger.debug('Error while calling the API for this user: '+i)

for i in Impersonating:
    response = requests.get(** Webservice End Point**)
    if response.status_code==200 :
            response_data = json.loads(response.text)
            if response_data['Active']==1 and response_data['Check career']==1:
                print('.',end='')
                pass
            elif response_data['Active']==1 and response_data['Check career']==-1:
                print('!', end='')
                logger.debug(i + '-' + response_data['Message'])
                restricted_users.append(i)
            elif response_data['Active']==-1 and response_data['Check career']==-1:
                print('!', end='')
                logger.debug(i + '-' + response_data['Message'])
                Inactive_users.append(i)
    else:
        logger.debug('Bad Request:The request path contains illegal characters:-'+i)
end=end = time.time()
print()
print('End of Process..!!')
print(f"Runtime of the program is {end - start}")
print('*************************************Results****************************************')
print("\033[4m" + 'Loading the results:' + "\033[0m")
print()

print("\033[4m" +'List of Inactive Users:'+ "\033[0m")

for i in Inactive_users:
    print(i)
print()
print("\033[4m" +'List of Invalid Users:'+ "\033[0m")


for i in Invalid_users:
    print(i)
print()

print("\033[4m" +'List of restricted_users:'+ "\033[0m")

for i in     restricted_users:
    print(i)

print()
print('*********************************-----------------***********************************')
print()
print('Logging the details in '+"\033[4m" +file_name[:-4]+".log"+ "\033[0m")



# Test messages
logger.debug('')
logger.debug('**********************Final Results**********************')
logger.debug("Invalid Users :")
logger.debug(Invalid_users)
logger.debug('----------')
logger.debug('Inactive Users')
logger.debug(Inactive_users)


logger.debug('End of Debugging')
