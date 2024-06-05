# Standard library imports
import os
import sys
import time
import json
import functools
import requests  # May not be needed


# Third-party library imports
import ee
import pandas as pd
import geopandas as gpd
import numpy as np
import geemap
from sidecar import Sidecar

# Initialize Earth Engine
# from parameters.config_gee import gee_cloud_project

from modules.gee_initialize import initialize_ee
initialize_ee()

# Custom module imports
from modules.agstack_to_gee import (
    start_agstack_session,
    get_agstack_token,
    register_fc_and_append_to_csv,
    add_geo_ids_to_csv_from_lookup_csv,
    add_geo_ids_to_feature_col_from_lookup_csv,
    add_empty_column_to_csv,
    remove_column_from_csv,
    read_geo_ids,
    geo_id_or_ids_to_feature_collection,
    shapefile_to_ee,
    ee_to_shapefile,
    geojson_to_ee, 
    geojson_to_shapefile,
    shapefile_to_geojson,
    register_fc_and_set_geo_id,
    add_geo_ids_to_feature_col_from_lookup_df,
)
from modules.file_to_ceo import (
    get_ceo_url,
    whisp_stats_shapefile_and_ceo_url,
)
from modules.utils import (
    collection_properties_to_df,
    remove_geometry_from_feature_collection,
    get_centroid,
)
from modules.tidy_tables import (
    whisp_risk,
    add_eudr_risk_col,
    add_indicators,
    select_years_in_range,
    create_wildcard_column_list,
    create_column_list_from_lookup,
    order_list_from_lookup,
)
from modules.stats import (
    get_stats,
    get_stats_formatted,
)
from parameters.config_runtime import (
    geo_id_column,
    out_directory,
    out_csv,
    out_shapefile, #to check
    cols_ind_1_treecover,
    cols_ind_2_commodities,
    cols_ind_3_dist_before_2020,
    cols_ind_4_dist_after_2020,
    geometry_area_column,
    geometry_type_column,
    plot_id_column,
    lookup_gee_datasets_df,
    keep_system_index,
    keep_original_properties,
    prefix_columns_list,
    threshold_to_drive,
)
from parameters.config_asr_url_info import (
    asset_registry_base,
    user_registry_base,
)
from parameters.config_asr_credentials import (
    email,
    password,
)


# Additional custom module imports
session = start_agstack_session(email, password, user_registry_base)
token = get_agstack_token(email, password, asset_registry_base)