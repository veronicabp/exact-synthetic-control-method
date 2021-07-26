import csv
from subprocess import call

call(["python3", "create_country_objects.py"])
call(["python3", "run_cpp_program.py"])
call(["python3", "analyze_results.py"])























