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

__all__ = ['Table']


class Table(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 clusterings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dataset_id: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encryption_configuration: Optional[pulumi.Input[pulumi.InputType['TableEncryptionConfigurationArgs']]] = None,
                 expiration_time: Optional[pulumi.Input[int]] = None,
                 external_data_configuration: Optional[pulumi.Input[pulumi.InputType['TableExternalDataConfigurationArgs']]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 materialized_view: Optional[pulumi.Input[pulumi.InputType['TableMaterializedViewArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 range_partitioning: Optional[pulumi.Input[pulumi.InputType['TableRangePartitioningArgs']]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 table_id: Optional[pulumi.Input[str]] = None,
                 time_partitioning: Optional[pulumi.Input[pulumi.InputType['TableTimePartitioningArgs']]] = None,
                 view: Optional[pulumi.Input[pulumi.InputType['TableViewArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        BigQuery tables can be imported using the `project`, `dataset_id`, and `table_id`, e.g.

        ```sh
         $ pulumi import gcp:bigquery/table:Table default gcp-project/foo/bar
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] clusterings: Specifies column names to use for data clustering.
               Up to four top-level columns are allowed, and should be specified in
               descending priority order.
        :param pulumi.Input[str] dataset_id: The dataset ID to create the table in.
               Changing this forces a new resource to be created.
        :param pulumi.Input[bool] deletion_protection: Whether or not to allow Terraform to destroy the instance. Unless this field is set to false in Terraform state, a
               terraform destroy or terraform apply that would delete the instance will fail.
        :param pulumi.Input[str] description: The field description.
        :param pulumi.Input[pulumi.InputType['TableEncryptionConfigurationArgs']] encryption_configuration: Specifies how the table should be encrypted.
               If left blank, the table will be encrypted with a Google-managed key; that process
               is transparent to the user.  Structure is documented below.
        :param pulumi.Input[int] expiration_time: The time when this table expires, in
               milliseconds since the epoch. If not present, the table will persist
               indefinitely. Expired tables will be deleted and their storage
               reclaimed.
        :param pulumi.Input[pulumi.InputType['TableExternalDataConfigurationArgs']] external_data_configuration: Describes the data format,
               location, and other properties of a table stored outside of BigQuery.
               By defining these properties, the data source can then be queried as
               if it were a standard BigQuery table. Structure is documented below.
        :param pulumi.Input[str] friendly_name: A descriptive name for the table.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A mapping of labels to assign to the resource.
        :param pulumi.Input[pulumi.InputType['TableMaterializedViewArgs']] materialized_view: If specified, configures this table as a materialized view.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['TableRangePartitioningArgs']] range_partitioning: If specified, configures range-based
               partitioning for this table. Structure is documented below.
        :param pulumi.Input[str] schema: A JSON schema for the external table. Schema is required
               for CSV and JSON formats if autodetect is not on. Schema is disallowed
               for Google Cloud Bigtable, Cloud Datastore backups, Avro, ORC and Parquet formats.
               ~>**NOTE:** Because this field expects a JSON string, any changes to the
               string will create a diff, even if the JSON itself hasn't changed.
               Furthermore drift for this field cannot not be detected because BigQuery
               only uses this schema to compute the effective schema for the table, therefore
               any changes on the configured value will force the table to be recreated.
               This schema is effectively only applied when creating a table from an external
               datasource, after creation the computed schema will be stored in
               `google_bigquery_table.schema`
        :param pulumi.Input[str] table_id: A unique ID for the resource.
               Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['TableTimePartitioningArgs']] time_partitioning: If specified, configures time-based
               partitioning for this table. Structure is documented below.
        :param pulumi.Input[pulumi.InputType['TableViewArgs']] view: If specified, configures this table as a view.
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

            __props__['clusterings'] = clusterings
            if dataset_id is None and not opts.urn:
                raise TypeError("Missing required property 'dataset_id'")
            __props__['dataset_id'] = dataset_id
            __props__['deletion_protection'] = deletion_protection
            __props__['description'] = description
            __props__['encryption_configuration'] = encryption_configuration
            __props__['expiration_time'] = expiration_time
            __props__['external_data_configuration'] = external_data_configuration
            __props__['friendly_name'] = friendly_name
            __props__['labels'] = labels
            __props__['materialized_view'] = materialized_view
            __props__['project'] = project
            __props__['range_partitioning'] = range_partitioning
            __props__['schema'] = schema
            if table_id is None and not opts.urn:
                raise TypeError("Missing required property 'table_id'")
            __props__['table_id'] = table_id
            __props__['time_partitioning'] = time_partitioning
            __props__['view'] = view
            __props__['creation_time'] = None
            __props__['etag'] = None
            __props__['last_modified_time'] = None
            __props__['location'] = None
            __props__['num_bytes'] = None
            __props__['num_long_term_bytes'] = None
            __props__['num_rows'] = None
            __props__['self_link'] = None
            __props__['type'] = None
        super(Table, __self__).__init__(
            'gcp:bigquery/table:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            clusterings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            creation_time: Optional[pulumi.Input[int]] = None,
            dataset_id: Optional[pulumi.Input[str]] = None,
            deletion_protection: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            encryption_configuration: Optional[pulumi.Input[pulumi.InputType['TableEncryptionConfigurationArgs']]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            expiration_time: Optional[pulumi.Input[int]] = None,
            external_data_configuration: Optional[pulumi.Input[pulumi.InputType['TableExternalDataConfigurationArgs']]] = None,
            friendly_name: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            last_modified_time: Optional[pulumi.Input[int]] = None,
            location: Optional[pulumi.Input[str]] = None,
            materialized_view: Optional[pulumi.Input[pulumi.InputType['TableMaterializedViewArgs']]] = None,
            num_bytes: Optional[pulumi.Input[int]] = None,
            num_long_term_bytes: Optional[pulumi.Input[int]] = None,
            num_rows: Optional[pulumi.Input[int]] = None,
            project: Optional[pulumi.Input[str]] = None,
            range_partitioning: Optional[pulumi.Input[pulumi.InputType['TableRangePartitioningArgs']]] = None,
            schema: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            table_id: Optional[pulumi.Input[str]] = None,
            time_partitioning: Optional[pulumi.Input[pulumi.InputType['TableTimePartitioningArgs']]] = None,
            type: Optional[pulumi.Input[str]] = None,
            view: Optional[pulumi.Input[pulumi.InputType['TableViewArgs']]] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] clusterings: Specifies column names to use for data clustering.
               Up to four top-level columns are allowed, and should be specified in
               descending priority order.
        :param pulumi.Input[int] creation_time: The time when this table was created, in milliseconds since the epoch.
        :param pulumi.Input[str] dataset_id: The dataset ID to create the table in.
               Changing this forces a new resource to be created.
        :param pulumi.Input[bool] deletion_protection: Whether or not to allow Terraform to destroy the instance. Unless this field is set to false in Terraform state, a
               terraform destroy or terraform apply that would delete the instance will fail.
        :param pulumi.Input[str] description: The field description.
        :param pulumi.Input[pulumi.InputType['TableEncryptionConfigurationArgs']] encryption_configuration: Specifies how the table should be encrypted.
               If left blank, the table will be encrypted with a Google-managed key; that process
               is transparent to the user.  Structure is documented below.
        :param pulumi.Input[str] etag: A hash of the resource.
        :param pulumi.Input[int] expiration_time: The time when this table expires, in
               milliseconds since the epoch. If not present, the table will persist
               indefinitely. Expired tables will be deleted and their storage
               reclaimed.
        :param pulumi.Input[pulumi.InputType['TableExternalDataConfigurationArgs']] external_data_configuration: Describes the data format,
               location, and other properties of a table stored outside of BigQuery.
               By defining these properties, the data source can then be queried as
               if it were a standard BigQuery table. Structure is documented below.
        :param pulumi.Input[str] friendly_name: A descriptive name for the table.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A mapping of labels to assign to the resource.
        :param pulumi.Input[int] last_modified_time: The time when this table was last modified, in milliseconds since the epoch.
        :param pulumi.Input[str] location: The geographic location where the table resides. This value is inherited from the dataset.
        :param pulumi.Input[pulumi.InputType['TableMaterializedViewArgs']] materialized_view: If specified, configures this table as a materialized view.
               Structure is documented below.
        :param pulumi.Input[int] num_bytes: The size of this table in bytes, excluding any data in the streaming buffer.
        :param pulumi.Input[int] num_long_term_bytes: The number of bytes in the table that are considered "long-term storage".
        :param pulumi.Input[int] num_rows: The number of rows of data in this table, excluding any data in the streaming buffer.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['TableRangePartitioningArgs']] range_partitioning: If specified, configures range-based
               partitioning for this table. Structure is documented below.
        :param pulumi.Input[str] schema: A JSON schema for the external table. Schema is required
               for CSV and JSON formats if autodetect is not on. Schema is disallowed
               for Google Cloud Bigtable, Cloud Datastore backups, Avro, ORC and Parquet formats.
               ~>**NOTE:** Because this field expects a JSON string, any changes to the
               string will create a diff, even if the JSON itself hasn't changed.
               Furthermore drift for this field cannot not be detected because BigQuery
               only uses this schema to compute the effective schema for the table, therefore
               any changes on the configured value will force the table to be recreated.
               This schema is effectively only applied when creating a table from an external
               datasource, after creation the computed schema will be stored in
               `google_bigquery_table.schema`
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[str] table_id: A unique ID for the resource.
               Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['TableTimePartitioningArgs']] time_partitioning: If specified, configures time-based
               partitioning for this table. Structure is documented below.
        :param pulumi.Input[str] type: The supported types are DAY, HOUR, MONTH, and YEAR,
               which will generate one partition per day, hour, month, and year, respectively.
        :param pulumi.Input[pulumi.InputType['TableViewArgs']] view: If specified, configures this table as a view.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["clusterings"] = clusterings
        __props__["creation_time"] = creation_time
        __props__["dataset_id"] = dataset_id
        __props__["deletion_protection"] = deletion_protection
        __props__["description"] = description
        __props__["encryption_configuration"] = encryption_configuration
        __props__["etag"] = etag
        __props__["expiration_time"] = expiration_time
        __props__["external_data_configuration"] = external_data_configuration
        __props__["friendly_name"] = friendly_name
        __props__["labels"] = labels
        __props__["last_modified_time"] = last_modified_time
        __props__["location"] = location
        __props__["materialized_view"] = materialized_view
        __props__["num_bytes"] = num_bytes
        __props__["num_long_term_bytes"] = num_long_term_bytes
        __props__["num_rows"] = num_rows
        __props__["project"] = project
        __props__["range_partitioning"] = range_partitioning
        __props__["schema"] = schema
        __props__["self_link"] = self_link
        __props__["table_id"] = table_id
        __props__["time_partitioning"] = time_partitioning
        __props__["type"] = type
        __props__["view"] = view
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def clusterings(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies column names to use for data clustering.
        Up to four top-level columns are allowed, and should be specified in
        descending priority order.
        """
        return pulumi.get(self, "clusterings")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        """
        The time when this table was created, in milliseconds since the epoch.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Output[str]:
        """
        The dataset ID to create the table in.
        Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "dataset_id")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not to allow Terraform to destroy the instance. Unless this field is set to false in Terraform state, a
        terraform destroy or terraform apply that would delete the instance will fail.
        """
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The field description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Output[Optional['outputs.TableEncryptionConfiguration']]:
        """
        Specifies how the table should be encrypted.
        If left blank, the table will be encrypted with a Google-managed key; that process
        is transparent to the user.  Structure is documented below.
        """
        return pulumi.get(self, "encryption_configuration")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A hash of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[int]:
        """
        The time when this table expires, in
        milliseconds since the epoch. If not present, the table will persist
        indefinitely. Expired tables will be deleted and their storage
        reclaimed.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter(name="externalDataConfiguration")
    def external_data_configuration(self) -> pulumi.Output[Optional['outputs.TableExternalDataConfiguration']]:
        """
        Describes the data format,
        location, and other properties of a table stored outside of BigQuery.
        By defining these properties, the data source can then be queried as
        if it were a standard BigQuery table. Structure is documented below.
        """
        return pulumi.get(self, "external_data_configuration")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        A descriptive name for the table.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of labels to assign to the resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[int]:
        """
        The time when this table was last modified, in milliseconds since the epoch.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geographic location where the table resides. This value is inherited from the dataset.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="materializedView")
    def materialized_view(self) -> pulumi.Output[Optional['outputs.TableMaterializedView']]:
        """
        If specified, configures this table as a materialized view.
        Structure is documented below.
        """
        return pulumi.get(self, "materialized_view")

    @property
    @pulumi.getter(name="numBytes")
    def num_bytes(self) -> pulumi.Output[int]:
        """
        The size of this table in bytes, excluding any data in the streaming buffer.
        """
        return pulumi.get(self, "num_bytes")

    @property
    @pulumi.getter(name="numLongTermBytes")
    def num_long_term_bytes(self) -> pulumi.Output[int]:
        """
        The number of bytes in the table that are considered "long-term storage".
        """
        return pulumi.get(self, "num_long_term_bytes")

    @property
    @pulumi.getter(name="numRows")
    def num_rows(self) -> pulumi.Output[int]:
        """
        The number of rows of data in this table, excluding any data in the streaming buffer.
        """
        return pulumi.get(self, "num_rows")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="rangePartitioning")
    def range_partitioning(self) -> pulumi.Output[Optional['outputs.TableRangePartitioning']]:
        """
        If specified, configures range-based
        partitioning for this table. Structure is documented below.
        """
        return pulumi.get(self, "range_partitioning")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[str]:
        """
        A JSON schema for the external table. Schema is required
        for CSV and JSON formats if autodetect is not on. Schema is disallowed
        for Google Cloud Bigtable, Cloud Datastore backups, Avro, ORC and Parquet formats.
        ~>**NOTE:** Because this field expects a JSON string, any changes to the
        string will create a diff, even if the JSON itself hasn't changed.
        Furthermore drift for this field cannot not be detected because BigQuery
        only uses this schema to compute the effective schema for the table, therefore
        any changes on the configured value will force the table to be recreated.
        This schema is effectively only applied when creating a table from an external
        datasource, after creation the computed schema will be stored in
        `google_bigquery_table.schema`
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Output[str]:
        """
        A unique ID for the resource.
        Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "table_id")

    @property
    @pulumi.getter(name="timePartitioning")
    def time_partitioning(self) -> pulumi.Output[Optional['outputs.TableTimePartitioning']]:
        """
        If specified, configures time-based
        partitioning for this table. Structure is documented below.
        """
        return pulumi.get(self, "time_partitioning")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The supported types are DAY, HOUR, MONTH, and YEAR,
        which will generate one partition per day, hour, month, and year, respectively.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def view(self) -> pulumi.Output[Optional['outputs.TableView']]:
        """
        If specified, configures this table as a view.
        Structure is documented below.
        """
        return pulumi.get(self, "view")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

