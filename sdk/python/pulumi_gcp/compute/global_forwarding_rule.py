# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class GlobalForwardingRule(pulumi.CustomResource):
    """
    Manages a Global Forwarding Rule within GCE. This binds an ip and port to a target HTTP(s) proxy. For more
    information see [the official
    documentation](https://cloud.google.com/compute/docs/load-balancing/http/global-forwarding-rules) and
    [API](https://cloud.google.com/compute/docs/reference/latest/globalForwardingRules).
    """
    def __init__(__self__, __name__, __opts__=None, description=None, ip_address=None, ip_protocol=None, ip_version=None, labels=None, name=None, port_range=None, project=None, target=None):
        """Create a GlobalForwardingRule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['description'] = description

        __props__['ipAddress'] = ip_address

        __props__['ipProtocol'] = ip_protocol

        __props__['ipVersion'] = ip_version

        __props__['labels'] = labels

        __props__['name'] = name

        __props__['portRange'] = port_range

        __props__['project'] = project

        if not target:
            raise TypeError('Missing required property target')
        __props__['target'] = target

        __props__['label_fingerprint'] = None
        __props__['self_link'] = None

        super(GlobalForwardingRule, __self__).__init__(
            'gcp:compute/globalForwardingRule:GlobalForwardingRule',
            __name__,
            __props__,
            __opts__)

