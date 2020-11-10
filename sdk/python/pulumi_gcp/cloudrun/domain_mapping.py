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

__all__ = ['DomainMapping']


class DomainMapping(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['DomainMappingMetadataArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Resource to hold the state and status of a user's domain mapping.

        To get more information about DomainMapping, see:

        * [API documentation](https://cloud.google.com/run/docs/reference/rest/v1/projects.locations.domainmappings)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/run/docs/mapping-custom-domains)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The location of the cloud run instance. eg us-central1
        :param pulumi.Input[pulumi.InputType['DomainMappingMetadataArgs']] metadata: Metadata associated with this DomainMapping.
               Structure is documented below.
        :param pulumi.Input[str] name: Name should be a verified domain
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']] spec: The spec for this DomainMapping.
               Structure is documented below.
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

            if location is None:
                raise TypeError("Missing required property 'location'")
            __props__['location'] = location
            if metadata is None:
                raise TypeError("Missing required property 'metadata'")
            __props__['metadata'] = metadata
            __props__['name'] = name
            __props__['project'] = project
            if spec is None:
                raise TypeError("Missing required property 'spec'")
            __props__['spec'] = spec
            __props__['statuses'] = None
        super(DomainMapping, __self__).__init__(
            'gcp:cloudrun/domainMapping:DomainMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            location: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[pulumi.InputType['DomainMappingMetadataArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            spec: Optional[pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']]] = None,
            statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainMappingStatusArgs']]]]] = None) -> 'DomainMapping':
        """
        Get an existing DomainMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The location of the cloud run instance. eg us-central1
        :param pulumi.Input[pulumi.InputType['DomainMappingMetadataArgs']] metadata: Metadata associated with this DomainMapping.
               Structure is documented below.
        :param pulumi.Input[str] name: Name should be a verified domain
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['DomainMappingSpecArgs']] spec: The spec for this DomainMapping.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainMappingStatusArgs']]]] statuses: The current status of the DomainMapping.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["location"] = location
        __props__["metadata"] = metadata
        __props__["name"] = name
        __props__["project"] = project
        __props__["spec"] = spec
        __props__["statuses"] = statuses
        return DomainMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the cloud run instance. eg us-central1
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.DomainMappingMetadata']:
        """
        Metadata associated with this DomainMapping.
        Structure is documented below.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name should be a verified domain
        """
        return pulumi.get(self, "name")

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
    def spec(self) -> pulumi.Output['outputs.DomainMappingSpec']:
        """
        The spec for this DomainMapping.
        Structure is documented below.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence['outputs.DomainMappingStatus']]:
        """
        The current status of the DomainMapping.
        """
        return pulumi.get(self, "statuses")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

