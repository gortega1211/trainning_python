import pathlib
import time
from contextlib import suppress

temporary_file = pathlib.Path("resources/transactions.txt")
main_file = pathlib.Path("resources/all_transactions.txt")

while True:
    archive_path = temporary_file.with_suffix(f".arch_{time.time()}")
    with suppress(FileNotFoundError):
        with temporary_file.open(mode="rt") as transactions:
            with main_file.open(mode="at") as main:
                print("Found new transactions, updating log & archiving.")
                main.writelines(transactions.readlines())
        temporary_file.replace(archive_path)
    time.sleep(3)