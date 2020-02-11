import re
import pathlib
import io
import os.path

EPGP_LOG_DIRECTORY="records"

def handle_message(contents, prefix):
    command = contents.lower()[len(prefix):].strip()
    if command == "help":
        return "helping...."
    elif command == "show" or not command:
        return get_epgp_ranking()
    else:
        print(f"received unknown command: {command}") #TODO: remove
        return f"Unknown command. Try `{prefix} help`"

async def handle_fileupload(attachment):
    filename = attachment.filename
    url = attachment.url
    p = pathlib.Path(f"{EPGP_LOG_DIRECTORY}/")
    p.mkdir(parents=True, exist_ok=True)
    if pathlib.Path(filename).suffix == ".csv":
        print(f"Received csv file: {filename}, url: {url}")
        fp = io.BytesIO()

        byteCount = await attachment.save(fp)
        with open(f'{EPGP_LOG_DIRECTORY}/{filename}','wb') as out: ## Open temporary file as bytes
            out.write(fp.read())
        print(f"Wrote {byteCount} bytes to {EPGP_LOG_DIRECTORY}/{filename}")

def get_epgp_ranking():
    return "EPGP logs: blah blah"