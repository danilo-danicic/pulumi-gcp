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

__all__ = ['RegionNetworkEndpointGroup']


class RegionNetworkEndpointGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_engine: Optional[pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupAppEngineArgs']]] = None,
                 cloud_function: Optional[pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupCloudFunctionArgs']]] = None,
                 cloud_run: Optional[pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupCloudRunArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_endpoint_type: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A regional NEG that can support Serverless Products.

        To get more information about RegionNetworkEndpointGroup, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/regionNetworkEndpointGroups)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)

        ## Example Usage
        ### Region Network Endpoint Group Functions

        ```python
        import pulumi
        import pulumi_gcp as gcp

        bucket = gcp.storage.Bucket("bucket")
        archive = gcp.storage.BucketObject("archive",
            bucket=bucket.name,
            source=pulumi.FileAsset("path/to/index.zip"))
        function_neg_function = gcp.cloudfunctions.Function("functionNegFunction",
            description="My function",
            runtime="nodejs10",
            available_memory_mb=128,
            source_archive_bucket=bucket.name,
            source_archive_object=archive.name,
            trigger_http=True,
            timeout=60,
            entry_point="helloGET")
        # Cloud Functions Example
        function_neg_region_network_endpoint_group = gcp.compute.RegionNetworkEndpointGroup("functionNegRegionNetworkEndpointGroup",
            network_endpoint_type="SERVERLESS",
            region="us-central1",
            cloud_function=gcp.compute.RegionNetworkEndpointGroupCloudFunctionArgs(
                function=function_neg_function.name,
            ))
        ```
        ### Region Network Endpoint Group Cloudrun

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cloudrun_neg_service = gcp.cloudrun.Service("cloudrunNegService",
            location="us-central1",
            template=gcp.cloudrun.ServiceTemplateArgs(
                spec=gcp.cloudrun.ServiceTemplateSpecArgs(
                    containers=[gcp.cloudrun.ServiceTemplateSpecContainerArgs(
                        image="us-docker.pkg.dev/cloudrun/container/hello",
                    )],
                ),
            ),
            traffics=[gcp.cloudrun.ServiceTrafficArgs(
                percent=100,
                latest_revision=True,
            )])
        # Cloud Run Example
        cloudrun_neg_region_network_endpoint_group = gcp.compute.RegionNetworkEndpointGroup("cloudrunNegRegionNetworkEndpointGroup",
            network_endpoint_type="SERVERLESS",
            region="us-central1",
            cloud_run=gcp.compute.RegionNetworkEndpointGroupCloudRunArgs(
                service=cloudrun_neg_service.name,
            ))
        ```
        ### Region Network Endpoint Group Appengine

        ```python
        import pulumi
        import pulumi_gcp as gcp

        appengine_neg_bucket = gcp.storage.Bucket("appengineNegBucket")
        appengine_neg_bucket_object = gcp.storage.BucketObject("appengineNegBucketObject",
            bucket=appengine_neg_bucket.name,
            source=pulumi.FileAsset("./test-fixtures/appengine/hello-world.zip"))
        appengine_neg_flexible_app_version = gcp.appengine.FlexibleAppVersion("appengineNegFlexibleAppVersion",
            version_id="v1",
            service="default",
            runtime="nodejs",
            entrypoint=gcp.appengine.FlexibleAppVersionEntrypointArgs(
                shell="node ./app.js",
            ),
            deployment=gcp.appengine.FlexibleAppVersionDeploymentArgs(
                zip=gcp.appengine.FlexibleAppVersionDeploymentZipArgs(
                    source_url=pulumi.Output.all(appengine_neg_bucket.name, appengine_neg_bucket_object.name).apply(lambda appengineNegBucketName, appengineNegBucketObjectName: f"https://storage.googleapis.com/{appengine_neg_bucket_name}/{appengine_neg_bucket_object_name}"),
                ),
            ),
            liveness_check=gcp.appengine.FlexibleAppVersionLivenessCheckArgs(
                path="/",
            ),
            readiness_check=gcp.appengine.FlexibleAppVersionReadinessCheckArgs(
                path="/",
            ),
            env_variables={
                "port": "8080",
            },
            handlers=[gcp.appengine.FlexibleAppVersionHandlerArgs(
                url_regex=".*\\/my-path\\/*",
                security_level="SECURE_ALWAYS",
                login="LOGIN_REQUIRED",
                auth_fail_action="AUTH_FAIL_ACTION_REDIRECT",
                static_files=gcp.appengine.FlexibleAppVersionHandlerStaticFilesArgs(
                    path="my-other-path",
                    upload_path_regex=".*\\/my-path\\/*",
                ),
            )],
            automatic_scaling=gcp.appengine.FlexibleAppVersionAutomaticScalingArgs(
                cool_down_period="120s",
                cpu_utilization=gcp.appengine.FlexibleAppVersionAutomaticScalingCpuUtilizationArgs(
                    target_utilization=0.5,
                ),
            ),
            noop_on_destroy=True)
        # App Engine Example
        appengine_neg_region_network_endpoint_group = gcp.compute.RegionNetworkEndpointGroup("appengineNegRegionNetworkEndpointGroup",
            network_endpoint_type="SERVERLESS",
            region="us-central1",
            app_engine=gcp.compute.RegionNetworkEndpointGroupAppEngineArgs(
                service=appengine_neg_flexible_app_version.service,
                version=appengine_neg_flexible_app_version.version_id,
            ))
        ```

        ## Import

        RegionNetworkEndpointGroup can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/regionNetworkEndpointGroup:RegionNetworkEndpointGroup default projects/{{project}}/regions/{{region}}/networkEndpointGroups/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionNetworkEndpointGroup:RegionNetworkEndpointGroup default {{project}}/{{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionNetworkEndpointGroup:RegionNetworkEndpointGroup default {{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionNetworkEndpointGroup:RegionNetworkEndpointGroup default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupAppEngineArgs']] app_engine: Only valid when networkEndpointType is "SERVERLESS".
               Only one of cloud_run, app_engine or cloud_function may be set.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupCloudFunctionArgs']] cloud_function: Only valid when networkEndpointType is "SERVERLESS".
               Only one of cloud_run, app_engine or cloud_function may be set.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupCloudRunArgs']] cloud_run: Only valid when networkEndpointType is "SERVERLESS".
               Only one of cloud_run, app_engine or cloud_function may be set.
               Structure is documented below.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when
               you create the resource.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] network_endpoint_type: Type of network endpoints in this network endpoint group. Defaults to SERVERLESS
               Default value is `SERVERLESS`.
               Possible values are `SERVERLESS`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: A reference to the region where the Serverless NEGs Reside.
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

            __props__['app_engine'] = app_engine
            __props__['cloud_function'] = cloud_function
            __props__['cloud_run'] = cloud_run
            __props__['description'] = description
            __props__['name'] = name
            __props__['network_endpoint_type'] = network_endpoint_type
            __props__['project'] = project
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__['region'] = region
            __props__['self_link'] = None
        super(RegionNetworkEndpointGroup, __self__).__init__(
            'gcp:compute/regionNetworkEndpointGroup:RegionNetworkEndpointGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_engine: Optional[pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupAppEngineArgs']]] = None,
            cloud_function: Optional[pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupCloudFunctionArgs']]] = None,
            cloud_run: Optional[pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupCloudRunArgs']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_endpoint_type: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None) -> 'RegionNetworkEndpointGroup':
        """
        Get an existing RegionNetworkEndpointGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupAppEngineArgs']] app_engine: Only valid when networkEndpointType is "SERVERLESS".
               Only one of cloud_run, app_engine or cloud_function may be set.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupCloudFunctionArgs']] cloud_function: Only valid when networkEndpointType is "SERVERLESS".
               Only one of cloud_run, app_engine or cloud_function may be set.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionNetworkEndpointGroupCloudRunArgs']] cloud_run: Only valid when networkEndpointType is "SERVERLESS".
               Only one of cloud_run, app_engine or cloud_function may be set.
               Structure is documented below.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when
               you create the resource.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] network_endpoint_type: Type of network endpoints in this network endpoint group. Defaults to SERVERLESS
               Default value is `SERVERLESS`.
               Possible values are `SERVERLESS`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: A reference to the region where the Serverless NEGs Reside.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_engine"] = app_engine
        __props__["cloud_function"] = cloud_function
        __props__["cloud_run"] = cloud_run
        __props__["description"] = description
        __props__["name"] = name
        __props__["network_endpoint_type"] = network_endpoint_type
        __props__["project"] = project
        __props__["region"] = region
        __props__["self_link"] = self_link
        return RegionNetworkEndpointGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appEngine")
    def app_engine(self) -> pulumi.Output[Optional['outputs.RegionNetworkEndpointGroupAppEngine']]:
        """
        Only valid when networkEndpointType is "SERVERLESS".
        Only one of cloud_run, app_engine or cloud_function may be set.
        Structure is documented below.
        """
        return pulumi.get(self, "app_engine")

    @property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(self) -> pulumi.Output[Optional['outputs.RegionNetworkEndpointGroupCloudFunction']]:
        """
        Only valid when networkEndpointType is "SERVERLESS".
        Only one of cloud_run, app_engine or cloud_function may be set.
        Structure is documented below.
        """
        return pulumi.get(self, "cloud_function")

    @property
    @pulumi.getter(name="cloudRun")
    def cloud_run(self) -> pulumi.Output[Optional['outputs.RegionNetworkEndpointGroupCloudRun']]:
        """
        Only valid when networkEndpointType is "SERVERLESS".
        Only one of cloud_run, app_engine or cloud_function may be set.
        Structure is documented below.
        """
        return pulumi.get(self, "cloud_run")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of this resource. Provide this property when
        you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource; provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression `a-z?` which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkEndpointType")
    def network_endpoint_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of network endpoints in this network endpoint group. Defaults to SERVERLESS
        Default value is `SERVERLESS`.
        Possible values are `SERVERLESS`.
        """
        return pulumi.get(self, "network_endpoint_type")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        A reference to the region where the Serverless NEGs Reside.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

