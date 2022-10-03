from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from obspy import read, UTCDateTime
import numpy as np
import matplotlib.pyplot as plot

from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import pandas
import csv

@api_view(['GET'])
def get_data(request): 
    sm = pandas.read_csv('resources/nakamura_1979_sm_locations.csv')
    ai = pandas.read_csv('resources/nakamura_1983_ai_locations.csv')
    dm = pandas.read_csv('resources/nakamura_2005_dm_locations.csv')
    
    sml = sm[["Lat", "Long", "Year", "Magnitude"]]
    ail = ai[["Lat", "Long", "Y"]]
    dml = dm[["Lat", "Long", "Depth"]]

    sml = sml[~sml.isin([np.nan, np.inf, -np.inf]).any(1)]
    ail = ail[~ail.isin([np.nan, np.inf, -np.inf]).any(1)]
    dml = dml[~dml.isin([np.nan, np.inf, -np.inf]).any(1)]
        

    return Response({
        "SM": sml,
        "DM": dml,
        "AI": ail
    })


