from os import path
from flask_restx import Api
from flask import Blueprint

from app.main.config import authorizations, version

blueprint=Blueprint('api',__name__)

api=Api(blueprint, 
title='Classification for checking the strength of Passwords given by users', 
version='1.0', 
description='Output "0" means the password is weak, "1" means the password is average/medium, "2" means the password is good/strong', 
authorizations=authorizations)

from app.main.controller.passwordclassificationcontroller import  api as password_clf_ns

api.add_namespace(password_clf_ns,path='/password')