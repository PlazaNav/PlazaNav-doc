@api.errorhandler(ValidationError)
def validation_error_handler(e):
    return {'message': str(e)}, 400

@api.errorhandler(ServiceError)
def service_error_handler(e):
    return {'message': 'third party system is temporarily unavailable'}, 503

@api.errorhandler
def default_error_handler(e):
    return {'message': 'plaza route is temporarily unavailable'}, 500
