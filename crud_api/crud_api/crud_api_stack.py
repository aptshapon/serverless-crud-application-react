from sys import path
from aws_cdk import (aws_lambda as _lambda,
                     core)
from aws_cdk.aws_apigatewayv2 import (
    HttpApi, HttpMethod, CorsHttpMethod)
from aws_cdk.aws_apigatewayv2_integrations import LambdaProxyIntegration


class DockerApiStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    # Create API
        lambda_post_fn = _lambda.Function(self, "CrudApiHandler",
                                          code=_lambda.Code.asset('lambda'),
                                          handler="create.handler",
                                          runtime=_lambda.Runtime.PYTHON_3_8,
                                          timeout=core.Duration.seconds(900),
                                          environment={'NAME': 'CrudApiHandler'})

        post_books_integration = LambdaProxyIntegration(handler=lambda_post_fn)

        http_api = HttpApi(self, 'CrudApi',
                    api_name='crud_api',
                    cors_preflight={
                        "allow_headers": ["*"],
                        "allow_origins": ["*"],
                        "expose_headers": ["*"],
                        "allow_methods": [CorsHttpMethod.POST, CorsHttpMethod.OPTIONS],
                        "max_age": core.Duration.days(10)})
        http_api.add_routes(
            path='/books',
            methods=[HttpMethod.POST],
            integration=post_books_integration)

    # Read API
        lambda_get_fn = _lambda.Function(self, "GetApiHandler",
                                         code=_lambda.Code.asset('lambda'),
                                         handler="read.handler",
                                         runtime=_lambda.Runtime.PYTHON_3_8,
                                         timeout=core.Duration.seconds(900),
                                         environment={'NAME': 'GetApiHandler'})
        get_books_integration = LambdaProxyIntegration(
            handler=lambda_get_fn)

        read_api = HttpApi(self, 'ReaddApi',
                    api_name='read_api',
                    cors_preflight={
                        "allow_headers": ["*"],
                        "allow_origins": ["*"],
                        "allow_methods": [CorsHttpMethod.GET, CorsHttpMethod.OPTIONS],
                        "max_age": core.Duration.days(10)})
        read_api.add_routes(
            path='/books',
            methods=[HttpMethod.GET],
            integration=get_books_integration)

    # UPDATE API
        lambda_put_fn = _lambda.Function(self, "PutApiHandler",
                                         code=_lambda.Code.asset('lambda'),
                                         handler="update.handler",
                                         runtime=_lambda.Runtime.PYTHON_3_8,
                                         timeout=core.Duration.seconds(900),
                                         environment={'NAME': 'PutApiHandler'},
                                         )
        put_books_integration = LambdaProxyIntegration(
            handler=lambda_put_fn)
        
        put_api = HttpApi(self, 'PutApi',
                    api_name='put_api',
                    cors_preflight={
                        "allow_headers": ["*"],
                        "allow_origins": ["*"],
                        "allow_methods": [CorsHttpMethod.PUT, CorsHttpMethod.OPTIONS],
                        "max_age": core.Duration.days(10)})

        put_api.add_routes(
            path='/book/{id}',
            methods=[HttpMethod.PUT],
            integration=put_books_integration)

    # DELETE API
        lambda_delete_fn = _lambda.Function(self, "DeleteApiHandler",
                                         code=_lambda.Code.asset('lambda'),
                                         handler="delete.handler",
                                         runtime=_lambda.Runtime.PYTHON_3_8,
                                         timeout=core.Duration.seconds(900),
                                         environment={'NAME': 'DeleteApiHandler'},
                                         )
        delete_books_integration = LambdaProxyIntegration(
            handler=lambda_delete_fn)
        
        delete_api = HttpApi(self, 'DeletetApi',
                    api_name='delete_api',
                    cors_preflight={
                        "allow_headers": ["*"],
                        "allow_origins": ["*"],
                        "allow_methods": [ CorsHttpMethod.OPTIONS, CorsHttpMethod.DELETE],
                        "max_age": core.Duration.days(10)})

        delete_api.add_routes(
            path='/book/{id}',
            methods=[HttpMethod.DELETE],
            integration=delete_books_integration)

        core.CfnOutput(self, 'get_url', value=read_api.url)
        core.CfnOutput(self, 'create_url', value=http_api.url)
        core.CfnOutput(self, 'update_url', value=put_api.url)
        core.CfnOutput(self, 'delete_url', value=delete_api.url)