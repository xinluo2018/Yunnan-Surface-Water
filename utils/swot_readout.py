### author: xin luo 
### create: 2025.2.9
### des: read the SWOT data and select the variables within the given geometry.

import numpy as np
import xarray as xr
import geopandas as gpd


def swot_pixc_readout(path_file, vars_sel=None, region_gpd=None):
    """
    des: read the SWOT_L2_HR_PIXC data and select the variables within the given geometry.    
    args:
      path_file (str): path to the SWOT PIXC .nc file.
      vars (list): list of variables to be selected.
      region_gpd (geopandas): the geometry to be used for selecting the data.    
    returns:
      pix_vars_geo (xarray): the selected variables within the geometry.
    """
    # Select main variables to be written out
    if vars_sel is None:
      vars_sel = ['latitude', 'longitude', 'height', \
                'solid_earth_tide', 'pole_tide', \
                'load_tide_fes', 'iono_cor_gim_ka', 'geoid',\
                'pixel_area','geolocation_qual']    
    # Read the SWOT PIXC data
    pixc_nc = xr.open_dataset(path_file, group='pixel_cloud')
    
    # Select main variables to be written out
    pixc_vars = pixc_nc[vars_sel]
   
    if region_gpd is not None:
      # Remove variables outside the vector geometry
      points = gpd.GeoDataFrame(geometry=gpd.points_from_xy(pixc_vars.longitude, pixc_vars.latitude))
      id_points_in_geom = points.sindex.query(region_gpd.geometry.unary_union, predicate='contains')
      pixc_vars = pixc_vars.isel(points=id_points_in_geom )
    if pixc_vars.sizes['points'] == 0:
      print(f"No points found within the geometry")
      return None    
    # Define the output path
    path_readout = path_file.split('.')[0]+'_readout.nc'
    # Write the selected variables to a new .nc file
    pixc_vars.to_netcdf(path_readout)
    print(f"file read and written to {path_readout}")
    return pixc_vars

