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

__all__ = ['AccessLevelCondition']


class AccessLevelCondition(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_level: Optional[pulumi.Input[str]] = None,
                 device_policy: Optional[pulumi.Input[pulumi.InputType['AccessLevelConditionDevicePolicyArgs']]] = None,
                 ip_subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 negate: Optional[pulumi.Input[bool]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 required_access_levels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows configuring a single access level condition to be appended to an access level's conditions.
        This resource is intended to be used in cases where it is not possible to compile a full list
        of conditions to include in a `accesscontextmanager.AccessLevel` resource,
        to enable them to be added separately.

        > **Note:** If this resource is used alongside a `accesscontextmanager.AccessLevel` resource,
        the access level resource must have a `lifecycle` block with `ignore_changes = [basic[0].conditions]` so
        they don't fight over which service accounts should be included.

        To get more information about AccessLevelCondition, see:

        * [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels)
        * How-to Guides
            * [Access Policy Quickstart](https://cloud.google.com/access-context-manager/docs/quickstart)

        > **Warning:** If you are using User ADCs (Application Default Credentials) with this resource,
        you must specify a `billing_project` and set `user_project_override` to true
        in the provider configuration. Otherwise the ACM API will return a 403 error.
        Your account must have the `serviceusage.services.use` permission on the
        `billing_project` you defined.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_level: The name of the Access Level to add this condition to.
        :param pulumi.Input[pulumi.InputType['AccessLevelConditionDevicePolicyArgs']] device_policy: Device specific restrictions, all restrictions must hold for
               the Condition to be true. If not specified, all devices are
               allowed.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_subnetworks: A list of CIDR block IP subnetwork specification. May be IPv4
               or IPv6.
               Note that for a CIDR IP address block, the specified IP address
               portion must be properly truncated (i.e. all the host bits must
               be zero) or the input is considered malformed. For example,
               "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. Similarly,
               for IPv6, "2001:db8::/32" is accepted whereas "2001:db8::1/32"
               is not. The originating IP of a request must be in one of the
               listed subnets in order for this Condition to be true.
               If empty, all IP addresses are allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: An allowed list of members (users, service accounts).
               Using groups is not supported yet.
               The signed-in user originating the request must be a part of one
               of the provided members. If not specified, a request may come
               from any user (logged in/not logged in, not present in any
               groups, etc.).
               Formats: `user:{emailid}`, `serviceAccount:{emailid}`
        :param pulumi.Input[bool] negate: Whether to negate the Condition. If true, the Condition becomes
               a NAND over its non-empty fields, each field must be false for
               the Condition overall to be satisfied. Defaults to false.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: The request must originate from one of the provided
               countries/regions.
               Format: A valid ISO 3166-1 alpha-2 code.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] required_access_levels: A list of other access levels defined in the same Policy,
               referenced by resource name. Referencing an AccessLevel which
               does not exist is an error. All access levels listed must be
               granted for the Condition to be true.
               Format: accessPolicies/{policy_id}/accessLevels/{short_name}
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

            if access_level is None:
                raise TypeError("Missing required property 'access_level'")
            __props__['access_level'] = access_level
            __props__['device_policy'] = device_policy
            __props__['ip_subnetworks'] = ip_subnetworks
            __props__['members'] = members
            __props__['negate'] = negate
            __props__['regions'] = regions
            __props__['required_access_levels'] = required_access_levels
        super(AccessLevelCondition, __self__).__init__(
            'gcp:accesscontextmanager/accessLevelCondition:AccessLevelCondition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_level: Optional[pulumi.Input[str]] = None,
            device_policy: Optional[pulumi.Input[pulumi.InputType['AccessLevelConditionDevicePolicyArgs']]] = None,
            ip_subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            negate: Optional[pulumi.Input[bool]] = None,
            regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            required_access_levels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'AccessLevelCondition':
        """
        Get an existing AccessLevelCondition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_level: The name of the Access Level to add this condition to.
        :param pulumi.Input[pulumi.InputType['AccessLevelConditionDevicePolicyArgs']] device_policy: Device specific restrictions, all restrictions must hold for
               the Condition to be true. If not specified, all devices are
               allowed.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_subnetworks: A list of CIDR block IP subnetwork specification. May be IPv4
               or IPv6.
               Note that for a CIDR IP address block, the specified IP address
               portion must be properly truncated (i.e. all the host bits must
               be zero) or the input is considered malformed. For example,
               "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. Similarly,
               for IPv6, "2001:db8::/32" is accepted whereas "2001:db8::1/32"
               is not. The originating IP of a request must be in one of the
               listed subnets in order for this Condition to be true.
               If empty, all IP addresses are allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: An allowed list of members (users, service accounts).
               Using groups is not supported yet.
               The signed-in user originating the request must be a part of one
               of the provided members. If not specified, a request may come
               from any user (logged in/not logged in, not present in any
               groups, etc.).
               Formats: `user:{emailid}`, `serviceAccount:{emailid}`
        :param pulumi.Input[bool] negate: Whether to negate the Condition. If true, the Condition becomes
               a NAND over its non-empty fields, each field must be false for
               the Condition overall to be satisfied. Defaults to false.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: The request must originate from one of the provided
               countries/regions.
               Format: A valid ISO 3166-1 alpha-2 code.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] required_access_levels: A list of other access levels defined in the same Policy,
               referenced by resource name. Referencing an AccessLevel which
               does not exist is an error. All access levels listed must be
               granted for the Condition to be true.
               Format: accessPolicies/{policy_id}/accessLevels/{short_name}
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_level"] = access_level
        __props__["device_policy"] = device_policy
        __props__["ip_subnetworks"] = ip_subnetworks
        __props__["members"] = members
        __props__["negate"] = negate
        __props__["regions"] = regions
        __props__["required_access_levels"] = required_access_levels
        return AccessLevelCondition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> pulumi.Output[str]:
        """
        The name of the Access Level to add this condition to.
        """
        return pulumi.get(self, "access_level")

    @property
    @pulumi.getter(name="devicePolicy")
    def device_policy(self) -> pulumi.Output[Optional['outputs.AccessLevelConditionDevicePolicy']]:
        """
        Device specific restrictions, all restrictions must hold for
        the Condition to be true. If not specified, all devices are
        allowed.
        Structure is documented below.
        """
        return pulumi.get(self, "device_policy")

    @property
    @pulumi.getter(name="ipSubnetworks")
    def ip_subnetworks(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of CIDR block IP subnetwork specification. May be IPv4
        or IPv6.
        Note that for a CIDR IP address block, the specified IP address
        portion must be properly truncated (i.e. all the host bits must
        be zero) or the input is considered malformed. For example,
        "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. Similarly,
        for IPv6, "2001:db8::/32" is accepted whereas "2001:db8::1/32"
        is not. The originating IP of a request must be in one of the
        listed subnets in order for this Condition to be true.
        If empty, all IP addresses are allowed.
        """
        return pulumi.get(self, "ip_subnetworks")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        An allowed list of members (users, service accounts).
        Using groups is not supported yet.
        The signed-in user originating the request must be a part of one
        of the provided members. If not specified, a request may come
        from any user (logged in/not logged in, not present in any
        groups, etc.).
        Formats: `user:{emailid}`, `serviceAccount:{emailid}`
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def negate(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to negate the Condition. If true, the Condition becomes
        a NAND over its non-empty fields, each field must be false for
        the Condition overall to be satisfied. Defaults to false.
        """
        return pulumi.get(self, "negate")

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The request must originate from one of the provided
        countries/regions.
        Format: A valid ISO 3166-1 alpha-2 code.
        """
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter(name="requiredAccessLevels")
    def required_access_levels(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of other access levels defined in the same Policy,
        referenced by resource name. Referencing an AccessLevel which
        does not exist is an error. All access levels listed must be
        granted for the Condition to be true.
        Format: accessPolicies/{policy_id}/accessLevels/{short_name}
        """
        return pulumi.get(self, "required_access_levels")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

