# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Connector']


class Connector(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_cidr_range: Optional[pulumi.Input[str]] = None,
                 max_throughput: Optional[pulumi.Input[int]] = None,
                 min_throughput: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Serverless VPC Access connector resource.

        To get more information about Connector, see:

        * [API documentation](https://cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1/projects.locations.connectors)
        * How-to Guides
            * [Configuring Serverless VPC Access](https://cloud.google.com/vpc/docs/configure-serverless-vpc-access)

        ## Example Usage
        ### VPC Access Connector

        ```python
        import pulumi
        import pulumi_gcp as gcp

        connector = gcp.vpcaccess.Connector("connector",
            ip_cidr_range="10.8.0.0/28",
            network="default")
        ```

        ## Import

        Connector can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:vpcaccess/connector:Connector default projects/{{project}}/locations/{{region}}/connectors/{{name}}
        ```

        ```sh
         $ pulumi import gcp:vpcaccess/connector:Connector default {{project}}/{{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:vpcaccess/connector:Connector default {{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:vpcaccess/connector:Connector default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip_cidr_range: The range of internal addresses that follows RFC 4632 notation. Example: `10.132.0.0/28`.
        :param pulumi.Input[int] max_throughput: Maximum throughput of the connector in Mbps, must be greater than `min_throughput`. Default is 1000.
        :param pulumi.Input[int] min_throughput: Minimum throughput of the connector in Mbps. Default and min is 200.
        :param pulumi.Input[str] name: The name of the resource (Max 25 characters).
        :param pulumi.Input[str] network: Name of a VPC network.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where the VPC Access connector resides. If it is not provided, the provider region is used.
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

            if ip_cidr_range is None and not opts.urn:
                raise TypeError("Missing required property 'ip_cidr_range'")
            __props__['ip_cidr_range'] = ip_cidr_range
            __props__['max_throughput'] = max_throughput
            __props__['min_throughput'] = min_throughput
            __props__['name'] = name
            if network is None and not opts.urn:
                raise TypeError("Missing required property 'network'")
            __props__['network'] = network
            __props__['project'] = project
            __props__['region'] = region
            __props__['self_link'] = None
            __props__['state'] = None
        super(Connector, __self__).__init__(
            'gcp:vpcaccess/connector:Connector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ip_cidr_range: Optional[pulumi.Input[str]] = None,
            max_throughput: Optional[pulumi.Input[int]] = None,
            min_throughput: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'Connector':
        """
        Get an existing Connector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip_cidr_range: The range of internal addresses that follows RFC 4632 notation. Example: `10.132.0.0/28`.
        :param pulumi.Input[int] max_throughput: Maximum throughput of the connector in Mbps, must be greater than `min_throughput`. Default is 1000.
        :param pulumi.Input[int] min_throughput: Minimum throughput of the connector in Mbps. Default and min is 200.
        :param pulumi.Input[str] name: The name of the resource (Max 25 characters).
        :param pulumi.Input[str] network: Name of a VPC network.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where the VPC Access connector resides. If it is not provided, the provider region is used.
        :param pulumi.Input[str] self_link: The fully qualified name of this VPC connector
        :param pulumi.Input[str] state: State of the VPC access connector.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["ip_cidr_range"] = ip_cidr_range
        __props__["max_throughput"] = max_throughput
        __props__["min_throughput"] = min_throughput
        __props__["name"] = name
        __props__["network"] = network
        __props__["project"] = project
        __props__["region"] = region
        __props__["self_link"] = self_link
        __props__["state"] = state
        return Connector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Output[str]:
        """
        The range of internal addresses that follows RFC 4632 notation. Example: `10.132.0.0/28`.
        """
        return pulumi.get(self, "ip_cidr_range")

    @property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum throughput of the connector in Mbps, must be greater than `min_throughput`. Default is 1000.
        """
        return pulumi.get(self, "max_throughput")

    @property
    @pulumi.getter(name="minThroughput")
    def min_throughput(self) -> pulumi.Output[Optional[int]]:
        """
        Minimum throughput of the connector in Mbps. Default and min is 200.
        """
        return pulumi.get(self, "min_throughput")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource (Max 25 characters).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        Name of a VPC network.
        """
        return pulumi.get(self, "network")

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
        Region where the VPC Access connector resides. If it is not provided, the provider region is used.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The fully qualified name of this VPC connector
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the VPC access connector.
        """
        return pulumi.get(self, "state")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

