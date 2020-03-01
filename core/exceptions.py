from rest_framework.exceptions import APIException


class CustomApiResponseException(APIException):
    def __init__(self, error_general, error_description, status_code, headers=None):
        if isinstance(headers, (dict)) is not True:
            raise ValueError('headers must an object of type dict')
        self.error_general = error_general
        self.error_description = error_description
        self.status_code = status_code

    def get_data_error(self):
        return {
            'error_general': self.error_general,
            'error_descrition': self.error_description,
            'errors': []
        }


