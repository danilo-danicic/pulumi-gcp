# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class RouterPeer(pulumi.CustomResource):
    """
    Manages a Cloud Router BGP peer. For more information see
    [the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
    and
    [API](https://cloud.google.com/compute/docs/reference/latest/routers).
    """
    def __init__(__self__, __name__, __opts__=None, advertised_route_priority=None, interface=None, name=None, peer_asn=None, peer_ip_address=None, project=None, region=None, router=None):
        """Create a RouterPeer resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if advertised_route_priority and not isinstance(advertised_route_priority, int):
            raise TypeError('Expected property advertised_route_priority to be a int')
        __self__.advertised_route_priority = advertised_route_priority
        """
        The priority of routes advertised to this BGP peer.
        Changing this forces a new peer to be created.
        """
        __props__['advertisedRoutePriority'] = advertised_route_priority

        if not interface:
            raise TypeError('Missing required property interface')
        elif not isinstance(interface, basestring):
            raise TypeError('Expected property interface to be a basestring')
        __self__.interface = interface
        """
        The name of the interface the BGP peer is associated with.
        Changing this forces a new peer to be created.
        """
        __props__['interface'] = interface

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A unique name for BGP peer, required by GCE. Changing
        this forces a new peer to be created.
        """
        __props__['name'] = name

        if not peer_asn:
            raise TypeError('Missing required property peer_asn')
        elif not isinstance(peer_asn, int):
            raise TypeError('Expected property peer_asn to be a int')
        __self__.peer_asn = peer_asn
        """
        Peer BGP Autonomous System Number (ASN).
        Changing this forces a new peer to be created.
        """
        __props__['peerAsn'] = peer_asn

        if peer_ip_address and not isinstance(peer_ip_address, basestring):
            raise TypeError('Expected property peer_ip_address to be a basestring')
        __self__.peer_ip_address = peer_ip_address
        """
        IP address of the BGP interface outside Google Cloud.
        Changing this forces a new peer to be created.
        """
        __props__['peerIpAddress'] = peer_ip_address

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The ID of the project in which this peer's router belongs. If it
        is not provided, the provider project is used. Changing this forces a new peer to be created.
        """
        __props__['project'] = project

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        The region this peer's router sits in. If not specified,
        the project region will be used. Changing this forces a new peer to be
        created.
        """
        __props__['region'] = region

        if not router:
            raise TypeError('Missing required property router')
        elif not isinstance(router, basestring):
            raise TypeError('Expected property router to be a basestring')
        __self__.router = router
        """
        The name of the router in which this BGP peer will be configured.
        Changing this forces a new peer to be created.
        """
        __props__['router'] = router

        __self__.ip_address = pulumi.runtime.UNKNOWN
        """
        IP address of the interface inside Google Cloud Platform.
        """

        super(RouterPeer, __self__).__init__(
            'gcp:compute/routerPeer:RouterPeer',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'advertisedRoutePriority' in outs:
            self.advertised_route_priority = outs['advertisedRoutePriority']
        if 'interface' in outs:
            self.interface = outs['interface']
        if 'ipAddress' in outs:
            self.ip_address = outs['ipAddress']
        if 'name' in outs:
            self.name = outs['name']
        if 'peerAsn' in outs:
            self.peer_asn = outs['peerAsn']
        if 'peerIpAddress' in outs:
            self.peer_ip_address = outs['peerIpAddress']
        if 'project' in outs:
            self.project = outs['project']
        if 'region' in outs:
            self.region = outs['region']
        if 'router' in outs:
            self.router = outs['router']