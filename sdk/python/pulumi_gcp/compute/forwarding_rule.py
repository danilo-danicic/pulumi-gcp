# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class ForwardingRule(pulumi.CustomResource):
    def __init__(__self__, __name__, __opts__=None, backend_service=None, description=None, ip_address=None, ip_protocol=None, ip_version=None, labels=None, load_balancing_scheme=None, name=None, network=None, network_tier=None, port_range=None, ports=None, project=None, region=None, service_label=None, subnetwork=None, target=None):
        """Create a ForwardingRule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['backendService'] = backend_service

        __props__['description'] = description

        __props__['ipAddress'] = ip_address

        __props__['ipProtocol'] = ip_protocol

        __props__['ipVersion'] = ip_version

        __props__['labels'] = labels

        __props__['loadBalancingScheme'] = load_balancing_scheme

        __props__['name'] = name

        __props__['network'] = network

        __props__['networkTier'] = network_tier

        __props__['portRange'] = port_range

        __props__['ports'] = ports

        __props__['project'] = project

        __props__['region'] = region

        __props__['serviceLabel'] = service_label

        __props__['subnetwork'] = subnetwork

        __props__['target'] = target

        __props__['creation_timestamp'] = None
        __props__['label_fingerprint'] = None
        __props__['self_link'] = None
        __props__['service_name'] = None

        super(ForwardingRule, __self__).__init__(
            'gcp:compute/forwardingRule:ForwardingRule',
            __name__,
            __props__,
            __opts__)

