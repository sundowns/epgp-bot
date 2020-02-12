import re
import pathlib
import io
import os.path
import epgp

EPGP_LOGS_DIRECTORY = os.getenv('EPGP_LOGS_DIRECTORY', default='records')

def handle_message(contents, prefix):
    command = contents.lower()[len(prefix):].strip()  # you like that shit?
    if command == "help":
        return "helping...."
    elif command == "show" or not command:
        return epgp.get_top()
    else:
        print(f"received unknown command: {command}")  # TODO: remove
        return f"Unknown command. Try `{prefix} help`"


async def handle_fileupload(attachment):
    filename = attachment.filename
    p = pathlib.Path(f"{EPGP_LOGS_DIRECTORY}/")
    p.mkdir(parents=True, exist_ok=True)
    if pathlib.Path(filename).suffix == ".csv":
        print(f"Received csv file: {filename}, url: {attachment.url}")
        fp = io.BytesIO()

        byteCount = await attachment.save(fp)
        with open(f'{EPGP_LOGS_DIRECTORY}/{filename}', 'wb') as out:  # Open temporary file as bytes
            bytes = fp.read()
            # to string so we can nuke any pesky quotes
            string_data = bytes.decode("utf-8").replace('"', '')
            out.write(string_data.encode("utf-8"))
        print(f"Wrote {byteCount} bytes to {EPGP_LOGS_DIRECTORY}/{filename}")
        epgp.set_epgp_file(filename)

