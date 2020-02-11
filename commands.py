import re
import pathlib

def handle_message(contents, prefix):
    command = contents.lower()[len(prefix):].strip()
    if command == "help":
        return "helping...."
    elif command == "show" or not command:
        return get_epgp_ranking()
    else:
        print(f"received unknown command: {command}") #TODO: remove
        return f"Unknown command. Try `{prefix} help`"

def handle_fileupload(attachment):
    filename = attachment.filename
    url = attachment.url
    if pathlib.Path(filename).suffix == ".csv":
        print(f"Received csv file: {filename}, url: {url}")
    

def get_epgp_ranking():
    return "EPGP logs: blah blah"