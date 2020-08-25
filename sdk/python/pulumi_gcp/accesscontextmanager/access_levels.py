# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['AccessLevels']


class AccessLevels(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_levels: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['AccessLevelsAccessLevelArgs']]]]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Replace all existing Access Levels in an Access Policy with the Access Levels provided. This is done atomically.
        This is a bulk edit of all Access Levels and may override existing Access Levels created by `accesscontextmanager.AccessLevel`,
        thus causing a permadiff if used alongside `accesscontextmanager.AccessLevel` on the same parent.

        To get more information about AccessLevels, see:

        * [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels)
        * How-to Guides
            * [Access Policy Quickstart](https://cloud.google.com/access-context-manager/docs/quickstart)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['AccessLevelsAccessLevelArgs']]]] access_levels: The desired Access Levels that should replace all existing Access Levels in the Access Policy.
               Structure is documented below.
        :param pulumi.Input[str] parent: The AccessPolicy this AccessLevel lives in.
               Format: accessPolicies/{policy_id}
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

            __props__['access_levels'] = access_levels
            if parent is None:
                raise TypeError("Missing required property 'parent'")
            __props__['parent'] = parent
        super(AccessLevels, __self__).__init__(
            'gcp:accesscontextmanager/accessLevels:AccessLevels',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_levels: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['AccessLevelsAccessLevelArgs']]]]] = None,
            parent: Optional[pulumi.Input[str]] = None) -> 'AccessLevels':
        """
        Get an existing AccessLevels resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['AccessLevelsAccessLevelArgs']]]] access_levels: The desired Access Levels that should replace all existing Access Levels in the Access Policy.
               Structure is documented below.
        :param pulumi.Input[str] parent: The AccessPolicy this AccessLevel lives in.
               Format: accessPolicies/{policy_id}
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_levels"] = access_levels
        __props__["parent"] = parent
        return AccessLevels(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[List['outputs.AccessLevelsAccessLevel']]:
        """
        The desired Access Levels that should replace all existing Access Levels in the Access Policy.
        Structure is documented below.
        """
        return pulumi.get(self, "access_levels")

    @property
    @pulumi.getter
    def parent(self) -> str:
        """
        The AccessPolicy this AccessLevel lives in.
        Format: accessPolicies/{policy_id}
        """
        return pulumi.get(self, "parent")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

