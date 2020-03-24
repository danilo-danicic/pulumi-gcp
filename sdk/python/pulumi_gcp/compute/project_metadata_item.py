# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class ProjectMetadataItem(pulumi.CustomResource):
    key: pulumi.Output[str]
    """
    The metadata key to set.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs. If it
    is not provided, the provider project is used.
    """
    value: pulumi.Output[str]
    """
    The value to set for the given metadata key.
    """
    def __init__(__self__, resource_name, opts=None, key=None, project=None, value=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a single key/value pair on metadata common to all instances for
        a project in GCE. Using `compute.ProjectMetadataItem` lets you
        manage a single key/value setting in the provider rather than the entire
        project metadata map.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_metadata_item.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The metadata key to set.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] value: The value to set for the given metadata key.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if key is None:
                raise TypeError("Missing required property 'key'")
            __props__['key'] = key
            __props__['project'] = project
            if value is None:
                raise TypeError("Missing required property 'value'")
            __props__['value'] = value
        super(ProjectMetadataItem, __self__).__init__(
            'gcp:compute/projectMetadataItem:ProjectMetadataItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, key=None, project=None, value=None):
        """
        Get an existing ProjectMetadataItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The metadata key to set.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] value: The value to set for the given metadata key.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["key"] = key
        __props__["project"] = project
        __props__["value"] = value
        return ProjectMetadataItem(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

