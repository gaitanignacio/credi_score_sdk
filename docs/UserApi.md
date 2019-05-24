# swagger_client.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](UserApi.md#login) | **POST** /login | Logs the user in
[**renew_token**](UserApi.md#renew_token) | **POST** /login/refreshToken | The user renews access token and refresh token
[**revoke_refresh_token**](UserApi.md#revoke_refresh_token) | **DELETE** /login/refreshToken | The user revokes a refresh token


# **login**
> AccessTokenResponse login(login_request)

Logs the user in

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
login_request = swagger_client.LoginRequest() # LoginRequest | 

try:
    # Logs the user in
    api_response = api_instance.login(login_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_token**
> AccessTokenResponse renew_token(renew_token_request)

The user renews access token and refresh token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
renew_token_request = swagger_client.RenewTokenRequest() # RenewTokenRequest | 

try:
    # The user renews access token and refresh token
    api_response = api_instance.renew_token(renew_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->renew_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **renew_token_request** | [**RenewTokenRequest**](RenewTokenRequest.md)|  | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_refresh_token**
> AccessTokenResponse revoke_refresh_token(refresh_token)

The user revokes a refresh token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
refresh_token = 'refresh_token_example' # str | The refresh token to be revoked

try:
    # The user revokes a refresh token
    api_response = api_instance.revoke_refresh_token(refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->revoke_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**| The refresh token to be revoked | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

