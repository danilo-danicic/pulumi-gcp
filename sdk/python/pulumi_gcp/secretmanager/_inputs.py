# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'SecretIamBindingConditionArgs',
    'SecretIamMemberConditionArgs',
    'SecretReplicationArgs',
    'SecretReplicationUserManagedArgs',
    'SecretReplicationUserManagedReplicaArgs',
]

@pulumi.input_type
class SecretIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class SecretIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class SecretReplicationArgs:
    def __init__(__self__, *,
                 automatic: Optional[pulumi.Input[bool]] = None,
                 user_managed: Optional[pulumi.Input['SecretReplicationUserManagedArgs']] = None):
        """
        :param pulumi.Input[bool] automatic: The Secret will automatically be replicated without any restrictions.
        :param pulumi.Input['SecretReplicationUserManagedArgs'] user_managed: The Secret will automatically be replicated without any restrictions.
               Structure is documented below.
        """
        if automatic is not None:
            pulumi.set(__self__, "automatic", automatic)
        if user_managed is not None:
            pulumi.set(__self__, "user_managed", user_managed)

    @property
    @pulumi.getter
    def automatic(self) -> Optional[pulumi.Input[bool]]:
        """
        The Secret will automatically be replicated without any restrictions.
        """
        return pulumi.get(self, "automatic")

    @automatic.setter
    def automatic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "automatic", value)

    @property
    @pulumi.getter(name="userManaged")
    def user_managed(self) -> Optional[pulumi.Input['SecretReplicationUserManagedArgs']]:
        """
        The Secret will automatically be replicated without any restrictions.
        Structure is documented below.
        """
        return pulumi.get(self, "user_managed")

    @user_managed.setter
    def user_managed(self, value: Optional[pulumi.Input['SecretReplicationUserManagedArgs']]):
        pulumi.set(self, "user_managed", value)


@pulumi.input_type
class SecretReplicationUserManagedArgs:
    def __init__(__self__, *,
                 replicas: pulumi.Input[Sequence[pulumi.Input['SecretReplicationUserManagedReplicaArgs']]]):
        """
        :param pulumi.Input[Sequence[pulumi.Input['SecretReplicationUserManagedReplicaArgs']]] replicas: The list of Replicas for this Secret. Cannot be empty.
               Structure is documented below.
        """
        pulumi.set(__self__, "replicas", replicas)

    @property
    @pulumi.getter
    def replicas(self) -> pulumi.Input[Sequence[pulumi.Input['SecretReplicationUserManagedReplicaArgs']]]:
        """
        The list of Replicas for this Secret. Cannot be empty.
        Structure is documented below.
        """
        return pulumi.get(self, "replicas")

    @replicas.setter
    def replicas(self, value: pulumi.Input[Sequence[pulumi.Input['SecretReplicationUserManagedReplicaArgs']]]):
        pulumi.set(self, "replicas", value)


@pulumi.input_type
class SecretReplicationUserManagedReplicaArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str]):
        """
        :param pulumi.Input[str] location: The canonical IDs of the location to replicate data. For example: "us-east1".
        """
        pulumi.set(__self__, "location", location)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The canonical IDs of the location to replicate data. For example: "us-east1".
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)


