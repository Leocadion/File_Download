import time
from prefect import flow, task


@flow(log_prints=True)
def download_files():

    time.sleep(3)

    print(f"Fetching filelist")
    get_filelist()
    
    print(f"Downloading data")
    download_data()

    print(f"Writing files")
    write_files()
    
    print(f"All files have been downloaded")


@task
def get_filelist():
    time.sleep(6)

@task
def download_data():
    time.sleep(8)

@task
def write_files():
    time.sleep(3)

if __name__ == "__main__":
    download_files()