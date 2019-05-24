# coding: utf-8

"""
    predictor_scoring

    Credit Score Predictor  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.output_parameters import OutputParameters  # noqa: F401,E501


class WebServiceResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'success': 'bool',
        'error_message': 'str',
        'console_output': 'str',
        'changed_files': 'list[str]',
        'output_parameters': 'OutputParameters'
    }

    attribute_map = {
        'success': 'success',
        'error_message': 'errorMessage',
        'console_output': 'consoleOutput',
        'changed_files': 'changedFiles',
        'output_parameters': 'outputParameters'
    }

    def __init__(self, success=None, error_message=None, console_output=None, changed_files=None, output_parameters=None):  # noqa: E501
        """WebServiceResult - a model defined in Swagger"""  # noqa: E501

        self._success = None
        self._error_message = None
        self._console_output = None
        self._changed_files = None
        self._output_parameters = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if error_message is not None:
            self.error_message = error_message
        if console_output is not None:
            self.console_output = console_output
        if changed_files is not None:
            self.changed_files = changed_files
        if output_parameters is not None:
            self.output_parameters = output_parameters

    @property
    def success(self):
        """Gets the success of this WebServiceResult.  # noqa: E501

        Boolean flag indicating the success status of web service execution.  # noqa: E501

        :return: The success of this WebServiceResult.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this WebServiceResult.

        Boolean flag indicating the success status of web service execution.  # noqa: E501

        :param success: The success of this WebServiceResult.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def error_message(self):
        """Gets the error_message of this WebServiceResult.  # noqa: E501

        Error messages if any occurred during the web service execution.  # noqa: E501

        :return: The error_message of this WebServiceResult.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this WebServiceResult.

        Error messages if any occurred during the web service execution.  # noqa: E501

        :param error_message: The error_message of this WebServiceResult.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def console_output(self):
        """Gets the console_output of this WebServiceResult.  # noqa: E501

        Console output from the web service execution.  # noqa: E501

        :return: The console_output of this WebServiceResult.  # noqa: E501
        :rtype: str
        """
        return self._console_output

    @console_output.setter
    def console_output(self, console_output):
        """Sets the console_output of this WebServiceResult.

        Console output from the web service execution.  # noqa: E501

        :param console_output: The console_output of this WebServiceResult.  # noqa: E501
        :type: str
        """

        self._console_output = console_output

    @property
    def changed_files(self):
        """Gets the changed_files of this WebServiceResult.  # noqa: E501

        The filenames of the files modified during the web service execution.  # noqa: E501

        :return: The changed_files of this WebServiceResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._changed_files

    @changed_files.setter
    def changed_files(self, changed_files):
        """Sets the changed_files of this WebServiceResult.

        The filenames of the files modified during the web service execution.  # noqa: E501

        :param changed_files: The changed_files of this WebServiceResult.  # noqa: E501
        :type: list[str]
        """

        self._changed_files = changed_files

    @property
    def output_parameters(self):
        """Gets the output_parameters of this WebServiceResult.  # noqa: E501


        :return: The output_parameters of this WebServiceResult.  # noqa: E501
        :rtype: OutputParameters
        """
        return self._output_parameters

    @output_parameters.setter
    def output_parameters(self, output_parameters):
        """Sets the output_parameters of this WebServiceResult.


        :param output_parameters: The output_parameters of this WebServiceResult.  # noqa: E501
        :type: OutputParameters
        """

        self._output_parameters = output_parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WebServiceResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebServiceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other