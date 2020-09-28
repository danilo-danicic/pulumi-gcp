# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetTestablePermissionsResult',
    'AwaitableGetTestablePermissionsResult',
    'get_testable_permissions',
]

@pulumi.output_type
class GetTestablePermissionsResult:
    """
    A collection of values returned by getTestablePermissions.
    """
    def __init__(__self__, custom_support_level=None, full_resource_name=None, id=None, permissions=None, stages=None):
        if custom_support_level and not isinstance(custom_support_level, str):
            raise TypeError("Expected argument 'custom_support_level' to be a str")
        pulumi.set(__self__, "custom_support_level", custom_support_level)
        if full_resource_name and not isinstance(full_resource_name, str):
            raise TypeError("Expected argument 'full_resource_name' to be a str")
        pulumi.set(__self__, "full_resource_name", full_resource_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if stages and not isinstance(stages, list):
            raise TypeError("Expected argument 'stages' to be a list")
        pulumi.set(__self__, "stages", stages)

    @property
    @pulumi.getter(name="customSupportLevel")
    def custom_support_level(self) -> Optional[str]:
        """
        The the support level of this permission for custom roles.
        """
        return pulumi.get(self, "custom_support_level")

    @property
    @pulumi.getter(name="fullResourceName")
    def full_resource_name(self) -> str:
        return pulumi.get(self, "full_resource_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def permissions(self) -> Sequence['outputs.GetTestablePermissionsPermissionResult']:
        """
        A list of permissions matching the provided input. Structure is defined below.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def stages(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "stages")


class AwaitableGetTestablePermissionsResult(GetTestablePermissionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTestablePermissionsResult(
            custom_support_level=self.custom_support_level,
            full_resource_name=self.full_resource_name,
            id=self.id,
            permissions=self.permissions,
            stages=self.stages)


def get_testable_permissions(custom_support_level: Optional[str] = None,
                             full_resource_name: Optional[str] = None,
                             stages: Optional[Sequence[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTestablePermissionsResult:
    """
    Retrieve a list of testable permissions for a resource. Testable permissions mean the permissions that user can add or remove in a role at a given resource. The resource can be referenced either via the full resource name or via a URI.


    :param str custom_support_level: The level of support for custom roles. Can be one of `"NOT_SUPPORTED"`, `"SUPPORTED"`, `"TESTING"`. Default is `"SUPPORTED"`
    :param str full_resource_name: See [full resource name documentation](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more detail.
    :param Sequence[str] stages: The acceptable release stages of the permission in the output. Note that `BETA` does not include permissions in `GA`, but you can specify both with `["GA", "BETA"]` for example. Can be a list of `"ALPHA"`, `"BETA"`, `"GA"`, `"DEPRECATED"`. Default is `["GA"]`.
    """
    __args__ = dict()
    __args__['customSupportLevel'] = custom_support_level
    __args__['fullResourceName'] = full_resource_name
    __args__['stages'] = stages
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:iam/getTestablePermissions:getTestablePermissions', __args__, opts=opts, typ=GetTestablePermissionsResult).value

    return AwaitableGetTestablePermissionsResult(
        custom_support_level=__ret__.custom_support_level,
        full_resource_name=__ret__.full_resource_name,
        id=__ret__.id,
        permissions=__ret__.permissions,
        stages=__ret__.stages)
