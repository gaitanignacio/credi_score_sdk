# swagger_client.PredictorScoringApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_and_delete_batch_execution**](PredictorScoringApi.md#cancel_and_delete_batch_execution) | **DELETE** /api/predictor_scoring/1.0/batch/{executionId} | Cancels and deletes all batch executions for predictor_scoring.
[**get_batch_execution_file**](PredictorScoringApi.md#get_batch_execution_file) | **GET** /api/predictor_scoring/1.0/batch/{executionId}/{index}/files/{fileName} | Gets a specific file from an execution in predictor_scoring.
[**get_batch_execution_files**](PredictorScoringApi.md#get_batch_execution_files) | **GET** /api/predictor_scoring/1.0/batch/{executionId}/{index}/files | Gets all files from an individual execution in predictor_scoring.
[**get_batch_execution_status**](PredictorScoringApi.md#get_batch_execution_status) | **GET** /api/predictor_scoring/1.0/batch/{executionId} | Gets all batch executions for predictor_scoring.
[**get_batch_executions**](PredictorScoringApi.md#get_batch_executions) | **GET** /api/predictor_scoring/1.0/batch | Gets all batch executions for predictor_scoring.
[**predictor_scoring**](PredictorScoringApi.md#predictor_scoring) | **POST** /api/predictor_scoring/1.0 | 
[**start_batch_execution**](PredictorScoringApi.md#start_batch_execution) | **POST** /api/predictor_scoring/1.0/batch | 


# **cancel_and_delete_batch_execution**
> list[str] cancel_and_delete_batch_execution(execution_id)

Cancels and deletes all batch executions for predictor_scoring.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PredictorScoringApi(swagger_client.ApiClient(configuration))
execution_id = 'execution_id_example' # str | Execution id of the execution.

try:
    # Cancels and deletes all batch executions for predictor_scoring.
    api_response = api_instance.cancel_and_delete_batch_execution(execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictorScoringApi->cancel_and_delete_batch_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| Execution id of the execution. | 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_execution_file**
> file get_batch_execution_file(execution_id, index, file_name)

Gets a specific file from an execution in predictor_scoring.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PredictorScoringApi(swagger_client.ApiClient(configuration))
execution_id = 'execution_id_example' # str | Execution id of the execution
index = 56 # int | Index of the execution in the batch.
file_name = 'file_name_example' # str | Name of the file to be returned.

try:
    # Gets a specific file from an execution in predictor_scoring.
    api_response = api_instance.get_batch_execution_file(execution_id, index, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictorScoringApi->get_batch_execution_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| Execution id of the execution | 
 **index** | **int**| Index of the execution in the batch. | 
 **file_name** | **str**| Name of the file to be returned. | 

### Return type

[**file**](file.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_execution_files**
> list[str] get_batch_execution_files(execution_id, index)

Gets all files from an individual execution in predictor_scoring.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PredictorScoringApi(swagger_client.ApiClient(configuration))
execution_id = 'execution_id_example' # str | Execution id of the execution
index = 56 # int | Index of the execution in the batch.

try:
    # Gets all files from an individual execution in predictor_scoring.
    api_response = api_instance.get_batch_execution_files(execution_id, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictorScoringApi->get_batch_execution_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| Execution id of the execution | 
 **index** | **int**| Index of the execution in the batch. | 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_execution_status**
> BatchWebServiceResult get_batch_execution_status(execution_id, show_partial_results=show_partial_results)

Gets all batch executions for predictor_scoring.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PredictorScoringApi(swagger_client.ApiClient(configuration))
execution_id = 'execution_id_example' # str | Execution id of the execution
show_partial_results = true # bool | Returns the already processed results of the batch execution even if it hasn't been fully completed. (optional)

try:
    # Gets all batch executions for predictor_scoring.
    api_response = api_instance.get_batch_execution_status(execution_id, show_partial_results=show_partial_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictorScoringApi->get_batch_execution_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| Execution id of the execution | 
 **show_partial_results** | **bool**| Returns the already processed results of the batch execution even if it hasn&#39;t been fully completed. | [optional] 

### Return type

[**BatchWebServiceResult**](BatchWebServiceResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_executions**
> list[str] get_batch_executions()

Gets all batch executions for predictor_scoring.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PredictorScoringApi(swagger_client.ApiClient(configuration))

try:
    # Gets all batch executions for predictor_scoring.
    api_response = api_instance.get_batch_executions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictorScoringApi->get_batch_executions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predictor_scoring**
> WebServiceResult predictor_scoring(web_service_parameters)



Consume the predictor_scoring web service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PredictorScoringApi(swagger_client.ApiClient(configuration))
web_service_parameters = swagger_client.InputParameters() # InputParameters | Input parameters to the web service.

try:
    api_response = api_instance.predictor_scoring(web_service_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictorScoringApi->predictor_scoring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_service_parameters** | [**InputParameters**](InputParameters.md)| Input parameters to the web service. | 

### Return type

[**WebServiceResult**](WebServiceResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_batch_execution**
> StartBatchExecutionResponse start_batch_execution(batch_web_service_parameters, parallel_count=parallel_count)



Consume the predictor_scoring web service asynchronously.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PredictorScoringApi(swagger_client.ApiClient(configuration))
batch_web_service_parameters = [swagger_client.InputParameters()] # list[InputParameters] | Input parameters to the web service.
parallel_count = 56 # int | Number of threads used to process entries in the batch. Default value is 10. Please make sure not to use too high of a number because it might negatively impact performance. (optional)

try:
    api_response = api_instance.start_batch_execution(batch_web_service_parameters, parallel_count=parallel_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictorScoringApi->start_batch_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_web_service_parameters** | [**list[InputParameters]**](InputParameters.md)| Input parameters to the web service. | 
 **parallel_count** | **int**| Number of threads used to process entries in the batch. Default value is 10. Please make sure not to use too high of a number because it might negatively impact performance. | [optional] 

### Return type

[**StartBatchExecutionResponse**](StartBatchExecutionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

