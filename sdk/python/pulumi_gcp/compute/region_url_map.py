# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class RegionUrlMap(pulumi.CustomResource):
    creation_timestamp: pulumi.Output[str]
    default_service: pulumi.Output[str]
    description: pulumi.Output[str]
    fingerprint: pulumi.Output[str]
    host_rules: pulumi.Output[list]
    map_id: pulumi.Output[float]
    name: pulumi.Output[str]
    path_matchers: pulumi.Output[list]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    region: pulumi.Output[str]
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    tests: pulumi.Output[list]
    def __init__(__self__, resource_name, opts=None, default_service=None, description=None, host_rules=None, name=None, path_matchers=None, project=None, region=None, tests=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a RegionUrlMap resource with the given unique name, props, and options.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        
        The **host_rules** object supports the following:
        
          * `description` (`pulumi.Input[str]`)
          * `hosts` (`pulumi.Input[list]`)
          * `pathMatcher` (`pulumi.Input[str]`)
        
        The **path_matchers** object supports the following:
        
          * `default_service` (`pulumi.Input[str]`)
          * `description` (`pulumi.Input[str]`)
          * `name` (`pulumi.Input[str]`)
          * `pathRules` (`pulumi.Input[list]`)
        
            * `paths` (`pulumi.Input[list]`)
            * `service` (`pulumi.Input[str]`)
        
        The **tests** object supports the following:
        
          * `description` (`pulumi.Input[str]`)
          * `host` (`pulumi.Input[str]`)
          * `path` (`pulumi.Input[str]`)
          * `service` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_url_map.html.markdown.
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

            if default_service is None:
                raise TypeError("Missing required property 'default_service'")
            __props__['default_service'] = default_service
            __props__['description'] = description
            __props__['host_rules'] = host_rules
            __props__['name'] = name
            __props__['path_matchers'] = path_matchers
            __props__['project'] = project
            __props__['region'] = region
            __props__['tests'] = tests
            __props__['creation_timestamp'] = None
            __props__['fingerprint'] = None
            __props__['map_id'] = None
            __props__['self_link'] = None
        super(RegionUrlMap, __self__).__init__(
            'gcp:compute/regionUrlMap:RegionUrlMap',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, creation_timestamp=None, default_service=None, description=None, fingerprint=None, host_rules=None, map_id=None, name=None, path_matchers=None, project=None, region=None, self_link=None, tests=None):
        """
        Get an existing RegionUrlMap resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        
        The **host_rules** object supports the following:
        
          * `description` (`pulumi.Input[str]`)
          * `hosts` (`pulumi.Input[list]`)
          * `pathMatcher` (`pulumi.Input[str]`)
        
        The **path_matchers** object supports the following:
        
          * `default_service` (`pulumi.Input[str]`)
          * `description` (`pulumi.Input[str]`)
          * `name` (`pulumi.Input[str]`)
          * `pathRules` (`pulumi.Input[list]`)
        
            * `paths` (`pulumi.Input[list]`)
            * `service` (`pulumi.Input[str]`)
        
        The **tests** object supports the following:
        
          * `description` (`pulumi.Input[str]`)
          * `host` (`pulumi.Input[str]`)
          * `path` (`pulumi.Input[str]`)
          * `service` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_url_map.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["creation_timestamp"] = creation_timestamp
        __props__["default_service"] = default_service
        __props__["description"] = description
        __props__["fingerprint"] = fingerprint
        __props__["host_rules"] = host_rules
        __props__["map_id"] = map_id
        __props__["name"] = name
        __props__["path_matchers"] = path_matchers
        __props__["project"] = project
        __props__["region"] = region
        __props__["self_link"] = self_link
        __props__["tests"] = tests
        return RegionUrlMap(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
