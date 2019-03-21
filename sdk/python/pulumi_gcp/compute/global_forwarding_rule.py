# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GlobalForwardingRule(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    Textual description field.
    """
    ip_address: pulumi.Output[str]
    """
    The static IP. (if not set, an ephemeral IP is
    used). This should be the literal IP address to be used, not the `self_link`
    to a `google_compute_global_address` resource. (If using a `google_compute_global_address`
    resource, use the `address` property instead of the `self_link` property.)
    """
    ip_protocol: pulumi.Output[str]
    """
    The IP protocol to route, one of "TCP" "UDP" "AH"
    "ESP" or "SCTP". (default "TCP").
    """
    ip_version: pulumi.Output[str]
    """
    
    The IP Version that will be used by this resource's address. One of `"IPV4"` or `"IPV6"`.
    You cannot provide this and `ip_address`.
    """
    label_fingerprint: pulumi.Output[str]
    labels: pulumi.Output[dict]
    """
    )
    A set of key/value label pairs to assign to the resource.
    """
    name: pulumi.Output[str]
    """
    A unique name for the resource, required by GCE. Changing
    this forces a new resource to be created.
    """
    port_range: pulumi.Output[str]
    """
    A range e.g. "1024-2048" or a single port "1024"
    (defaults to all ports!).
    Some types of forwarding targets have constraints on the acceptable ports:
    * Target HTTP proxy: 80, 8080
    * Target HTTPS proxy: 443
    * Target TCP proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
    * Target SSL proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
    * Target VPN gateway: 500, 4500
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs. If it
    is not provided, the provider project is used.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    target: pulumi.Output[str]
    """
    URL of target HTTP or HTTPS proxy.
    """
    def __init__(__self__, resource_name, opts=None, description=None, ip_address=None, ip_protocol=None, ip_version=None, labels=None, name=None, port_range=None, project=None, target=None, __name__=None, __opts__=None):
        """
        Manages a Global Forwarding Rule within GCE. This binds an ip and port to a target HTTP(s) proxy. For more
        information see [the official
        documentation](https://cloud.google.com/compute/docs/load-balancing/http/global-forwarding-rules) and
        [API](https://cloud.google.com/compute/docs/reference/latest/globalForwardingRules).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Textual description field.
        :param pulumi.Input[str] ip_address: The static IP. (if not set, an ephemeral IP is
               used). This should be the literal IP address to be used, not the `self_link`
               to a `google_compute_global_address` resource. (If using a `google_compute_global_address`
               resource, use the `address` property instead of the `self_link` property.)
        :param pulumi.Input[str] ip_protocol: The IP protocol to route, one of "TCP" "UDP" "AH"
               "ESP" or "SCTP". (default "TCP").
        :param pulumi.Input[str] ip_version: 
               The IP Version that will be used by this resource's address. One of `"IPV4"` or `"IPV6"`.
               You cannot provide this and `ip_address`.
        :param pulumi.Input[dict] labels: )
               A set of key/value label pairs to assign to the resource.
        :param pulumi.Input[str] name: A unique name for the resource, required by GCE. Changing
               this forces a new resource to be created.
        :param pulumi.Input[str] port_range: A range e.g. "1024-2048" or a single port "1024"
               (defaults to all ports!).
               Some types of forwarding targets have constraints on the acceptable ports:
               * Target HTTP proxy: 80, 8080
               * Target HTTPS proxy: 443
               * Target TCP proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
               * Target SSL proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
               * Target VPN gateway: 500, 4500
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] target: URL of target HTTP or HTTPS proxy.
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

        __props__['description'] = description

        __props__['ip_address'] = ip_address

        __props__['ip_protocol'] = ip_protocol

        __props__['ip_version'] = ip_version

        __props__['labels'] = labels

        __props__['name'] = name

        __props__['port_range'] = port_range

        __props__['project'] = project

        if target is None:
            raise TypeError('Missing required property target')
        __props__['target'] = target

        __props__['label_fingerprint'] = None
        __props__['self_link'] = None

        super(GlobalForwardingRule, __self__).__init__(
            'gcp:compute/globalForwardingRule:GlobalForwardingRule',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

