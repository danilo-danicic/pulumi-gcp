# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Network(pulumi.CustomResource):
    auto_create_subnetworks: pulumi.Output[bool]
    delete_default_routes_on_create: pulumi.Output[bool]
    description: pulumi.Output[str]
    gateway_ipv4: pulumi.Output[str]
    ipv4_range: pulumi.Output[str]
    name: pulumi.Output[str]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    routing_mode: pulumi.Output[str]
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    def __init__(__self__, resource_name, opts=None, auto_create_subnetworks=None, delete_default_routes_on_create=None, description=None, ipv4_range=None, name=None, project=None, routing_mode=None, __name__=None, __opts__=None):
        """
        Manages a VPC network or legacy network resource on GCP.
        
        
        To get more information about Network, see:
        
        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/networks)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/vpc/docs/vpc)
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['auto_create_subnetworks'] = auto_create_subnetworks

        __props__['delete_default_routes_on_create'] = delete_default_routes_on_create

        __props__['description'] = description

        __props__['ipv4_range'] = ipv4_range

        __props__['name'] = name

        __props__['project'] = project

        __props__['routing_mode'] = routing_mode

        __props__['gateway_ipv4'] = None
        __props__['self_link'] = None

        super(Network, __self__).__init__(
            'gcp:compute/network:Network',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

