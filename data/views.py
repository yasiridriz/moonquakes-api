from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from obspy import read, UTCDateTime
import matplotlib.pyplot as plot

from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import pandas
import csv

@api_view(['GET', 'POST'])
def get_coordinates(request):
    pd = pandas.read_csv("resources/nakamura_1979_sm_locations.csv")
    return Response(pd)


