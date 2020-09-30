# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetForwardingRuleResult',
    'AwaitableGetForwardingRuleResult',
    'get_forwarding_rule',
]

@pulumi.output_type
class GetForwardingRuleResult:
    """
    A collection of values returned by getForwardingRule.
    """
    def __init__(__self__, backend_service=None, description=None, id=None, ip_address=None, ip_protocol=None, load_balancing_scheme=None, name=None, network=None, port_range=None, ports=None, project=None, region=None, self_link=None, subnetwork=None, target=None):
        if backend_service and not isinstance(backend_service, str):
            raise TypeError("Expected argument 'backend_service' to be a str")
        pulumi.set(__self__, "backend_service", backend_service)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if ip_protocol and not isinstance(ip_protocol, str):
            raise TypeError("Expected argument 'ip_protocol' to be a str")
        pulumi.set(__self__, "ip_protocol", ip_protocol)
        if load_balancing_scheme and not isinstance(load_balancing_scheme, str):
            raise TypeError("Expected argument 'load_balancing_scheme' to be a str")
        pulumi.set(__self__, "load_balancing_scheme", load_balancing_scheme)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if port_range and not isinstance(port_range, str):
            raise TypeError("Expected argument 'port_range' to be a str")
        pulumi.set(__self__, "port_range", port_range)
        if ports and not isinstance(ports, list):
            raise TypeError("Expected argument 'ports' to be a list")
        pulumi.set(__self__, "ports", ports)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if subnetwork and not isinstance(subnetwork, str):
            raise TypeError("Expected argument 'subnetwork' to be a str")
        pulumi.set(__self__, "subnetwork", subnetwork)
        if target and not isinstance(target, str):
            raise TypeError("Expected argument 'target' to be a str")
        pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="backendService")
    def backend_service(self) -> str:
        """
        Backend service, if this forwarding rule has one.
        """
        return pulumi.get(self, "backend_service")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of this forwarding rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        IP address of this forwarding rule.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> str:
        """
        IP protocol of this forwarding rule.
        """
        return pulumi.get(self, "ip_protocol")

    @property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> str:
        """
        Type of load balancing of this forwarding rule.
        """
        return pulumi.get(self, "load_balancing_scheme")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        Network of this forwarding rule.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> str:
        """
        Port range, if this forwarding rule has one.
        """
        return pulumi.get(self, "port_range")

    @property
    @pulumi.getter
    def ports(self) -> Sequence[str]:
        """
        List of ports to use for internal load balancing, if this forwarding rule has any.
        """
        return pulumi.get(self, "ports")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        Region of this forwarding rule.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        The URI of the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def subnetwork(self) -> str:
        """
        Subnetwork of this forwarding rule.
        """
        return pulumi.get(self, "subnetwork")

    @property
    @pulumi.getter
    def target(self) -> str:
        """
        URL of the target pool, if this forwarding rule has one.
        """
        return pulumi.get(self, "target")


class AwaitableGetForwardingRuleResult(GetForwardingRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetForwardingRuleResult(
            backend_service=self.backend_service,
            description=self.description,
            id=self.id,
            ip_address=self.ip_address,
            ip_protocol=self.ip_protocol,
            load_balancing_scheme=self.load_balancing_scheme,
            name=self.name,
            network=self.network,
            port_range=self.port_range,
            ports=self.ports,
            project=self.project,
            region=self.region,
            self_link=self.self_link,
            subnetwork=self.subnetwork,
            target=self.target)


def get_forwarding_rule(name: Optional[str] = None,
                        project: Optional[str] = None,
                        region: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetForwardingRuleResult:
    """
    Get a forwarding rule within GCE from its name.


    :param str name: The name of the forwarding rule.
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str region: The region in which the resource belongs. If it
           is not provided, the project region is used.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:compute/getForwardingRule:getForwardingRule', __args__, opts=opts, typ=GetForwardingRuleResult).value

    return AwaitableGetForwardingRuleResult(
        backend_service=__ret__.backend_service,
        description=__ret__.description,
        id=__ret__.id,
        ip_address=__ret__.ip_address,
        ip_protocol=__ret__.ip_protocol,
        load_balancing_scheme=__ret__.load_balancing_scheme,
        name=__ret__.name,
        network=__ret__.network,
        port_range=__ret__.port_range,
        ports=__ret__.ports,
        project=__ret__.project,
        region=__ret__.region,
        self_link=__ret__.self_link,
        subnetwork=__ret__.subnetwork,
        target=__ret__.target)
