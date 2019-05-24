# BatchWebServiceResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State of the execution. Can be of the following values:  - Pending: The batch execution was submitted but is not yet scheduled. Ready: The batch execution was submitted and can be executed. InProgress: The batch execution is currently being processed. Complete: The batch execution has been completed. | [optional] 
**completed_item_count** | **int** | Number of completed items in this batch operation. | [optional] 
**total_item_count** | **int** | Number of total items in this batch operation. | [optional] 
**parallel_count** | **int** | Number of parallel threads that are processing this batch operation. | [optional] 
**batch_execution_results** | [**list[WebServiceResult]**](WebServiceResult.md) | The responses of the individual executions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


