from qiskit import IBMQ
from algorithms import *
import config

def main():
    deutsch_jozsa()

def loadIBM():
    """
    Loads IBM account to access real hardware to run circuits on. You need to call this function to run your circuit in hardware; if you only want to simulate the circuit in your local machine, there is no need to call it.
    """
    try:
        IBMQ.load_account()
    except Exception:
        try:
            IBMQ.save_account(f"{config.IBM_KEY}", overwrite = True)
        except NameError:
            raise Exception("You have not set up your config file correctly.")

if __name__ == "__main__":
    main()
