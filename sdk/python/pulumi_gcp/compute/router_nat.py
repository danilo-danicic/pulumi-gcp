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

__all__ = ['RouterNat']


class RouterNat(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 drain_nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 icmp_idle_timeout_sec: Optional[pulumi.Input[int]] = None,
                 log_config: Optional[pulumi.Input[pulumi.InputType['RouterNatLogConfigArgs']]] = None,
                 min_ports_per_vm: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_ip_allocate_option: Optional[pulumi.Input[str]] = None,
                 nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 router: Optional[pulumi.Input[str]] = None,
                 source_subnetwork_ip_ranges_to_nat: Optional[pulumi.Input[str]] = None,
                 subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouterNatSubnetworkArgs']]]]] = None,
                 tcp_established_idle_timeout_sec: Optional[pulumi.Input[int]] = None,
                 tcp_transitory_idle_timeout_sec: Optional[pulumi.Input[int]] = None,
                 udp_idle_timeout_sec: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A NAT service created in a router.

        To get more information about RouterNat, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/routers)
        * How-to Guides
            * [Google Cloud Router](https://cloud.google.com/router/docs/)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] drain_nat_ips: A list of URLs of the IP resources to be drained. These IPs must be
               valid static external IPs that have been assigned to the NAT.
        :param pulumi.Input[int] icmp_idle_timeout_sec: Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
        :param pulumi.Input[pulumi.InputType['RouterNatLogConfigArgs']] log_config: Configuration for logging on NAT
               Structure is documented below.
        :param pulumi.Input[int] min_ports_per_vm: Minimum number of ports allocated to a VM from this NAT.
        :param pulumi.Input[str] name: Self-link of subnetwork to NAT
        :param pulumi.Input[str] nat_ip_allocate_option: How external IPs should be allocated for this NAT. Valid values are
               `AUTO_ONLY` for only allowing NAT IPs allocated by Google Cloud
               Platform, or `MANUAL_ONLY` for only user-allocated NAT IP addresses.
               Possible values are `MANUAL_ONLY` and `AUTO_ONLY`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] nat_ips: Self-links of NAT IPs. Only valid if natIpAllocateOption
               is set to MANUAL_ONLY.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where the router and NAT reside.
        :param pulumi.Input[str] router: The name of the Cloud Router in which this NAT will be configured.
        :param pulumi.Input[str] source_subnetwork_ip_ranges_to_nat: How NAT should be configured per Subnetwork.
               If `ALL_SUBNETWORKS_ALL_IP_RANGES`, all of the
               IP ranges in every Subnetwork are allowed to Nat.
               If `ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES`, all of the primary IP
               ranges in every Subnetwork are allowed to Nat.
               `LIST_OF_SUBNETWORKS`: A list of Subnetworks are allowed to Nat
               (specified in the field subnetwork below). Note that if this field
               contains ALL_SUBNETWORKS_ALL_IP_RANGES or
               ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any
               other RouterNat section in any Router for this network in this region.
               Possible values are `ALL_SUBNETWORKS_ALL_IP_RANGES`, `ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES`, and `LIST_OF_SUBNETWORKS`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouterNatSubnetworkArgs']]]] subnetworks: One or more subnetwork NAT configurations. Only used if
               `source_subnetwork_ip_ranges_to_nat` is set to `LIST_OF_SUBNETWORKS`
               Structure is documented below.
        :param pulumi.Input[int] tcp_established_idle_timeout_sec: Timeout (in seconds) for TCP established connections.
               Defaults to 1200s if not set.
        :param pulumi.Input[int] tcp_transitory_idle_timeout_sec: Timeout (in seconds) for TCP transitory connections.
               Defaults to 30s if not set.
        :param pulumi.Input[int] udp_idle_timeout_sec: Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
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

            __props__['drain_nat_ips'] = drain_nat_ips
            __props__['icmp_idle_timeout_sec'] = icmp_idle_timeout_sec
            __props__['log_config'] = log_config
            __props__['min_ports_per_vm'] = min_ports_per_vm
            __props__['name'] = name
            if nat_ip_allocate_option is None:
                raise TypeError("Missing required property 'nat_ip_allocate_option'")
            __props__['nat_ip_allocate_option'] = nat_ip_allocate_option
            __props__['nat_ips'] = nat_ips
            __props__['project'] = project
            __props__['region'] = region
            if router is None:
                raise TypeError("Missing required property 'router'")
            __props__['router'] = router
            if source_subnetwork_ip_ranges_to_nat is None:
                raise TypeError("Missing required property 'source_subnetwork_ip_ranges_to_nat'")
            __props__['source_subnetwork_ip_ranges_to_nat'] = source_subnetwork_ip_ranges_to_nat
            __props__['subnetworks'] = subnetworks
            __props__['tcp_established_idle_timeout_sec'] = tcp_established_idle_timeout_sec
            __props__['tcp_transitory_idle_timeout_sec'] = tcp_transitory_idle_timeout_sec
            __props__['udp_idle_timeout_sec'] = udp_idle_timeout_sec
        super(RouterNat, __self__).__init__(
            'gcp:compute/routerNat:RouterNat',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            drain_nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            icmp_idle_timeout_sec: Optional[pulumi.Input[int]] = None,
            log_config: Optional[pulumi.Input[pulumi.InputType['RouterNatLogConfigArgs']]] = None,
            min_ports_per_vm: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nat_ip_allocate_option: Optional[pulumi.Input[str]] = None,
            nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            router: Optional[pulumi.Input[str]] = None,
            source_subnetwork_ip_ranges_to_nat: Optional[pulumi.Input[str]] = None,
            subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouterNatSubnetworkArgs']]]]] = None,
            tcp_established_idle_timeout_sec: Optional[pulumi.Input[int]] = None,
            tcp_transitory_idle_timeout_sec: Optional[pulumi.Input[int]] = None,
            udp_idle_timeout_sec: Optional[pulumi.Input[int]] = None) -> 'RouterNat':
        """
        Get an existing RouterNat resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] drain_nat_ips: A list of URLs of the IP resources to be drained. These IPs must be
               valid static external IPs that have been assigned to the NAT.
        :param pulumi.Input[int] icmp_idle_timeout_sec: Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
        :param pulumi.Input[pulumi.InputType['RouterNatLogConfigArgs']] log_config: Configuration for logging on NAT
               Structure is documented below.
        :param pulumi.Input[int] min_ports_per_vm: Minimum number of ports allocated to a VM from this NAT.
        :param pulumi.Input[str] name: Self-link of subnetwork to NAT
        :param pulumi.Input[str] nat_ip_allocate_option: How external IPs should be allocated for this NAT. Valid values are
               `AUTO_ONLY` for only allowing NAT IPs allocated by Google Cloud
               Platform, or `MANUAL_ONLY` for only user-allocated NAT IP addresses.
               Possible values are `MANUAL_ONLY` and `AUTO_ONLY`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] nat_ips: Self-links of NAT IPs. Only valid if natIpAllocateOption
               is set to MANUAL_ONLY.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: Region where the router and NAT reside.
        :param pulumi.Input[str] router: The name of the Cloud Router in which this NAT will be configured.
        :param pulumi.Input[str] source_subnetwork_ip_ranges_to_nat: How NAT should be configured per Subnetwork.
               If `ALL_SUBNETWORKS_ALL_IP_RANGES`, all of the
               IP ranges in every Subnetwork are allowed to Nat.
               If `ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES`, all of the primary IP
               ranges in every Subnetwork are allowed to Nat.
               `LIST_OF_SUBNETWORKS`: A list of Subnetworks are allowed to Nat
               (specified in the field subnetwork below). Note that if this field
               contains ALL_SUBNETWORKS_ALL_IP_RANGES or
               ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any
               other RouterNat section in any Router for this network in this region.
               Possible values are `ALL_SUBNETWORKS_ALL_IP_RANGES`, `ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES`, and `LIST_OF_SUBNETWORKS`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouterNatSubnetworkArgs']]]] subnetworks: One or more subnetwork NAT configurations. Only used if
               `source_subnetwork_ip_ranges_to_nat` is set to `LIST_OF_SUBNETWORKS`
               Structure is documented below.
        :param pulumi.Input[int] tcp_established_idle_timeout_sec: Timeout (in seconds) for TCP established connections.
               Defaults to 1200s if not set.
        :param pulumi.Input[int] tcp_transitory_idle_timeout_sec: Timeout (in seconds) for TCP transitory connections.
               Defaults to 30s if not set.
        :param pulumi.Input[int] udp_idle_timeout_sec: Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["drain_nat_ips"] = drain_nat_ips
        __props__["icmp_idle_timeout_sec"] = icmp_idle_timeout_sec
        __props__["log_config"] = log_config
        __props__["min_ports_per_vm"] = min_ports_per_vm
        __props__["name"] = name
        __props__["nat_ip_allocate_option"] = nat_ip_allocate_option
        __props__["nat_ips"] = nat_ips
        __props__["project"] = project
        __props__["region"] = region
        __props__["router"] = router
        __props__["source_subnetwork_ip_ranges_to_nat"] = source_subnetwork_ip_ranges_to_nat
        __props__["subnetworks"] = subnetworks
        __props__["tcp_established_idle_timeout_sec"] = tcp_established_idle_timeout_sec
        __props__["tcp_transitory_idle_timeout_sec"] = tcp_transitory_idle_timeout_sec
        __props__["udp_idle_timeout_sec"] = udp_idle_timeout_sec
        return RouterNat(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="drainNatIps")
    def drain_nat_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of URLs of the IP resources to be drained. These IPs must be
        valid static external IPs that have been assigned to the NAT.
        """
        return pulumi.get(self, "drain_nat_ips")

    @property
    @pulumi.getter(name="icmpIdleTimeoutSec")
    def icmp_idle_timeout_sec(self) -> pulumi.Output[Optional[int]]:
        """
        Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
        """
        return pulumi.get(self, "icmp_idle_timeout_sec")

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[Optional['outputs.RouterNatLogConfig']]:
        """
        Configuration for logging on NAT
        Structure is documented below.
        """
        return pulumi.get(self, "log_config")

    @property
    @pulumi.getter(name="minPortsPerVm")
    def min_ports_per_vm(self) -> pulumi.Output[Optional[int]]:
        """
        Minimum number of ports allocated to a VM from this NAT.
        """
        return pulumi.get(self, "min_ports_per_vm")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Self-link of subnetwork to NAT
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natIpAllocateOption")
    def nat_ip_allocate_option(self) -> pulumi.Output[str]:
        """
        How external IPs should be allocated for this NAT. Valid values are
        `AUTO_ONLY` for only allowing NAT IPs allocated by Google Cloud
        Platform, or `MANUAL_ONLY` for only user-allocated NAT IP addresses.
        Possible values are `MANUAL_ONLY` and `AUTO_ONLY`.
        """
        return pulumi.get(self, "nat_ip_allocate_option")

    @property
    @pulumi.getter(name="natIps")
    def nat_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Self-links of NAT IPs. Only valid if natIpAllocateOption
        is set to MANUAL_ONLY.
        """
        return pulumi.get(self, "nat_ips")

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
        Region where the router and NAT reside.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def router(self) -> pulumi.Output[str]:
        """
        The name of the Cloud Router in which this NAT will be configured.
        """
        return pulumi.get(self, "router")

    @property
    @pulumi.getter(name="sourceSubnetworkIpRangesToNat")
    def source_subnetwork_ip_ranges_to_nat(self) -> pulumi.Output[str]:
        """
        How NAT should be configured per Subnetwork.
        If `ALL_SUBNETWORKS_ALL_IP_RANGES`, all of the
        IP ranges in every Subnetwork are allowed to Nat.
        If `ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES`, all of the primary IP
        ranges in every Subnetwork are allowed to Nat.
        `LIST_OF_SUBNETWORKS`: A list of Subnetworks are allowed to Nat
        (specified in the field subnetwork below). Note that if this field
        contains ALL_SUBNETWORKS_ALL_IP_RANGES or
        ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any
        other RouterNat section in any Router for this network in this region.
        Possible values are `ALL_SUBNETWORKS_ALL_IP_RANGES`, `ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES`, and `LIST_OF_SUBNETWORKS`.
        """
        return pulumi.get(self, "source_subnetwork_ip_ranges_to_nat")

    @property
    @pulumi.getter
    def subnetworks(self) -> pulumi.Output[Optional[Sequence['outputs.RouterNatSubnetwork']]]:
        """
        One or more subnetwork NAT configurations. Only used if
        `source_subnetwork_ip_ranges_to_nat` is set to `LIST_OF_SUBNETWORKS`
        Structure is documented below.
        """
        return pulumi.get(self, "subnetworks")

    @property
    @pulumi.getter(name="tcpEstablishedIdleTimeoutSec")
    def tcp_established_idle_timeout_sec(self) -> pulumi.Output[Optional[int]]:
        """
        Timeout (in seconds) for TCP established connections.
        Defaults to 1200s if not set.
        """
        return pulumi.get(self, "tcp_established_idle_timeout_sec")

    @property
    @pulumi.getter(name="tcpTransitoryIdleTimeoutSec")
    def tcp_transitory_idle_timeout_sec(self) -> pulumi.Output[Optional[int]]:
        """
        Timeout (in seconds) for TCP transitory connections.
        Defaults to 30s if not set.
        """
        return pulumi.get(self, "tcp_transitory_idle_timeout_sec")

    @property
    @pulumi.getter(name="udpIdleTimeoutSec")
    def udp_idle_timeout_sec(self) -> pulumi.Output[Optional[int]]:
        """
        Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
        """
        return pulumi.get(self, "udp_idle_timeout_sec")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

