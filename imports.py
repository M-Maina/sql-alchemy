#Absolute vs Relative


#import library imports
import datetime
import os

#Third party imports
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

#Local application imports
from local_module import local_class
from local_package import local_function



#relative
from . import class1
