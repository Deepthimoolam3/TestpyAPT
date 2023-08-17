import os
from pyats.easypy import run

# All run() must be inside a main function
def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(test_path, 'SamppleTest.py')

    # Execute the testscript
    run(testscript=testscript)