import re
import pathlib
import io
import os.path

EPGP_LOG_DIRECTORY = "records"


def handle_message(contents, prefix):
    command = contents.lower()[len(prefix):].strip()  # you like that shit?
    if command == "help":
        return "helping...."
    elif command == "show" or not command:
        return get_epgp_ranking()
    else:
        print(f"received unknown command: {command}")  # TODO: remove
        return f"Unknown command. Try `{prefix} help`"


async def handle_fileupload(attachment):
    filename = attachment.filename
    p = pathlib.Path(f"{EPGP_LOG_DIRECTORY}/")
    p.mkdir(parents=True, exist_ok=True)
    if pathlib.Path(filename).suffix == ".csv":
        print(f"Received csv file: {filename}, url: {attachment.url}")
        fp = io.BytesIO()

        byteCount = await attachment.save(fp)
        with open(f'{EPGP_LOG_DIRECTORY}/{filename}', 'wb') as out:  # Open temporary file as bytes
            bytes = fp.read()
            # to string so we can nuke any pesky quotes
            string_data = bytes.decode("utf-8").replace('"', '')
            out.write(string_data.encode("utf-8"))
        print(f"Wrote {byteCount} bytes to {EPGP_LOG_DIRECTORY}/{filename}")


def get_epgp_ranking():
    # TODO: if local record doesnt exist, grab the attachment from latest message in the channel (iterate from first to last looking for attachment)
    return "EPGP logs: blah blah"
