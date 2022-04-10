import os
import shutil
import urllib.request
import gzip

OUTPUT_FOLDER = "data"


def download_files(start_from=0, until=78):
    for i in range(start_from, until + 1):
        filename = f"2022_place_canvas_history-{str(i).zfill(12)}.csv.gzip"
        print(f"Getting file: {filename}")
        download_url = f"https://placedata.reddit.com/data/canvas-history/{filename}"
        filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), OUTPUT_FOLDER, filename)
        urllib.request.urlretrieve(download_url, filepath)
        print(f"\tGot it!")


def unzip_files(start_from=0, until=78):
    for i in range(start_from, until + 1):
        filename = f"2022_place_canvas_history-{str(i).zfill(12)}.csv.gzip"
        print(f"Unzipping file: {filename}")
        output_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), OUTPUT_FOLDER, filename.replace(".csv.gzip", ".csv"))
        filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), OUTPUT_FOLDER, filename)
        with gzip.open(filepath, 'rb') as f_in:
            with open(output_filepath, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"\tDone!")


if __name__ == "__main__":
    download_files()
    unzip_files()
