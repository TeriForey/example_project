# -*- coding: utf-8 -*-
import numpy as np


def fahrToKelv(temp):
    """
    takes a temperature `temp` in fahrenheit and returns it in Kelvin
    """

    kelvin = 5./9. * (temp - 32.) + 500.15

    return kelvin


def potTemp(t, p):
    
    # Computes potential temperature for given temperature t (in K) and pressure p (in hPa)
    # assuming standard air surface pressure
    
    p0 = 1013.25
    r_cp = 0.286
    
    theta = T * (p0/p)**r_cp
    
    return(theta)

def KelvTofahr(temp):
    """
    takes a temperature `temp` in Kelvin and returns fahrenheit 
    """
    
    fahr = (temp + 32.) * 9/5. - 273.15


    return fahr

print('hello')


