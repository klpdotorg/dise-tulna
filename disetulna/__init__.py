# -*- coding: utf-8 -*-

# The imports in this file are order-sensitive

from __future__ import absolute_import
from flask import Flask
from flask.ext.assets import Environment, Bundle

# First, make an app

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('settings.py', silent=True)
assets = Environment(app)

css = Bundle('js/libs/bootstrap/css/bootstrap.min.css',
	'css/app.css')

js = Bundle('js/libs/jquery/jquery1.10.js',
			'js/libs/bootstrap/js/bootstrap.min.js',
			'js/app.js',
            filters='jsmin', output='js/packed.js')

assets.register('js_all', js)
assets.register('css_all', css)

# Second, import the models and views

from . import views
# from . import models, views
# from .models import db