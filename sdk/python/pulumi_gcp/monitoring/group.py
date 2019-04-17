# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Group(pulumi.CustomResource):
    display_name: pulumi.Output[str]
    filter: pulumi.Output[str]
    is_cluster: pulumi.Output[bool]
    name: pulumi.Output[str]
    parent_name: pulumi.Output[str]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    def __init__(__self__, resource_name, opts=None, display_name=None, filter=None, is_cluster=None, parent_name=None, project=None, __name__=None, __opts__=None):
        """
        The description of a dynamic collection of monitored resources. Each group
        has a filter that is matched against monitored resources and their
        associated metadata. If a group's filter matches an available monitored
        resource, then that resource is a member of that group.
        
        
        To get more information about Group, see:
        
        * [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/monitoring/groups/)
        
        <div class = "oics-button" style="float: right; margin: 0 0 -15px">
          <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=monitoring_group_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
            <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
          </a>
        </div>
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if display_name is None:
            raise TypeError("Missing required property 'display_name'")
        __props__['display_name'] = display_name

        if filter is None:
            raise TypeError("Missing required property 'filter'")
        __props__['filter'] = filter

        __props__['is_cluster'] = is_cluster

        __props__['parent_name'] = parent_name

        __props__['project'] = project

        __props__['name'] = None

        super(Group, __self__).__init__(
            'gcp:monitoring/group:Group',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

