import re

def handle_message(contents, prefix):
    command = contents.lower()[len(prefix):].strip()
    print(f"received command: `{command}`")#TODO: remove
    if command == "help":
        return "helping...."
    elif command == "show" or not command:
        return get_epgp_ranking()
    else:
        print(f"received unknown command: {command}")
        return f"Unknown command. Try `{prefix} help`"

def get_epgp_ranking():
    return "EPGP logs: blah blah"