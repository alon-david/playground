# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import openapi_client
from openapi_client.models.http_validation_error import HTTPValidationError  # noqa: E501
from openapi_client.rest import ApiException

class TestHTTPValidationError(unittest.TestCase):
    """HTTPValidationError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HTTPValidationError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HTTPValidationError`
        """
        model = openapi_client.models.http_validation_error.HTTPValidationError()  # noqa: E501
        if include_optional :
            return HTTPValidationError(
                detail = None
            )
        else :
            return HTTPValidationError(
        )
        """

    def testHTTPValidationError(self):
        """Test HTTPValidationError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
