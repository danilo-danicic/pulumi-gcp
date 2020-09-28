# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetDefaultServiceAccountResult',
    'AwaitableGetDefaultServiceAccountResult',
    'get_default_service_account',
]

@pulumi.output_type
class GetDefaultServiceAccountResult:
    """
    A collection of values returned by getDefaultServiceAccount.
    """
    def __init__(__self__, email=None, id=None, project=None):
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address of the service account. This value is often used to refer to the service account
        in order to grant IAM permissions.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")


class AwaitableGetDefaultServiceAccountResult(GetDefaultServiceAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDefaultServiceAccountResult(
            email=self.email,
            id=self.id,
            project=self.project)


def get_default_service_account(project: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDefaultServiceAccountResult:
    """
    Get the email address of a project's unique BigQuery service account.

    Each Google Cloud project has a unique service account used by BigQuery. When using
    BigQuery with [customer-managed encryption keys](https://cloud.google.com/bigquery/docs/customer-managed-encryption),
    this account needs to be granted the
    `cloudkms.cryptoKeyEncrypterDecrypter` IAM role on the customer-managed Cloud KMS key used to protect the data.

    For more information see
    [the API reference](https://cloud.google.com/bigquery/docs/reference/rest/v2/projects/getServiceAccount).


    :param str project: The project the unique service account was created for. If it is not provided, the provider project is used.
    """
    __args__ = dict()
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:bigquery/getDefaultServiceAccount:getDefaultServiceAccount', __args__, opts=opts, typ=GetDefaultServiceAccountResult).value

    return AwaitableGetDefaultServiceAccountResult(
        email=__ret__.email,
        id=__ret__.id,
        project=__ret__.project)
