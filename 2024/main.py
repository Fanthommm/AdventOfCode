import os
import glob
import sys
from utils import *

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def get_days():
    return {x[0][2:]:x[0] for x in os.walk(".")}

def main(day = None, part = None):
    days = get_days()
    day = "day"+ str(day).zfill(2)
    print(days)
    if day in days:
        day_python_file = os.path.join(days[day], day + ".py")
        print(day_python_file)
        os.system("python " + day_python_file)
    #     parts = get_parts(day)
    #     part = day + "\\part" + str(part).zfill(2) + ".py"
    #     print(part)
    #     if part in parts:
            
    #     else:
    #         print("Not implemented")
    #     print("good")
    # else:
    #     return 1
    # print(get_parts(days['day01']))
    # print("Welcome to Advent of Code 2024!")



if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        day = int(sys.argv[1])
        # part = int(sys.argv[2])
        main(day)