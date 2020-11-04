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

__all__ = ['RegionBackendService']


class RegionBackendService(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 affinity_cookie_ttl_sec: Optional[pulumi.Input[int]] = None,
                 backends: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegionBackendServiceBackendArgs']]]]] = None,
                 circuit_breakers: Optional[pulumi.Input[pulumi.InputType['RegionBackendServiceCircuitBreakersArgs']]] = None,
                 connection_draining_timeout_sec: Optional[pulumi.Input[int]] = None,
                 consistent_hash: Optional[pulumi.Input[pulumi.InputType['RegionBackendServiceConsistentHashArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 failover_policy: Optional[pulumi.Input[pulumi.InputType['RegionBackendServiceFailoverPolicyArgs']]] = None,
                 health_checks: Optional[pulumi.Input[str]] = None,
                 load_balancing_scheme: Optional[pulumi.Input[str]] = None,
                 locality_lb_policy: Optional[pulumi.Input[str]] = None,
                 log_config: Optional[pulumi.Input[pulumi.InputType['RegionBackendServiceLogConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 outlier_detection: Optional[pulumi.Input[pulumi.InputType['RegionBackendServiceOutlierDetectionArgs']]] = None,
                 port_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 session_affinity: Optional[pulumi.Input[str]] = None,
                 timeout_sec: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A Region Backend Service defines a regionally-scoped group of virtual
        machines that will serve traffic for load balancing.

        To get more information about RegionBackendService, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/latest/regionBackendServices)
        * How-to Guides
            * [Internal TCP/UDP Load Balancing](https://cloud.google.com/compute/docs/load-balancing/internal/)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] affinity_cookie_ttl_sec: Lifetime of cookies in seconds if session_affinity is
               GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
               only until the end of the browser session (or equivalent). The
               maximum allowed value for TTL is one day.
               When the load balancing scheme is INTERNAL, this field is not used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegionBackendServiceBackendArgs']]]] backends: The set of backends that serve this RegionBackendService.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionBackendServiceCircuitBreakersArgs']] circuit_breakers: Settings controlling the volume of connections to a backend service. This field
               is applicable only when the `load_balancing_scheme` is set to INTERNAL_MANAGED
               and the `protocol` is set to HTTP, HTTPS, or HTTP2.
               Structure is documented below.
        :param pulumi.Input[int] connection_draining_timeout_sec: Time for which instance will be drained (not accept new
               connections, but still work to finish started).
        :param pulumi.Input[pulumi.InputType['RegionBackendServiceConsistentHashArgs']] consistent_hash: Consistent Hash-based load balancing can be used to provide soft session
               affinity based on HTTP headers, cookies or other properties. This load balancing
               policy is applicable only for HTTP connections. The affinity to a particular
               destination host will be lost when one or more hosts are added/removed from the
               destination service. This field specifies parameters that control consistent
               hashing.
               This field only applies when all of the following are true -
        :param pulumi.Input[str] description: An optional description of this resource.
               Provide this property when you create the resource.
        :param pulumi.Input[pulumi.InputType['RegionBackendServiceFailoverPolicyArgs']] failover_policy: Policy for failovers.
               Structure is documented below.
        :param pulumi.Input[str] health_checks: The set of URLs to HealthCheck resources for health checking
               this RegionBackendService. Currently at most one health
               check can be specified.
               A health check must be specified unless the backend service uses an internet
               or serverless NEG as a backend.
        :param pulumi.Input[str] load_balancing_scheme: Indicates what kind of load balancing this regional backend service
               will be used for. A backend service created for one type of load
               balancing cannot be used with the other(s).
               Default value is `INTERNAL`.
               Possible values are `EXTERNAL`, `INTERNAL`, and `INTERNAL_MANAGED`.
        :param pulumi.Input[str] locality_lb_policy: The load balancing algorithm used within the scope of the locality.
               The possible values are -
               * ROUND_ROBIN - This is a simple policy in which each healthy backend
               is selected in round robin order.
               * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
               hosts and picks the host which has fewer active requests.
               * RING_HASH - The ring/modulo hash load balancer implements consistent
               hashing to backends. The algorithm has the property that the
               addition/removal of a host from a set of N hosts only affects
               1/N of the requests.
               * RANDOM - The load balancer selects a random healthy host.
               * ORIGINAL_DESTINATION - Backend host is selected based on the client
               connection metadata, i.e., connections are opened
               to the same address as the destination address of
               the incoming connection before the connection
               was redirected to the load balancer.
               * MAGLEV - used as a drop in replacement for the ring hash load balancer.
               Maglev is not as stable as ring hash but has faster table lookup
               build times and host selection times. For more information about
               Maglev, refer to https://ai.google/research/pubs/pub44824
               This field is applicable only when the `load_balancing_scheme` is set to
               INTERNAL_MANAGED and the `protocol` is set to HTTP, HTTPS, or HTTP2.
               Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
        :param pulumi.Input[pulumi.InputType['RegionBackendServiceLogConfigArgs']] log_config: This field denotes the logging options for the load balancer traffic served by this backend service.
               If logging is enabled, logs will be exported to Stackdriver.
               Structure is documented below.
        :param pulumi.Input[str] name: Name of the cookie.
        :param pulumi.Input[str] network: The URL of the network to which this backend service belongs.
               This field can only be specified when the load balancing scheme is set to INTERNAL.
        :param pulumi.Input[pulumi.InputType['RegionBackendServiceOutlierDetectionArgs']] outlier_detection: Settings controlling eviction of unhealthy hosts from the load balancing pool.
               This field is applicable only when the `load_balancing_scheme` is set
               to INTERNAL_MANAGED and the `protocol` is set to HTTP, HTTPS, or HTTP2.
               Structure is documented below.
        :param pulumi.Input[str] port_name: A named port on a backend instance group representing the port for
               communication to the backend VMs in that group. Required when the
               loadBalancingScheme is EXTERNAL, INTERNAL_MANAGED, or INTERNAL_SELF_MANAGED
               and the backends are instance groups. The named port must be defined on each
               backend instance group. This parameter has no meaning if the backends are NEGs. API sets a
               default of "http" if not given.
               Must be omitted when the loadBalancingScheme is INTERNAL (Internal TCP/UDP Load Balancing).
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] protocol: The protocol this RegionBackendService uses to communicate with backends.
               The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
               types and may result in errors if used with the GA API.
               Possible values are `HTTP`, `HTTPS`, `HTTP2`, `SSL`, `TCP`, `UDP`, and `GRPC`.
        :param pulumi.Input[str] region: The Region in which the created backend service should reside.
               If it is not provided, the provider region is used.
        :param pulumi.Input[str] session_affinity: Type of session affinity to use. The default is NONE. Session affinity is
               not applicable if the protocol is UDP.
               Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
        :param pulumi.Input[int] timeout_sec: How many seconds to wait for the backend before considering it a
               failed request. Default is 30 seconds. Valid range is [1, 86400].
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

            __props__['affinity_cookie_ttl_sec'] = affinity_cookie_ttl_sec
            __props__['backends'] = backends
            __props__['circuit_breakers'] = circuit_breakers
            __props__['connection_draining_timeout_sec'] = connection_draining_timeout_sec
            __props__['consistent_hash'] = consistent_hash
            __props__['description'] = description
            __props__['failover_policy'] = failover_policy
            __props__['health_checks'] = health_checks
            __props__['load_balancing_scheme'] = load_balancing_scheme
            __props__['locality_lb_policy'] = locality_lb_policy
            __props__['log_config'] = log_config
            __props__['name'] = name
            __props__['network'] = network
            __props__['outlier_detection'] = outlier_detection
            __props__['port_name'] = port_name
            __props__['project'] = project
            __props__['protocol'] = protocol
            __props__['region'] = region
            __props__['session_affinity'] = session_affinity
            __props__['timeout_sec'] = timeout_sec
            __props__['creation_timestamp'] = None
            __props__['fingerprint'] = None
            __props__['self_link'] = None
        super(RegionBackendService, __self__).__init__(
            'gcp:compute/regionBackendService:RegionBackendService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            affinity_cookie_ttl_sec: Optional[pulumi.Input[int]] = None,
            backends: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegionBackendServiceBackendArgs']]]]] = None,
            circuit_breakers: Optional[pulumi.Input[pulumi.InputType['RegionBackendServiceCircuitBreakersArgs']]] = None,
            connection_draining_timeout_sec: Optional[pulumi.Input[int]] = None,
            consistent_hash: Optional[pulumi.Input[pulumi.InputType['RegionBackendServiceConsistentHashArgs']]] = None,
            creation_timestamp: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            failover_policy: Optional[pulumi.Input[pulumi.InputType['RegionBackendServiceFailoverPolicyArgs']]] = None,
            fingerprint: Optional[pulumi.Input[str]] = None,
            health_checks: Optional[pulumi.Input[str]] = None,
            load_balancing_scheme: Optional[pulumi.Input[str]] = None,
            locality_lb_policy: Optional[pulumi.Input[str]] = None,
            log_config: Optional[pulumi.Input[pulumi.InputType['RegionBackendServiceLogConfigArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network: Optional[pulumi.Input[str]] = None,
            outlier_detection: Optional[pulumi.Input[pulumi.InputType['RegionBackendServiceOutlierDetectionArgs']]] = None,
            port_name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            session_affinity: Optional[pulumi.Input[str]] = None,
            timeout_sec: Optional[pulumi.Input[int]] = None) -> 'RegionBackendService':
        """
        Get an existing RegionBackendService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] affinity_cookie_ttl_sec: Lifetime of cookies in seconds if session_affinity is
               GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
               only until the end of the browser session (or equivalent). The
               maximum allowed value for TTL is one day.
               When the load balancing scheme is INTERNAL, this field is not used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RegionBackendServiceBackendArgs']]]] backends: The set of backends that serve this RegionBackendService.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['RegionBackendServiceCircuitBreakersArgs']] circuit_breakers: Settings controlling the volume of connections to a backend service. This field
               is applicable only when the `load_balancing_scheme` is set to INTERNAL_MANAGED
               and the `protocol` is set to HTTP, HTTPS, or HTTP2.
               Structure is documented below.
        :param pulumi.Input[int] connection_draining_timeout_sec: Time for which instance will be drained (not accept new
               connections, but still work to finish started).
        :param pulumi.Input[pulumi.InputType['RegionBackendServiceConsistentHashArgs']] consistent_hash: Consistent Hash-based load balancing can be used to provide soft session
               affinity based on HTTP headers, cookies or other properties. This load balancing
               policy is applicable only for HTTP connections. The affinity to a particular
               destination host will be lost when one or more hosts are added/removed from the
               destination service. This field specifies parameters that control consistent
               hashing.
               This field only applies when all of the following are true -
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource.
               Provide this property when you create the resource.
        :param pulumi.Input[pulumi.InputType['RegionBackendServiceFailoverPolicyArgs']] failover_policy: Policy for failovers.
               Structure is documented below.
        :param pulumi.Input[str] fingerprint: Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
        :param pulumi.Input[str] health_checks: The set of URLs to HealthCheck resources for health checking
               this RegionBackendService. Currently at most one health
               check can be specified.
               A health check must be specified unless the backend service uses an internet
               or serverless NEG as a backend.
        :param pulumi.Input[str] load_balancing_scheme: Indicates what kind of load balancing this regional backend service
               will be used for. A backend service created for one type of load
               balancing cannot be used with the other(s).
               Default value is `INTERNAL`.
               Possible values are `EXTERNAL`, `INTERNAL`, and `INTERNAL_MANAGED`.
        :param pulumi.Input[str] locality_lb_policy: The load balancing algorithm used within the scope of the locality.
               The possible values are -
               * ROUND_ROBIN - This is a simple policy in which each healthy backend
               is selected in round robin order.
               * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
               hosts and picks the host which has fewer active requests.
               * RING_HASH - The ring/modulo hash load balancer implements consistent
               hashing to backends. The algorithm has the property that the
               addition/removal of a host from a set of N hosts only affects
               1/N of the requests.
               * RANDOM - The load balancer selects a random healthy host.
               * ORIGINAL_DESTINATION - Backend host is selected based on the client
               connection metadata, i.e., connections are opened
               to the same address as the destination address of
               the incoming connection before the connection
               was redirected to the load balancer.
               * MAGLEV - used as a drop in replacement for the ring hash load balancer.
               Maglev is not as stable as ring hash but has faster table lookup
               build times and host selection times. For more information about
               Maglev, refer to https://ai.google/research/pubs/pub44824
               This field is applicable only when the `load_balancing_scheme` is set to
               INTERNAL_MANAGED and the `protocol` is set to HTTP, HTTPS, or HTTP2.
               Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
        :param pulumi.Input[pulumi.InputType['RegionBackendServiceLogConfigArgs']] log_config: This field denotes the logging options for the load balancer traffic served by this backend service.
               If logging is enabled, logs will be exported to Stackdriver.
               Structure is documented below.
        :param pulumi.Input[str] name: Name of the cookie.
        :param pulumi.Input[str] network: The URL of the network to which this backend service belongs.
               This field can only be specified when the load balancing scheme is set to INTERNAL.
        :param pulumi.Input[pulumi.InputType['RegionBackendServiceOutlierDetectionArgs']] outlier_detection: Settings controlling eviction of unhealthy hosts from the load balancing pool.
               This field is applicable only when the `load_balancing_scheme` is set
               to INTERNAL_MANAGED and the `protocol` is set to HTTP, HTTPS, or HTTP2.
               Structure is documented below.
        :param pulumi.Input[str] port_name: A named port on a backend instance group representing the port for
               communication to the backend VMs in that group. Required when the
               loadBalancingScheme is EXTERNAL, INTERNAL_MANAGED, or INTERNAL_SELF_MANAGED
               and the backends are instance groups. The named port must be defined on each
               backend instance group. This parameter has no meaning if the backends are NEGs. API sets a
               default of "http" if not given.
               Must be omitted when the loadBalancingScheme is INTERNAL (Internal TCP/UDP Load Balancing).
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] protocol: The protocol this RegionBackendService uses to communicate with backends.
               The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
               types and may result in errors if used with the GA API.
               Possible values are `HTTP`, `HTTPS`, `HTTP2`, `SSL`, `TCP`, `UDP`, and `GRPC`.
        :param pulumi.Input[str] region: The Region in which the created backend service should reside.
               If it is not provided, the provider region is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[str] session_affinity: Type of session affinity to use. The default is NONE. Session affinity is
               not applicable if the protocol is UDP.
               Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
        :param pulumi.Input[int] timeout_sec: How many seconds to wait for the backend before considering it a
               failed request. Default is 30 seconds. Valid range is [1, 86400].
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["affinity_cookie_ttl_sec"] = affinity_cookie_ttl_sec
        __props__["backends"] = backends
        __props__["circuit_breakers"] = circuit_breakers
        __props__["connection_draining_timeout_sec"] = connection_draining_timeout_sec
        __props__["consistent_hash"] = consistent_hash
        __props__["creation_timestamp"] = creation_timestamp
        __props__["description"] = description
        __props__["failover_policy"] = failover_policy
        __props__["fingerprint"] = fingerprint
        __props__["health_checks"] = health_checks
        __props__["load_balancing_scheme"] = load_balancing_scheme
        __props__["locality_lb_policy"] = locality_lb_policy
        __props__["log_config"] = log_config
        __props__["name"] = name
        __props__["network"] = network
        __props__["outlier_detection"] = outlier_detection
        __props__["port_name"] = port_name
        __props__["project"] = project
        __props__["protocol"] = protocol
        __props__["region"] = region
        __props__["self_link"] = self_link
        __props__["session_affinity"] = session_affinity
        __props__["timeout_sec"] = timeout_sec
        return RegionBackendService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="affinityCookieTtlSec")
    def affinity_cookie_ttl_sec(self) -> pulumi.Output[Optional[int]]:
        """
        Lifetime of cookies in seconds if session_affinity is
        GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
        only until the end of the browser session (or equivalent). The
        maximum allowed value for TTL is one day.
        When the load balancing scheme is INTERNAL, this field is not used.
        """
        return pulumi.get(self, "affinity_cookie_ttl_sec")

    @property
    @pulumi.getter
    def backends(self) -> pulumi.Output[Optional[Sequence['outputs.RegionBackendServiceBackend']]]:
        """
        The set of backends that serve this RegionBackendService.
        Structure is documented below.
        """
        return pulumi.get(self, "backends")

    @property
    @pulumi.getter(name="circuitBreakers")
    def circuit_breakers(self) -> pulumi.Output[Optional['outputs.RegionBackendServiceCircuitBreakers']]:
        """
        Settings controlling the volume of connections to a backend service. This field
        is applicable only when the `load_balancing_scheme` is set to INTERNAL_MANAGED
        and the `protocol` is set to HTTP, HTTPS, or HTTP2.
        Structure is documented below.
        """
        return pulumi.get(self, "circuit_breakers")

    @property
    @pulumi.getter(name="connectionDrainingTimeoutSec")
    def connection_draining_timeout_sec(self) -> pulumi.Output[Optional[int]]:
        """
        Time for which instance will be drained (not accept new
        connections, but still work to finish started).
        """
        return pulumi.get(self, "connection_draining_timeout_sec")

    @property
    @pulumi.getter(name="consistentHash")
    def consistent_hash(self) -> pulumi.Output[Optional['outputs.RegionBackendServiceConsistentHash']]:
        """
        Consistent Hash-based load balancing can be used to provide soft session
        affinity based on HTTP headers, cookies or other properties. This load balancing
        policy is applicable only for HTTP connections. The affinity to a particular
        destination host will be lost when one or more hosts are added/removed from the
        destination service. This field specifies parameters that control consistent
        hashing.
        This field only applies when all of the following are true -
        """
        return pulumi.get(self, "consistent_hash")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of this resource.
        Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="failoverPolicy")
    def failover_policy(self) -> pulumi.Output[Optional['outputs.RegionBackendServiceFailoverPolicy']]:
        """
        Policy for failovers.
        Structure is documented below.
        """
        return pulumi.get(self, "failover_policy")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> pulumi.Output[Optional[str]]:
        """
        The set of URLs to HealthCheck resources for health checking
        this RegionBackendService. Currently at most one health
        check can be specified.
        A health check must be specified unless the backend service uses an internet
        or serverless NEG as a backend.
        """
        return pulumi.get(self, "health_checks")

    @property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates what kind of load balancing this regional backend service
        will be used for. A backend service created for one type of load
        balancing cannot be used with the other(s).
        Default value is `INTERNAL`.
        Possible values are `EXTERNAL`, `INTERNAL`, and `INTERNAL_MANAGED`.
        """
        return pulumi.get(self, "load_balancing_scheme")

    @property
    @pulumi.getter(name="localityLbPolicy")
    def locality_lb_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The load balancing algorithm used within the scope of the locality.
        The possible values are -
        * ROUND_ROBIN - This is a simple policy in which each healthy backend
        is selected in round robin order.
        * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
        hosts and picks the host which has fewer active requests.
        * RING_HASH - The ring/modulo hash load balancer implements consistent
        hashing to backends. The algorithm has the property that the
        addition/removal of a host from a set of N hosts only affects
        1/N of the requests.
        * RANDOM - The load balancer selects a random healthy host.
        * ORIGINAL_DESTINATION - Backend host is selected based on the client
        connection metadata, i.e., connections are opened
        to the same address as the destination address of
        the incoming connection before the connection
        was redirected to the load balancer.
        * MAGLEV - used as a drop in replacement for the ring hash load balancer.
        Maglev is not as stable as ring hash but has faster table lookup
        build times and host selection times. For more information about
        Maglev, refer to https://ai.google/research/pubs/pub44824
        This field is applicable only when the `load_balancing_scheme` is set to
        INTERNAL_MANAGED and the `protocol` is set to HTTP, HTTPS, or HTTP2.
        Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
        """
        return pulumi.get(self, "locality_lb_policy")

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[Optional['outputs.RegionBackendServiceLogConfig']]:
        """
        This field denotes the logging options for the load balancer traffic served by this backend service.
        If logging is enabled, logs will be exported to Stackdriver.
        Structure is documented below.
        """
        return pulumi.get(self, "log_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the cookie.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional[str]]:
        """
        The URL of the network to which this backend service belongs.
        This field can only be specified when the load balancing scheme is set to INTERNAL.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="outlierDetection")
    def outlier_detection(self) -> pulumi.Output[Optional['outputs.RegionBackendServiceOutlierDetection']]:
        """
        Settings controlling eviction of unhealthy hosts from the load balancing pool.
        This field is applicable only when the `load_balancing_scheme` is set
        to INTERNAL_MANAGED and the `protocol` is set to HTTP, HTTPS, or HTTP2.
        Structure is documented below.
        """
        return pulumi.get(self, "outlier_detection")

    @property
    @pulumi.getter(name="portName")
    def port_name(self) -> pulumi.Output[str]:
        """
        A named port on a backend instance group representing the port for
        communication to the backend VMs in that group. Required when the
        loadBalancingScheme is EXTERNAL, INTERNAL_MANAGED, or INTERNAL_SELF_MANAGED
        and the backends are instance groups. The named port must be defined on each
        backend instance group. This parameter has no meaning if the backends are NEGs. API sets a
        default of "http" if not given.
        Must be omitted when the loadBalancingScheme is INTERNAL (Internal TCP/UDP Load Balancing).
        """
        return pulumi.get(self, "port_name")

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
    def protocol(self) -> pulumi.Output[str]:
        """
        The protocol this RegionBackendService uses to communicate with backends.
        The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
        types and may result in errors if used with the GA API.
        Possible values are `HTTP`, `HTTPS`, `HTTP2`, `SSL`, `TCP`, `UDP`, and `GRPC`.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The Region in which the created backend service should reside.
        If it is not provided, the provider region is used.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> pulumi.Output[str]:
        """
        Type of session affinity to use. The default is NONE. Session affinity is
        not applicable if the protocol is UDP.
        Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
        """
        return pulumi.get(self, "session_affinity")

    @property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> pulumi.Output[int]:
        """
        How many seconds to wait for the backend before considering it a
        failed request. Default is 30 seconds. Valid range is [1, 86400].
        """
        return pulumi.get(self, "timeout_sec")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

