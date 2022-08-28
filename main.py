import os
import pandas as pd
import numpy as np
import utilities as ut
import datetime as dt

def main():
    
    # fetch all the levels
    lvls = list(ut.getTimeDelta().keys())
    exp_path = 'Cryps/'
    
    for lvl in lvls:
        ut.exportAllHistoricalData(level = lvl,export_path=exp_path)
    
if __name__ == '__main__':
    main()