from django.utils.translation import gettext_lazy as _
from django.http import Http404
from django.core.exceptions import PermissionDenied
from rest_framework.serializers import ValidationError
from rest_framework.views import exception_handler
from rest_framework.exceptions import (
        NotAuthenticated, AuthenticationFailed, PermissionDenied as PermissionDeniedDrf 
    )

from core.exceptions import CustomApiResponseException

# TODO: to create catalog of erros and it will make translation of the codes
def custom_exception_handler(exception, context):

    response = exception_handler(exception, context)
    error_response = {
        'error_general': 'error',
        'error_description': 'error',
        'errors': []
    }
    if type(exception) == Http404:
        error_response['error_general'] = 'NOT_FOUND'
        error_response['error_description'] = 'resource not found'
    elif type(exception) == PermissionDenied:
        error_response['error_general'] = 'not_permitted'
        error_response['error_description'] = 'permission denied'
    elif type(exception) == NotAuthenticated:
        error_response['error_general'] = 'not_auntheticated'
        error_response['error_description'] = 'missin credentials'
    elif type(exception) == PermissionDeniedDrf:
        error_response['error_general'] = 'permission_denied'
        error_response['error_description'] = 'You do not have permission to perform this action.'
    elif type(exception) == AuthenticationFailed:
        error_response['error_general'] = 'authentication_failed'
        error_response['error_description'] = _('Incorrect authentication credentials.')
    elif type(exception) == CustomApiResponseException:
        error_response = exception.get_data_error()
        response.status_code = exception.status_code
        if exception.headers is not None:
            response._headers.update(exception.headers)
    # error serializers validation
    if type(exception) == ValidationError:
        error_response['error_general'] = 'form_validation'
        error_response['error_description'] = "error body's fields"
        error_response['errors'] = exception.detail
    response.data = error_response
    return response
