import numpy as np
import pandas as pd
#import sys
#sys.path.append("../")

def read_round(filename):
    mask = [False, False, True, True, False, False, False, True, True]
    header = ["epic_number", "mix_mean", "mix_sd", "mix_neff", "mix_rhat", "logdeltaQ_mean", "logdeltaQ_sd", "logdeltaQ_neff", "logdeltaQ_rhat",
              "logQ0_mean", "logQ0_sd", "logQ0_neff", "logQ0_rhat", "logperiod_mean", "logperiod_sd", "logperiod_neff", "logperiod_rhat",
              "logamp_mean", "logamp_sd", "logamp_neff", "logamp_rhat", "logs2_mean", "logs2_sd", "logs2_neff", "logs2_rhat", "acfpeak"]
    with open(filename, "r") as file:
        lines = file.readlines()
        nstars = (np.int((len(lines)/7)))
        data = np.zeros((nstars, 26))
        for i in range(nstars):
            data[i, 0] = lines[7*i].split()[0]
            for j in range(6):
                data[i, 4*j+1:4*(j+1)+1] = np.array(lines[7*i+j].split())[mask]
            acfpeak = lines[7*i+6].split()[2]
            if "None" in acfpeak:
                data[i, 25] = np.nan
            else:
                data[i, 25] = acfpeak
    return pd.DataFrame(data=data, columns=header)

