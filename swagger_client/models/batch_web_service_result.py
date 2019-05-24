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

from swagger_client.models.web_service_result import WebServiceResult  # noqa: F401,E501


class BatchWebServiceResult(object):
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
        'state': 'str',
        'completed_item_count': 'int',
        'total_item_count': 'int',
        'parallel_count': 'int',
        'batch_execution_results': 'list[WebServiceResult]'
    }

    attribute_map = {
        'state': 'state',
        'completed_item_count': 'completedItemCount',
        'total_item_count': 'totalItemCount',
        'parallel_count': 'parallelCount',
        'batch_execution_results': 'batchExecutionResults'
    }

    def __init__(self, state=None, completed_item_count=None, total_item_count=None, parallel_count=None, batch_execution_results=None):  # noqa: E501
        """BatchWebServiceResult - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._completed_item_count = None
        self._total_item_count = None
        self._parallel_count = None
        self._batch_execution_results = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if completed_item_count is not None:
            self.completed_item_count = completed_item_count
        if total_item_count is not None:
            self.total_item_count = total_item_count
        if parallel_count is not None:
            self.parallel_count = parallel_count
        if batch_execution_results is not None:
            self.batch_execution_results = batch_execution_results

    @property
    def state(self):
        """Gets the state of this BatchWebServiceResult.  # noqa: E501

        State of the execution. Can be of the following values:  - Pending: The batch execution was submitted but is not yet scheduled. Ready: The batch execution was submitted and can be executed. InProgress: The batch execution is currently being processed. Complete: The batch execution has been completed.  # noqa: E501

        :return: The state of this BatchWebServiceResult.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BatchWebServiceResult.

        State of the execution. Can be of the following values:  - Pending: The batch execution was submitted but is not yet scheduled. Ready: The batch execution was submitted and can be executed. InProgress: The batch execution is currently being processed. Complete: The batch execution has been completed.  # noqa: E501

        :param state: The state of this BatchWebServiceResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "inProgress", "ready", "complete"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def completed_item_count(self):
        """Gets the completed_item_count of this BatchWebServiceResult.  # noqa: E501

        Number of completed items in this batch operation.  # noqa: E501

        :return: The completed_item_count of this BatchWebServiceResult.  # noqa: E501
        :rtype: int
        """
        return self._completed_item_count

    @completed_item_count.setter
    def completed_item_count(self, completed_item_count):
        """Sets the completed_item_count of this BatchWebServiceResult.

        Number of completed items in this batch operation.  # noqa: E501

        :param completed_item_count: The completed_item_count of this BatchWebServiceResult.  # noqa: E501
        :type: int
        """

        self._completed_item_count = completed_item_count

    @property
    def total_item_count(self):
        """Gets the total_item_count of this BatchWebServiceResult.  # noqa: E501

        Number of total items in this batch operation.  # noqa: E501

        :return: The total_item_count of this BatchWebServiceResult.  # noqa: E501
        :rtype: int
        """
        return self._total_item_count

    @total_item_count.setter
    def total_item_count(self, total_item_count):
        """Sets the total_item_count of this BatchWebServiceResult.

        Number of total items in this batch operation.  # noqa: E501

        :param total_item_count: The total_item_count of this BatchWebServiceResult.  # noqa: E501
        :type: int
        """

        self._total_item_count = total_item_count

    @property
    def parallel_count(self):
        """Gets the parallel_count of this BatchWebServiceResult.  # noqa: E501

        Number of parallel threads that are processing this batch operation.  # noqa: E501

        :return: The parallel_count of this BatchWebServiceResult.  # noqa: E501
        :rtype: int
        """
        return self._parallel_count

    @parallel_count.setter
    def parallel_count(self, parallel_count):
        """Sets the parallel_count of this BatchWebServiceResult.

        Number of parallel threads that are processing this batch operation.  # noqa: E501

        :param parallel_count: The parallel_count of this BatchWebServiceResult.  # noqa: E501
        :type: int
        """

        self._parallel_count = parallel_count

    @property
    def batch_execution_results(self):
        """Gets the batch_execution_results of this BatchWebServiceResult.  # noqa: E501

        The responses of the individual executions.  # noqa: E501

        :return: The batch_execution_results of this BatchWebServiceResult.  # noqa: E501
        :rtype: list[WebServiceResult]
        """
        return self._batch_execution_results

    @batch_execution_results.setter
    def batch_execution_results(self, batch_execution_results):
        """Sets the batch_execution_results of this BatchWebServiceResult.

        The responses of the individual executions.  # noqa: E501

        :param batch_execution_results: The batch_execution_results of this BatchWebServiceResult.  # noqa: E501
        :type: list[WebServiceResult]
        """

        self._batch_execution_results = batch_execution_results

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
        if issubclass(BatchWebServiceResult, dict):
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
        if not isinstance(other, BatchWebServiceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other