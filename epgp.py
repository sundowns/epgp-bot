import os
import pandas

EPGP_LOGS_DIRECTORY = os.getenv('EPGP_LOGS_DIRECTORY', default='records')

EPGP_LOGS_LOADED = False
EPGP_LOG_FILE = None

def set_epgp_file(filename):
    print(f"EPGP log file loaded: {filename}")
    global EPGP_LOG_FILE
    EPGP_LOG_FILE=filename
    global EPGP_LOGS_LOADED
    EPGP_LOGS_LOADED = True

# Get the top x number of members by PR (EP/GP)
def get_top(count=50):
    if not EPGP_LOGS_LOADED: 
        get_latest_log_file()

    df = pandas.read_csv(f"{EPGP_LOGS_DIRECTORY}/{EPGP_LOG_FILE}", 
        names=['Character','Class','Role','EP','GP','PR'])
    return str(df.head())

def get_latest_log_file():
    # TODO: no idea yet lol, I guess iterate the channels messages from latest backwards looking for attachments
    # global EPGP_LOGS_LOADED
    # EPGP_LOGS_LOADED = True
    assert False, "No log file loaded dummy"