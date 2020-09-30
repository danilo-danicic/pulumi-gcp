# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ServiceIdentity']


class ServiceIdentity(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Generate service identity for a service.

        > **Note**: Once created, this resource cannot be updated or destroyed. These
        actions are a no-op.

        To get more information about Service Identity, see:

        * [API documentation](https://cloud.google.com/service-usage/docs/reference/rest/v1beta1/services/generateServiceIdentity)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] service: The service to generate identity for.
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

            __props__['project'] = project
            if service is None:
                raise TypeError("Missing required property 'service'")
            __props__['service'] = service
            __props__['email'] = None
        super(ServiceIdentity, __self__).__init__(
            'gcp:projects/serviceIdentity:ServiceIdentity',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            email: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            service: Optional[pulumi.Input[str]] = None) -> 'ServiceIdentity':
        """
        Get an existing ServiceIdentity resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] email: The email address of the Google managed service account.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] service: The service to generate identity for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["email"] = email
        __props__["project"] = project
        __props__["service"] = service
        return ServiceIdentity(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        The email address of the Google managed service account.
        """
        return pulumi.get(self, "email")

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
    def service(self) -> pulumi.Output[str]:
        """
        The service to generate identity for.
        """
        return pulumi.get(self, "service")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

