# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Database']


class Database(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ddls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A Cloud Spanner Database which is hosted on a Spanner instance.

        To get more information about Database, see:

        * [API documentation](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/spanner/)

        > **Warning:** It is strongly recommended to set `lifecycle { prevent_destroy = true }` on databases in order to prevent accidental data loss.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ddls: An optional list of DDL statements to run inside the newly created
               database. Statements can create tables, indexes, etc. These statements
               execute atomically with the creation of the database: if there is an
               error in any statement, the database is not created.
        :param pulumi.Input[str] instance: The instance to create the database on.
        :param pulumi.Input[str] name: A unique identifier for the database, which cannot be changed after
               the instance is created. Values are of the form [a-z][-a-z0-9]*[a-z0-9].
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
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

            __props__['ddls'] = ddls
            if instance is None:
                raise TypeError("Missing required property 'instance'")
            __props__['instance'] = instance
            __props__['name'] = name
            __props__['project'] = project
            __props__['state'] = None
        super(Database, __self__).__init__(
            'gcp:spanner/database:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ddls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            instance: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'Database':
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ddls: An optional list of DDL statements to run inside the newly created
               database. Statements can create tables, indexes, etc. These statements
               execute atomically with the creation of the database: if there is an
               error in any statement, the database is not created.
        :param pulumi.Input[str] instance: The instance to create the database on.
        :param pulumi.Input[str] name: A unique identifier for the database, which cannot be changed after
               the instance is created. Values are of the form [a-z][-a-z0-9]*[a-z0-9].
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] state: An explanation of the status of the database.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["ddls"] = ddls
        __props__["instance"] = instance
        __props__["name"] = name
        __props__["project"] = project
        __props__["state"] = state
        return Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def ddls(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        An optional list of DDL statements to run inside the newly created
        database. Statements can create tables, indexes, etc. These statements
        execute atomically with the creation of the database: if there is an
        error in any statement, the database is not created.
        """
        return pulumi.get(self, "ddls")

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Output[str]:
        """
        The instance to create the database on.
        """
        return pulumi.get(self, "instance")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique identifier for the database, which cannot be changed after
        the instance is created. Values are of the form [a-z][-a-z0-9]*[a-z0-9].
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
    def state(self) -> pulumi.Output[str]:
        """
        An explanation of the status of the database.
        """
        return pulumi.get(self, "state")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

