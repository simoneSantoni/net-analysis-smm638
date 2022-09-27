# %% libraries
import pandas as pd
from pymongo import MongoClient
from sshtunnel import SSHTunnelForwarder

# %% open mongo pipeline
'''
mongo is runnining on a server
'''
# --+ params
mongo_host = "10.16.142.91"
mongo_db = "onlineForums"
mongo_user = "simone"
mongo_pass = "DELL123"
# --+ server
server = SSHTunnelForwarder(
    mongo_host,
    ssh_username=mongo_user,
    ssh_password=mongo_pass,
    remote_bind_address=('127.0.0.1', 27017)
)
# --+ start server
server.start()
# --+ create client
client = MongoClient('127.0.0.1', server.local_bind_port)
# --+ target db
db = client[mongo_db]

# %%
# --+ demography
d = pd.DataFrame(list(db['AgentsDemographics'].find()))
# --+ agents' activities

a = pd.DataFrame(list(db['voice_no_schedule_no_demog'].find()))

# --+ schedule
s = pd.DataFrame(list(db['schedule_data'].find()))
# --+ WfH treatment
t = pd.DataFrame(list(db['wfh_stats'].find())) 