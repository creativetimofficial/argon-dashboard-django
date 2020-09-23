# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class Test(object):
    """docstring for Test."""
    test = models.CharField(verbose_name='Teste')

    def is_valid(self):
        return true
