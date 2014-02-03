#TODO: Pass config from Test object to H2O cloud builder
#TODO: Where will AWS instance info come from?
#TODO: Finish main in this runner.py (lines below)
#TODO: Debug & Examples

from h2oPerf import PerfUtils
#h2oPerf imports 

import sys
import os
import argparse
import shutil
import signal
import time
import random
import getpass
import re
import subprocess

def parse_args():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--wipe", action = 'store_true', help = "Wipes the output dir before starting.")
        parser.add_argument("--baseport", help = "The first port at which H2O starts searching for free ports.")
        parser.add_argument("--test", help = "If you only want to run one test, specify it like this.")
        parser.add_argument("--testlist", help = "A file containing a list of tests to run (for example the 'failed.txt' file from the output directory).")
        parser.add_argument("--testgroup", help = "Test a group of tests by function: pca, glm, kmeans, gbm, rf, algos, golden, munging")
        parser.add_argument("--usecloud", help = "ip:port of cloud to send tests to instead of starting clouds.")
        args = ""
        args = vars(parser.parse_args())
    except:
        parser.print_help()
        sys.exit(1)
    return args

def main(argv):
    script_name = os.path.basename(argv[0])
    test_root_output_dir = os.path.dirname(os.path.realpath(__file__))
    
    output_dir = os.path.join(test_root_output_dir, "results")
    
    test_root_dir = os.path.join(
                        os.path.dirname(test_root_output_dir), "tests")

    h2o_jar = os.path.abspath(
                  os.path.join(test_root_dir, "..", "..", "target", "h2o.jar"))

    if not os.path.exists(h2o_jar):
        print("")
        print("ERROR: H2O jar not found: " + h2o_jar)
        print("")
        sys.exit(1)
  
    #parse cmdline arguments
    args = parse_args()
    if args['wipe']:
        PerfUtils.wipe_output_dir()

    #new perfdb connection
    #new runner
    #build_test list
    
    signal.signal(signal.SIGINT, PerfUtils.signal_handler)
    signal.signal(signal.SIGTERM, PerfUtils.signal_handler)

    while True:
        time.sleep(4)
    #run tests
    #report summary

if __name__ == "__main__":
    main(sys.argv)
