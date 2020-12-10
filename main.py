from qiskit import IBMQ
from algorithms import *
import matplotlib
import config

def main():
    """
    Main function.
    """
    try:
        IBMQ.save_account("config.ibm_key", overwrite = True)
    except NameError:
        raise Exception("You have not set up your config file correctly.")

    create_bell_state()

if __name__ == "__main__":
    main()
