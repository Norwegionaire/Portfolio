#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:33:57 2024

@author: abbas
"""

# This module contains utility functions for validations

def is_number(n):
    """Check if the input is a number (int or float)."""
    return isinstance(n, (int, float))
