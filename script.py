import pandas as pd
import os
from datetime import datetime


def console_commands():
    try:
        command = "getmac" # command to automate
        response = os.popen(command).read()
        # add date
        date_create = datetime.now()
        date_create = str(date_create)
        date_create = date_create[0:19]
        # write response in file txt
        with open("response.txt","w", encoding="utf-8") as f:
            f.writelines(response + "\n\n")
            f.write(date_create)
            f.close()
    except Exception as excpt:
        print("*File creation error " + str(excpt))


def run():
    console_commands()


if __name__ == "__main__":
    run()