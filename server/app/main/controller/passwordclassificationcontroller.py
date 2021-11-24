from flask_restx import Resource
from app.main.service.passwordpredictionservice import passwordstrengthpredict
from app.main.util.passwordclassificationdto import PasswordClassificationDto
from flask import request
from flask import render_template, make_response

api = PasswordClassificationDto.api 
_password_pred = PasswordClassificationDto.password_pred

# @api.route('/predict')
# class PasswordPrediction(Resource):
#     @api.doc('Password Strength Prediction')
#     @api.expect(_password_pred) 
#     def post(self):
#         """Password Strength Prediction"""
#         return passwordstrengthpredict(request.json)


@api.route('/checker')
class HomePage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        status = 200
        message = ""
        color = ""
        print(message)
        return make_response(render_template("app.html", status = status, message = message, color = color), 200,headers)

    
    def post(self):
        headers = {'Content-Type': 'text/html'}
        message = ""
        data = {}
        data['password'] = request.form['password'] 
        response, status = passwordstrengthpredict(data)
        message = response['message']
        strength = response['data']
        if strength == '2':
            color = 'success'
        elif strength == '1':
            color = 'warning'

        else:
            color = 'danger'

        print(message)
        
        return make_response(render_template("app.html", message = message, status = status, color = color), 200,headers)