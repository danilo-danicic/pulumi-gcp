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

__all__ = ['PatchDeployment']


class PatchDeployment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 duration: Optional[pulumi.Input[str]] = None,
                 instance_filter: Optional[pulumi.Input[pulumi.InputType['PatchDeploymentInstanceFilterArgs']]] = None,
                 one_time_schedule: Optional[pulumi.Input[pulumi.InputType['PatchDeploymentOneTimeScheduleArgs']]] = None,
                 patch_config: Optional[pulumi.Input[pulumi.InputType['PatchDeploymentPatchConfigArgs']]] = None,
                 patch_deployment_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 recurring_schedule: Optional[pulumi.Input[pulumi.InputType['PatchDeploymentRecurringScheduleArgs']]] = None,
                 rollout: Optional[pulumi.Input[pulumi.InputType['PatchDeploymentRolloutArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Patch deployments are configurations that individual patch jobs use to complete a patch.
        These configurations include instance filter, package repository settings, and a schedule.

        To get more information about PatchDeployment, see:

        * [API documentation](https://cloud.google.com/compute/docs/osconfig/rest)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/compute/docs/os-patch-management)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the patch deployment. Length of the description is limited to 1024 characters.
        :param pulumi.Input[str] duration: Duration of the patch. After the duration ends, the patch times out.
               A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
        :param pulumi.Input[pulumi.InputType['PatchDeploymentInstanceFilterArgs']] instance_filter: VM instances to patch.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['PatchDeploymentOneTimeScheduleArgs']] one_time_schedule: Schedule a one-time execution.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['PatchDeploymentPatchConfigArgs']] patch_config: Patch configuration that is applied.
               Structure is documented below.
        :param pulumi.Input[str] patch_deployment_id: A name for the patch deployment in the project. When creating a name the following rules apply:
               * Must contain only lowercase letters, numbers, and hyphens.
               * Must start with a letter.
               * Must be between 1-63 characters.
               * Must end with a number or a letter.
               * Must be unique within the project.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['PatchDeploymentRecurringScheduleArgs']] recurring_schedule: Schedule recurring executions.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['PatchDeploymentRolloutArgs']] rollout: Rollout strategy of the patch job.
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

            __props__['description'] = description
            __props__['duration'] = duration
            if instance_filter is None:
                raise TypeError("Missing required property 'instance_filter'")
            __props__['instance_filter'] = instance_filter
            __props__['one_time_schedule'] = one_time_schedule
            __props__['patch_config'] = patch_config
            if patch_deployment_id is None:
                raise TypeError("Missing required property 'patch_deployment_id'")
            __props__['patch_deployment_id'] = patch_deployment_id
            __props__['project'] = project
            __props__['recurring_schedule'] = recurring_schedule
            __props__['rollout'] = rollout
            __props__['create_time'] = None
            __props__['last_execute_time'] = None
            __props__['name'] = None
            __props__['update_time'] = None
        super(PatchDeployment, __self__).__init__(
            'gcp:osconfig/patchDeployment:PatchDeployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            duration: Optional[pulumi.Input[str]] = None,
            instance_filter: Optional[pulumi.Input[pulumi.InputType['PatchDeploymentInstanceFilterArgs']]] = None,
            last_execute_time: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            one_time_schedule: Optional[pulumi.Input[pulumi.InputType['PatchDeploymentOneTimeScheduleArgs']]] = None,
            patch_config: Optional[pulumi.Input[pulumi.InputType['PatchDeploymentPatchConfigArgs']]] = None,
            patch_deployment_id: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            recurring_schedule: Optional[pulumi.Input[pulumi.InputType['PatchDeploymentRecurringScheduleArgs']]] = None,
            rollout: Optional[pulumi.Input[pulumi.InputType['PatchDeploymentRolloutArgs']]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'PatchDeployment':
        """
        Get an existing PatchDeployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Time the patch deployment was created. Timestamp is in RFC3339 text format. A timestamp in RFC3339 UTC "Zulu" format,
               accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        :param pulumi.Input[str] description: Description of the patch deployment. Length of the description is limited to 1024 characters.
        :param pulumi.Input[str] duration: Duration of the patch. After the duration ends, the patch times out.
               A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
        :param pulumi.Input[pulumi.InputType['PatchDeploymentInstanceFilterArgs']] instance_filter: VM instances to patch.
               Structure is documented below.
        :param pulumi.Input[str] last_execute_time: -
               The time the last patch job ran successfully.
               A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        :param pulumi.Input[str] name: Unique name for the patch deployment resource in a project. The patch deployment name is in the form:
               projects/{project_id}/patchDeployments/{patchDeploymentId}.
        :param pulumi.Input[pulumi.InputType['PatchDeploymentOneTimeScheduleArgs']] one_time_schedule: Schedule a one-time execution.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['PatchDeploymentPatchConfigArgs']] patch_config: Patch configuration that is applied.
               Structure is documented below.
        :param pulumi.Input[str] patch_deployment_id: A name for the patch deployment in the project. When creating a name the following rules apply:
               * Must contain only lowercase letters, numbers, and hyphens.
               * Must start with a letter.
               * Must be between 1-63 characters.
               * Must end with a number or a letter.
               * Must be unique within the project.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['PatchDeploymentRecurringScheduleArgs']] recurring_schedule: Schedule recurring executions.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['PatchDeploymentRolloutArgs']] rollout: Rollout strategy of the patch job.
               Structure is documented below.
        :param pulumi.Input[str] update_time: Time the patch deployment was last updated. Timestamp is in RFC3339 text format. A timestamp in RFC3339 UTC "Zulu"
               format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["create_time"] = create_time
        __props__["description"] = description
        __props__["duration"] = duration
        __props__["instance_filter"] = instance_filter
        __props__["last_execute_time"] = last_execute_time
        __props__["name"] = name
        __props__["one_time_schedule"] = one_time_schedule
        __props__["patch_config"] = patch_config
        __props__["patch_deployment_id"] = patch_deployment_id
        __props__["project"] = project
        __props__["recurring_schedule"] = recurring_schedule
        __props__["rollout"] = rollout
        __props__["update_time"] = update_time
        return PatchDeployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time the patch deployment was created. Timestamp is in RFC3339 text format. A timestamp in RFC3339 UTC "Zulu" format,
        accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the patch deployment. Length of the description is limited to 1024 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Output[Optional[str]]:
        """
        Duration of the patch. After the duration ends, the patch times out.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(self) -> pulumi.Output['outputs.PatchDeploymentInstanceFilter']:
        """
        VM instances to patch.
        Structure is documented below.
        """
        return pulumi.get(self, "instance_filter")

    @property
    @pulumi.getter(name="lastExecuteTime")
    def last_execute_time(self) -> pulumi.Output[str]:
        """
        -
        The time the last patch job ran successfully.
        A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "last_execute_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique name for the patch deployment resource in a project. The patch deployment name is in the form:
        projects/{project_id}/patchDeployments/{patchDeploymentId}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oneTimeSchedule")
    def one_time_schedule(self) -> pulumi.Output[Optional['outputs.PatchDeploymentOneTimeSchedule']]:
        """
        Schedule a one-time execution.
        Structure is documented below.
        """
        return pulumi.get(self, "one_time_schedule")

    @property
    @pulumi.getter(name="patchConfig")
    def patch_config(self) -> pulumi.Output[Optional['outputs.PatchDeploymentPatchConfig']]:
        """
        Patch configuration that is applied.
        Structure is documented below.
        """
        return pulumi.get(self, "patch_config")

    @property
    @pulumi.getter(name="patchDeploymentId")
    def patch_deployment_id(self) -> pulumi.Output[str]:
        """
        A name for the patch deployment in the project. When creating a name the following rules apply:
        * Must contain only lowercase letters, numbers, and hyphens.
        * Must start with a letter.
        * Must be between 1-63 characters.
        * Must end with a number or a letter.
        * Must be unique within the project.
        """
        return pulumi.get(self, "patch_deployment_id")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="recurringSchedule")
    def recurring_schedule(self) -> pulumi.Output[Optional['outputs.PatchDeploymentRecurringSchedule']]:
        """
        Schedule recurring executions.
        Structure is documented below.
        """
        return pulumi.get(self, "recurring_schedule")

    @property
    @pulumi.getter
    def rollout(self) -> pulumi.Output[Optional['outputs.PatchDeploymentRollout']]:
        """
        Rollout strategy of the patch job.
        Structure is documented below.
        """
        return pulumi.get(self, "rollout")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Time the patch deployment was last updated. Timestamp is in RFC3339 text format. A timestamp in RFC3339 UTC "Zulu"
        format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "update_time")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

