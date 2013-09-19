# -*- coding: utf-8 -*-

# The imports in this file are order-sensitive

from __future__ import absolute_import
from flask import Flask

# First, make an app

app = Flask(__name__, instance_relative_config=True)

# Second, import the models and views

from . import views
# from . import models, views
# from .models import db