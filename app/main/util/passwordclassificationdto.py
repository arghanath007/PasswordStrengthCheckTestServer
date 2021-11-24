from flask_restx import Namespace, fields


class PasswordClassificationDto:

    api = Namespace('Predicting the strength of the password', description='Enter your password')
    
    password_pred = api.model('password_pred',{
        'password' : fields.String(required = True, description="Password")
    })