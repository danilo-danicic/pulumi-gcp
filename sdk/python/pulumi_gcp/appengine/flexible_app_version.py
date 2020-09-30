# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['FlexibleAppVersion']


class FlexibleAppVersion(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_config: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionApiConfigArgs']]] = None,
                 automatic_scaling: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionAutomaticScalingArgs']]] = None,
                 beta_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 default_expiration: Optional[pulumi.Input[str]] = None,
                 delete_service_on_destroy: Optional[pulumi.Input[bool]] = None,
                 deployment: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionDeploymentArgs']]] = None,
                 endpoints_api_service: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionEndpointsApiServiceArgs']]] = None,
                 entrypoint: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionEntrypointArgs']]] = None,
                 env_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 handlers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlexibleAppVersionHandlerArgs']]]]] = None,
                 inbound_services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 instance_class: Optional[pulumi.Input[str]] = None,
                 liveness_check: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionLivenessCheckArgs']]] = None,
                 manual_scaling: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionManualScalingArgs']]] = None,
                 network: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionNetworkArgs']]] = None,
                 nobuild_files_regex: Optional[pulumi.Input[str]] = None,
                 noop_on_destroy: Optional[pulumi.Input[bool]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 readiness_check: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionReadinessCheckArgs']]] = None,
                 resources: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionResourcesArgs']]] = None,
                 runtime: Optional[pulumi.Input[str]] = None,
                 runtime_api_version: Optional[pulumi.Input[str]] = None,
                 runtime_channel: Optional[pulumi.Input[str]] = None,
                 runtime_main_executable_path: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 serving_status: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None,
                 vpc_access_connector: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionVpcAccessConnectorArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Flexible App Version resource to create a new version of flexible GAE Application. Based on Google Compute Engine,
        the App Engine flexible environment automatically scales your app up and down while also balancing the load.
        Learn about the differences between the standard environment and the flexible environment
        at https://cloud.google.com/appengine/docs/the-appengine-environments.

        > **Note:** The App Engine flexible environment service account uses the member ID `service-[YOUR_PROJECT_NUMBER]@gae-api-prod.google.com.iam.gserviceaccount.com`
        It should have the App Engine Flexible Environment Service Agent role, which will be applied when the `appengineflex.googleapis.com` service is enabled.

        To get more information about FlexibleAppVersion, see:

        * [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/appengine/docs/flexible)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionApiConfigArgs']] api_config: Serving configuration for Google Cloud Endpoints.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionAutomaticScalingArgs']] automatic_scaling: Automatic scaling is based on request rate, response latencies, and other application metrics.
               Structure is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] beta_settings: Metadata settings that are supplied to this version to enable beta runtime features.
        :param pulumi.Input[str] default_expiration: Duration that static files should be cached by web proxies and browsers.
               Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time.
        :param pulumi.Input[bool] delete_service_on_destroy: If set to `true`, the service will be deleted if it is the last version.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionDeploymentArgs']] deployment: Code and application artifacts that make up this version.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionEndpointsApiServiceArgs']] endpoints_api_service: Code and application artifacts that make up this version.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionEntrypointArgs']] entrypoint: The entrypoint for the application.
               Structure is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] env_variables: Environment variables available to the application.  As these are not returned in the API request, the provider will not detect any changes made outside of the config.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlexibleAppVersionHandlerArgs']]]] handlers: An ordered list of URL-matching patterns that should be applied to incoming requests.
               The first matching URL handles the request and other request handlers are not attempted.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inbound_services: A list of the types of messages that this application is able to receive.
               Each value may be one of `INBOUND_SERVICE_MAIL`, `INBOUND_SERVICE_MAIL_BOUNCE`, `INBOUND_SERVICE_XMPP_ERROR`, `INBOUND_SERVICE_XMPP_MESSAGE`, `INBOUND_SERVICE_XMPP_SUBSCRIBE`, `INBOUND_SERVICE_XMPP_PRESENCE`, `INBOUND_SERVICE_CHANNEL_PRESENCE`, and `INBOUND_SERVICE_WARMUP`.
        :param pulumi.Input[str] instance_class: Instance class that is used to run this version. Valid values are
               AutomaticScaling: F1, F2, F4, F4_1G
               ManualScaling: B1, B2, B4, B8, B4_1G
               Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionLivenessCheckArgs']] liveness_check: Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionManualScalingArgs']] manual_scaling: A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionNetworkArgs']] network: Extra network settings
               Structure is documented below.
        :param pulumi.Input[str] nobuild_files_regex: Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
        :param pulumi.Input[bool] noop_on_destroy: If set to `true`, the application version will not be deleted.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionReadinessCheckArgs']] readiness_check: Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionResourcesArgs']] resources: Machine resources for a version.
               Structure is documented below.
        :param pulumi.Input[str] runtime: Desired runtime. Example python27.
        :param pulumi.Input[str] runtime_api_version: The version of the API in the given runtime environment.
               Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
        :param pulumi.Input[str] runtime_channel: The channel of the runtime to use. Only available for some runtimes.
        :param pulumi.Input[str] runtime_main_executable_path: The path or name of the app's main executable.
        :param pulumi.Input[str] service: AppEngine service resource
        :param pulumi.Input[str] serving_status: Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
               Default value is `SERVING`.
               Possible values are `SERVING` and `STOPPED`.
        :param pulumi.Input[str] version_id: Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens.
               Reserved names,"default", "latest", and any name with the prefix "ah-".
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionVpcAccessConnectorArgs']] vpc_access_connector: Enables VPC connectivity for standard apps.
               Structure is documented below.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['api_config'] = api_config
            __props__['automatic_scaling'] = automatic_scaling
            __props__['beta_settings'] = beta_settings
            __props__['default_expiration'] = default_expiration
            __props__['delete_service_on_destroy'] = delete_service_on_destroy
            __props__['deployment'] = deployment
            __props__['endpoints_api_service'] = endpoints_api_service
            __props__['entrypoint'] = entrypoint
            __props__['env_variables'] = env_variables
            __props__['handlers'] = handlers
            __props__['inbound_services'] = inbound_services
            __props__['instance_class'] = instance_class
            if liveness_check is None:
                raise TypeError("Missing required property 'liveness_check'")
            __props__['liveness_check'] = liveness_check
            __props__['manual_scaling'] = manual_scaling
            __props__['network'] = network
            __props__['nobuild_files_regex'] = nobuild_files_regex
            __props__['noop_on_destroy'] = noop_on_destroy
            __props__['project'] = project
            if readiness_check is None:
                raise TypeError("Missing required property 'readiness_check'")
            __props__['readiness_check'] = readiness_check
            __props__['resources'] = resources
            if runtime is None:
                raise TypeError("Missing required property 'runtime'")
            __props__['runtime'] = runtime
            __props__['runtime_api_version'] = runtime_api_version
            __props__['runtime_channel'] = runtime_channel
            __props__['runtime_main_executable_path'] = runtime_main_executable_path
            if service is None:
                raise TypeError("Missing required property 'service'")
            __props__['service'] = service
            __props__['serving_status'] = serving_status
            __props__['version_id'] = version_id
            __props__['vpc_access_connector'] = vpc_access_connector
            __props__['name'] = None
        super(FlexibleAppVersion, __self__).__init__(
            'gcp:appengine/flexibleAppVersion:FlexibleAppVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_config: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionApiConfigArgs']]] = None,
            automatic_scaling: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionAutomaticScalingArgs']]] = None,
            beta_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            default_expiration: Optional[pulumi.Input[str]] = None,
            delete_service_on_destroy: Optional[pulumi.Input[bool]] = None,
            deployment: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionDeploymentArgs']]] = None,
            endpoints_api_service: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionEndpointsApiServiceArgs']]] = None,
            entrypoint: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionEntrypointArgs']]] = None,
            env_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            handlers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlexibleAppVersionHandlerArgs']]]]] = None,
            inbound_services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            instance_class: Optional[pulumi.Input[str]] = None,
            liveness_check: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionLivenessCheckArgs']]] = None,
            manual_scaling: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionManualScalingArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionNetworkArgs']]] = None,
            nobuild_files_regex: Optional[pulumi.Input[str]] = None,
            noop_on_destroy: Optional[pulumi.Input[bool]] = None,
            project: Optional[pulumi.Input[str]] = None,
            readiness_check: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionReadinessCheckArgs']]] = None,
            resources: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionResourcesArgs']]] = None,
            runtime: Optional[pulumi.Input[str]] = None,
            runtime_api_version: Optional[pulumi.Input[str]] = None,
            runtime_channel: Optional[pulumi.Input[str]] = None,
            runtime_main_executable_path: Optional[pulumi.Input[str]] = None,
            service: Optional[pulumi.Input[str]] = None,
            serving_status: Optional[pulumi.Input[str]] = None,
            version_id: Optional[pulumi.Input[str]] = None,
            vpc_access_connector: Optional[pulumi.Input[pulumi.InputType['FlexibleAppVersionVpcAccessConnectorArgs']]] = None) -> 'FlexibleAppVersion':
        """
        Get an existing FlexibleAppVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionApiConfigArgs']] api_config: Serving configuration for Google Cloud Endpoints.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionAutomaticScalingArgs']] automatic_scaling: Automatic scaling is based on request rate, response latencies, and other application metrics.
               Structure is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] beta_settings: Metadata settings that are supplied to this version to enable beta runtime features.
        :param pulumi.Input[str] default_expiration: Duration that static files should be cached by web proxies and browsers.
               Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time.
        :param pulumi.Input[bool] delete_service_on_destroy: If set to `true`, the service will be deleted if it is the last version.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionDeploymentArgs']] deployment: Code and application artifacts that make up this version.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionEndpointsApiServiceArgs']] endpoints_api_service: Code and application artifacts that make up this version.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionEntrypointArgs']] entrypoint: The entrypoint for the application.
               Structure is documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] env_variables: Environment variables available to the application.  As these are not returned in the API request, the provider will not detect any changes made outside of the config.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FlexibleAppVersionHandlerArgs']]]] handlers: An ordered list of URL-matching patterns that should be applied to incoming requests.
               The first matching URL handles the request and other request handlers are not attempted.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inbound_services: A list of the types of messages that this application is able to receive.
               Each value may be one of `INBOUND_SERVICE_MAIL`, `INBOUND_SERVICE_MAIL_BOUNCE`, `INBOUND_SERVICE_XMPP_ERROR`, `INBOUND_SERVICE_XMPP_MESSAGE`, `INBOUND_SERVICE_XMPP_SUBSCRIBE`, `INBOUND_SERVICE_XMPP_PRESENCE`, `INBOUND_SERVICE_CHANNEL_PRESENCE`, and `INBOUND_SERVICE_WARMUP`.
        :param pulumi.Input[str] instance_class: Instance class that is used to run this version. Valid values are
               AutomaticScaling: F1, F2, F4, F4_1G
               ManualScaling: B1, B2, B4, B8, B4_1G
               Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionLivenessCheckArgs']] liveness_check: Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionManualScalingArgs']] manual_scaling: A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.
               Structure is documented below.
        :param pulumi.Input[str] name: Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionNetworkArgs']] network: Extra network settings
               Structure is documented below.
        :param pulumi.Input[str] nobuild_files_regex: Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
        :param pulumi.Input[bool] noop_on_destroy: If set to `true`, the application version will not be deleted.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionReadinessCheckArgs']] readiness_check: Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionResourcesArgs']] resources: Machine resources for a version.
               Structure is documented below.
        :param pulumi.Input[str] runtime: Desired runtime. Example python27.
        :param pulumi.Input[str] runtime_api_version: The version of the API in the given runtime environment.
               Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
        :param pulumi.Input[str] runtime_channel: The channel of the runtime to use. Only available for some runtimes.
        :param pulumi.Input[str] runtime_main_executable_path: The path or name of the app's main executable.
        :param pulumi.Input[str] service: AppEngine service resource
        :param pulumi.Input[str] serving_status: Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
               Default value is `SERVING`.
               Possible values are `SERVING` and `STOPPED`.
        :param pulumi.Input[str] version_id: Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens.
               Reserved names,"default", "latest", and any name with the prefix "ah-".
        :param pulumi.Input[pulumi.InputType['FlexibleAppVersionVpcAccessConnectorArgs']] vpc_access_connector: Enables VPC connectivity for standard apps.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_config"] = api_config
        __props__["automatic_scaling"] = automatic_scaling
        __props__["beta_settings"] = beta_settings
        __props__["default_expiration"] = default_expiration
        __props__["delete_service_on_destroy"] = delete_service_on_destroy
        __props__["deployment"] = deployment
        __props__["endpoints_api_service"] = endpoints_api_service
        __props__["entrypoint"] = entrypoint
        __props__["env_variables"] = env_variables
        __props__["handlers"] = handlers
        __props__["inbound_services"] = inbound_services
        __props__["instance_class"] = instance_class
        __props__["liveness_check"] = liveness_check
        __props__["manual_scaling"] = manual_scaling
        __props__["name"] = name
        __props__["network"] = network
        __props__["nobuild_files_regex"] = nobuild_files_regex
        __props__["noop_on_destroy"] = noop_on_destroy
        __props__["project"] = project
        __props__["readiness_check"] = readiness_check
        __props__["resources"] = resources
        __props__["runtime"] = runtime
        __props__["runtime_api_version"] = runtime_api_version
        __props__["runtime_channel"] = runtime_channel
        __props__["runtime_main_executable_path"] = runtime_main_executable_path
        __props__["service"] = service
        __props__["serving_status"] = serving_status
        __props__["version_id"] = version_id
        __props__["vpc_access_connector"] = vpc_access_connector
        return FlexibleAppVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiConfig")
    def api_config(self) -> pulumi.Output[Optional['outputs.FlexibleAppVersionApiConfig']]:
        """
        Serving configuration for Google Cloud Endpoints.
        Structure is documented below.
        """
        return pulumi.get(self, "api_config")

    @property
    @pulumi.getter(name="automaticScaling")
    def automatic_scaling(self) -> pulumi.Output[Optional['outputs.FlexibleAppVersionAutomaticScaling']]:
        """
        Automatic scaling is based on request rate, response latencies, and other application metrics.
        Structure is documented below.
        """
        return pulumi.get(self, "automatic_scaling")

    @property
    @pulumi.getter(name="betaSettings")
    def beta_settings(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Metadata settings that are supplied to this version to enable beta runtime features.
        """
        return pulumi.get(self, "beta_settings")

    @property
    @pulumi.getter(name="defaultExpiration")
    def default_expiration(self) -> pulumi.Output[Optional[str]]:
        """
        Duration that static files should be cached by web proxies and browsers.
        Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time.
        """
        return pulumi.get(self, "default_expiration")

    @property
    @pulumi.getter(name="deleteServiceOnDestroy")
    def delete_service_on_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        If set to `true`, the service will be deleted if it is the last version.
        """
        return pulumi.get(self, "delete_service_on_destroy")

    @property
    @pulumi.getter
    def deployment(self) -> pulumi.Output[Optional['outputs.FlexibleAppVersionDeployment']]:
        """
        Code and application artifacts that make up this version.
        Structure is documented below.
        """
        return pulumi.get(self, "deployment")

    @property
    @pulumi.getter(name="endpointsApiService")
    def endpoints_api_service(self) -> pulumi.Output[Optional['outputs.FlexibleAppVersionEndpointsApiService']]:
        """
        Code and application artifacts that make up this version.
        Structure is documented below.
        """
        return pulumi.get(self, "endpoints_api_service")

    @property
    @pulumi.getter
    def entrypoint(self) -> pulumi.Output[Optional['outputs.FlexibleAppVersionEntrypoint']]:
        """
        The entrypoint for the application.
        Structure is documented below.
        """
        return pulumi.get(self, "entrypoint")

    @property
    @pulumi.getter(name="envVariables")
    def env_variables(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Environment variables available to the application.  As these are not returned in the API request, the provider will not detect any changes made outside of the config.
        """
        return pulumi.get(self, "env_variables")

    @property
    @pulumi.getter
    def handlers(self) -> pulumi.Output[Sequence['outputs.FlexibleAppVersionHandler']]:
        """
        An ordered list of URL-matching patterns that should be applied to incoming requests.
        The first matching URL handles the request and other request handlers are not attempted.
        Structure is documented below.
        """
        return pulumi.get(self, "handlers")

    @property
    @pulumi.getter(name="inboundServices")
    def inbound_services(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of the types of messages that this application is able to receive.
        Each value may be one of `INBOUND_SERVICE_MAIL`, `INBOUND_SERVICE_MAIL_BOUNCE`, `INBOUND_SERVICE_XMPP_ERROR`, `INBOUND_SERVICE_XMPP_MESSAGE`, `INBOUND_SERVICE_XMPP_SUBSCRIBE`, `INBOUND_SERVICE_XMPP_PRESENCE`, `INBOUND_SERVICE_CHANNEL_PRESENCE`, and `INBOUND_SERVICE_WARMUP`.
        """
        return pulumi.get(self, "inbound_services")

    @property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> pulumi.Output[Optional[str]]:
        """
        Instance class that is used to run this version. Valid values are
        AutomaticScaling: F1, F2, F4, F4_1G
        ManualScaling: B1, B2, B4, B8, B4_1G
        Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
        """
        return pulumi.get(self, "instance_class")

    @property
    @pulumi.getter(name="livenessCheck")
    def liveness_check(self) -> pulumi.Output['outputs.FlexibleAppVersionLivenessCheck']:
        """
        Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
        Structure is documented below.
        """
        return pulumi.get(self, "liveness_check")

    @property
    @pulumi.getter(name="manualScaling")
    def manual_scaling(self) -> pulumi.Output[Optional['outputs.FlexibleAppVersionManualScaling']]:
        """
        A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.
        Structure is documented below.
        """
        return pulumi.get(self, "manual_scaling")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional['outputs.FlexibleAppVersionNetwork']]:
        """
        Extra network settings
        Structure is documented below.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="nobuildFilesRegex")
    def nobuild_files_regex(self) -> pulumi.Output[Optional[str]]:
        """
        Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
        """
        return pulumi.get(self, "nobuild_files_regex")

    @property
    @pulumi.getter(name="noopOnDestroy")
    def noop_on_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        If set to `true`, the application version will not be deleted.
        """
        return pulumi.get(self, "noop_on_destroy")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="readinessCheck")
    def readiness_check(self) -> pulumi.Output['outputs.FlexibleAppVersionReadinessCheck']:
        """
        Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
        Structure is documented below.
        """
        return pulumi.get(self, "readiness_check")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional['outputs.FlexibleAppVersionResources']]:
        """
        Machine resources for a version.
        Structure is documented below.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter
    def runtime(self) -> pulumi.Output[str]:
        """
        Desired runtime. Example python27.
        """
        return pulumi.get(self, "runtime")

    @property
    @pulumi.getter(name="runtimeApiVersion")
    def runtime_api_version(self) -> pulumi.Output[str]:
        """
        The version of the API in the given runtime environment.
        Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
        """
        return pulumi.get(self, "runtime_api_version")

    @property
    @pulumi.getter(name="runtimeChannel")
    def runtime_channel(self) -> pulumi.Output[Optional[str]]:
        """
        The channel of the runtime to use. Only available for some runtimes.
        """
        return pulumi.get(self, "runtime_channel")

    @property
    @pulumi.getter(name="runtimeMainExecutablePath")
    def runtime_main_executable_path(self) -> pulumi.Output[Optional[str]]:
        """
        The path or name of the app's main executable.
        """
        return pulumi.get(self, "runtime_main_executable_path")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output[str]:
        """
        AppEngine service resource
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter(name="servingStatus")
    def serving_status(self) -> pulumi.Output[Optional[str]]:
        """
        Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
        Default value is `SERVING`.
        Possible values are `SERVING` and `STOPPED`.
        """
        return pulumi.get(self, "serving_status")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[Optional[str]]:
        """
        Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens.
        Reserved names,"default", "latest", and any name with the prefix "ah-".
        """
        return pulumi.get(self, "version_id")

    @property
    @pulumi.getter(name="vpcAccessConnector")
    def vpc_access_connector(self) -> pulumi.Output[Optional['outputs.FlexibleAppVersionVpcAccessConnector']]:
        """
        Enables VPC connectivity for standard apps.
        Structure is documented below.
        """
        return pulumi.get(self, "vpc_access_connector")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

