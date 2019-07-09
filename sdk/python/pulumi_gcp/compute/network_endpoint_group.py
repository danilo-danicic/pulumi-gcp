# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class NetworkEndpointGroup(pulumi.CustomResource):
    default_port: pulumi.Output[float]
    description: pulumi.Output[str]
    name: pulumi.Output[str]
    network: pulumi.Output[str]
    network_endpoint_type: pulumi.Output[str]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    size: pulumi.Output[float]
    subnetwork: pulumi.Output[str]
    zone: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, default_port=None, description=None, name=None, network=None, network_endpoint_type=None, project=None, subnetwork=None, zone=None, __name__=None, __opts__=None):
        """
        Network endpoint groups (NEGs) are zonal resources that represent
        collections of IP address and port combinations for GCP resources within a
        single subnet. Each IP address and port combination is called a network
        endpoint.
        
        Network endpoint groups can be used as backends in backend services for
        HTTP(S), TCP proxy, and SSL proxy load balancers. You cannot use NEGs as a
        backend with internal load balancers. Because NEG backends allow you to
        specify IP addresses and ports, you can distribute traffic in a granular
        fashion among applications or containers running within VM instances.
        
        
        To get more information about NetworkEndpointGroup, see:
        
        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/negs/)
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_endpoint_group.html.markdown.
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

        __props__['default_port'] = default_port

        __props__['description'] = description

        __props__['name'] = name

        if network is None:
            raise TypeError("Missing required property 'network'")
        __props__['network'] = network

        __props__['network_endpoint_type'] = network_endpoint_type

        __props__['project'] = project

        __props__['subnetwork'] = subnetwork

        __props__['zone'] = zone

        __props__['self_link'] = None
        __props__['size'] = None

        super(NetworkEndpointGroup, __self__).__init__(
            'gcp:compute/networkEndpointGroup:NetworkEndpointGroup',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

