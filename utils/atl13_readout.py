# author: xin luo
# create: 2025.10.14.   
# des: read in and write out reorganized atl13 data

'''
des: 1. read icesat2 alt13 data and extract parameters of lon, lat, h_water and date. 
'''

import os
import h5py
import numpy as np
from astropy.time import Time

def gps2dyr(gps_seconds):
    time_gps = Time(gps_seconds, format="gps")
    time_dyr = Time(time_gps, format="decimalyear").value
    return time_dyr

def read_atl13(path_in, path_out):
    # Create dictionary for saving output variables
    out_keys = ['h', 'lon', 'lat', 't_dyr']   ## output variables
    d, d_update = {}, {}     
    for key in out_keys: 
        d[key]=np.array([]); 
        d_update[key]=np.array([]); 

    #-----------------------------------#
    # 1) Read data for beams         #
    #-----------------------------------#
    group = ["./gt1l", "./gt1r", "./gt2l", "./gt2r", "./gt3l", "./gt3r"]
    ## loop for groups
    for k in range(len(group)):
        with h5py.File(path_in, "r") as fi:
            try:
                ## group varibales:
                d['h'] = fi[group[k] + "/ht_ortho"][:]
                d['lat'] = fi[group[k] + "/sseg_mean_lat"][:]
                d['lon'] = fi[group[k] + "/sseg_mean_lon"][:]
                d['t_dt'] = fi[group[k] + "/sseg_mean_time"][:]
                ## dset varibales
                d['tref'] = fi["ancillary_data/atlas_sdp_gps_epoch"][:] 
            except:
                print(("missing group:", group[k]))
                print(("in file:", path_in))
                continue
        ## convert time to decimal years
        t_gps = d['t_dt'] + d['tref']
        d['t_dyr'] = gps2dyr(t_gps)      # time in decimal years

        for key in out_keys:
            d_update[key] = np.append(d_update[key], d[key])

    #------------------------------------------#
    # 3) Writting out the selected data        #
    #------------------------------------------#
    with h5py.File(path_out, "w") as f_out:
        [f_out.create_dataset(key, data=d_update[key]) for key in out_keys]
    print('written file:', path_out)
    return

