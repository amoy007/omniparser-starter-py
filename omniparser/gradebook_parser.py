# omniparser/gradebook_parser.py

import os #the "os" module allows you to use this on either operating system. Does not need to be installed, just imported.
import statistics

import pandas #helps open CSV files.

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)

    avg_grade = df["final_grade"].mean()
    return avg_grade #90.64 #"OOPS"

    #Alternative 1of3
    #breakpoint()
    # avg_grade = df["final_grade"].mean()

    #Alternative 2of3
    #breakpoint()
    #rows = df.to_dict("records")
    #grades = [r["final_grade"] for r in rows] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5]
    #avg_grade = statistics.mean(grades)
    
    #Alternative 3of3
    #breakpoint()
    #grades =  df["final_grade"].to_list()
    #avg_grade = statistics.mean(grades)

    

if __name__ == "__main__": #the metadata for __name__ is "__main__"
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    #Alternatives
    #gradebook_filepath = "C:/Users/alice.moy/Desktop/ProPython/GitHub/omniparser-starter-py/data/gradebook_2019.csv"
    #gradebook_filepath = "data/gradebook_2019.csv"
          
    #the metadata for __file__ is 'omniparser/gradebook_parser.py'

    print(gradebook_filepath)
    #breakpoint() #In Git Bash, when you run python omniparser/gradebook_parser.py, you can get into the (pdb) debugger mode on the command line.

    avg = calculate_average_grade_from_csv(gradebook_filepath)
    print(avg)