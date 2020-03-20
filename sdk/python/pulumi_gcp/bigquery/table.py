# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Table(pulumi.CustomResource):
    clusterings: pulumi.Output[list]
    """
    Specifies column names to use for data clustering.
    Up to four top-level columns are allowed, and should be specified in
    descending priority order.
    """
    creation_time: pulumi.Output[float]
    """
    The time when this table was created, in milliseconds since the epoch.
    """
    dataset_id: pulumi.Output[str]
    """
    The dataset ID to create the table in.
    Changing this forces a new resource to be created.
    """
    description: pulumi.Output[str]
    """
    The field description.
    """
    encryption_configuration: pulumi.Output[dict]
    """
    Specifies how the table should be encrypted.
    If left blank, the table will be encrypted with a Google-managed key; that process
    is transparent to the user.  Structure is documented below.

      * `kms_key_name` (`str`)
    """
    etag: pulumi.Output[str]
    """
    A hash of the resource.
    """
    expiration_time: pulumi.Output[float]
    """
    The time when this table expires, in
    milliseconds since the epoch. If not present, the table will persist
    indefinitely. Expired tables will be deleted and their storage
    reclaimed.
    """
    external_data_configuration: pulumi.Output[dict]
    """
    Describes the data format,
    location, and other properties of a table stored outside of BigQuery.
    By defining these properties, the data source can then be queried as
    if it were a standard BigQuery table. Structure is documented below.

      * `autodetect` (`bool`)
      * `compression` (`str`)
      * `csvOptions` (`dict`)
        * `allowJaggedRows` (`bool`)
        * `allowQuotedNewlines` (`bool`)
        * `encoding` (`str`)
        * `fieldDelimiter` (`str`)
        * `quote` (`str`)
        * `skipLeadingRows` (`float`)

      * `googleSheetsOptions` (`dict`)
        * `range` (`str`)
        * `skipLeadingRows` (`float`)

      * `ignoreUnknownValues` (`bool`)
      * `maxBadRecords` (`float`)
      * `sourceFormat` (`str`)
      * `sourceUris` (`list`)
    """
    friendly_name: pulumi.Output[str]
    """
    A descriptive name for the table.
    """
    labels: pulumi.Output[dict]
    """
    A mapping of labels to assign to the resource.
    """
    last_modified_time: pulumi.Output[float]
    """
    The time when this table was last modified, in milliseconds since the epoch.
    """
    location: pulumi.Output[str]
    """
    The geographic location where the table resides. This value is inherited from the dataset.
    """
    num_bytes: pulumi.Output[float]
    """
    The size of this table in bytes, excluding any data in the streaming buffer.
    """
    num_long_term_bytes: pulumi.Output[float]
    """
    The number of bytes in the table that are considered "long-term storage".
    """
    num_rows: pulumi.Output[float]
    """
    The number of rows of data in this table, excluding any data in the streaming buffer.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs. If it
    is not provided, the provider project is used.
    """
    range_partitioning: pulumi.Output[dict]
    """
    If specified, configures range-based
    partitioning for this table. Structure is documented below.

      * `field` (`str`)
      * `range` (`dict`)
        * `end` (`float`)
        * `interval` (`float`)
        * `start` (`float`)
    """
    schema: pulumi.Output[str]
    """
    A JSON schema for the table. Schema is required
    for CSV and JSON formats and is disallowed for Google Cloud
    Bigtable, Cloud Datastore backups, and Avro formats when using
    external tables. For more information see the
    [BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
    ~>**NOTE**: Because this field expects a JSON string, any changes to the
    string will create a diff, even if the JSON itself hasn't changed.
    If the API returns a different value for the same schema, e.g. it
    switched the order of values or replaced `STRUCT` field type with `RECORD`
    field type, we currently cannot suppress the recurring diff this causes.
    As a workaround, we recommend using the schema as returned by the API.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    table_id: pulumi.Output[str]
    """
    A unique ID for the resource.
    Changing this forces a new resource to be created.
    """
    time_partitioning: pulumi.Output[dict]
    """
    If specified, configures time-based
    partitioning for this table. Structure is documented below.

      * `expirationMs` (`float`)
      * `field` (`str`)
      * `requirePartitionFilter` (`bool`)
      * `type` (`str`) - Describes the table type.
    """
    type: pulumi.Output[str]
    """
    Describes the table type.
    """
    view: pulumi.Output[dict]
    """
    If specified, configures this table as a view.
    Structure is documented below.

      * `query` (`str`)
      * `useLegacySql` (`bool`)
    """
    def __init__(__self__, resource_name, opts=None, clusterings=None, dataset_id=None, description=None, encryption_configuration=None, expiration_time=None, external_data_configuration=None, friendly_name=None, labels=None, project=None, range_partitioning=None, schema=None, table_id=None, time_partitioning=None, view=None, __props__=None, __name__=None, __opts__=None):
        """
        Creates a table resource in a dataset for Google BigQuery. For more information see
        [the official documentation](https://cloud.google.com/bigquery/docs/) and
        [API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables).

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_table.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] clusterings: Specifies column names to use for data clustering.
               Up to four top-level columns are allowed, and should be specified in
               descending priority order.
        :param pulumi.Input[str] dataset_id: The dataset ID to create the table in.
               Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The field description.
        :param pulumi.Input[dict] encryption_configuration: Specifies how the table should be encrypted.
               If left blank, the table will be encrypted with a Google-managed key; that process
               is transparent to the user.  Structure is documented below.
        :param pulumi.Input[float] expiration_time: The time when this table expires, in
               milliseconds since the epoch. If not present, the table will persist
               indefinitely. Expired tables will be deleted and their storage
               reclaimed.
        :param pulumi.Input[dict] external_data_configuration: Describes the data format,
               location, and other properties of a table stored outside of BigQuery.
               By defining these properties, the data source can then be queried as
               if it were a standard BigQuery table. Structure is documented below.
        :param pulumi.Input[str] friendly_name: A descriptive name for the table.
        :param pulumi.Input[dict] labels: A mapping of labels to assign to the resource.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[dict] range_partitioning: If specified, configures range-based
               partitioning for this table. Structure is documented below.
        :param pulumi.Input[str] schema: A JSON schema for the table. Schema is required
               for CSV and JSON formats and is disallowed for Google Cloud
               Bigtable, Cloud Datastore backups, and Avro formats when using
               external tables. For more information see the
               [BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
               ~>**NOTE**: Because this field expects a JSON string, any changes to the
               string will create a diff, even if the JSON itself hasn't changed.
               If the API returns a different value for the same schema, e.g. it
               switched the order of values or replaced `STRUCT` field type with `RECORD`
               field type, we currently cannot suppress the recurring diff this causes.
               As a workaround, we recommend using the schema as returned by the API.
        :param pulumi.Input[str] table_id: A unique ID for the resource.
               Changing this forces a new resource to be created.
        :param pulumi.Input[dict] time_partitioning: If specified, configures time-based
               partitioning for this table. Structure is documented below.
        :param pulumi.Input[dict] view: If specified, configures this table as a view.
               Structure is documented below.

        The **encryption_configuration** object supports the following:

          * `kms_key_name` (`pulumi.Input[str]`)

        The **external_data_configuration** object supports the following:

          * `autodetect` (`pulumi.Input[bool]`)
          * `compression` (`pulumi.Input[str]`)
          * `csvOptions` (`pulumi.Input[dict]`)
            * `allowJaggedRows` (`pulumi.Input[bool]`)
            * `allowQuotedNewlines` (`pulumi.Input[bool]`)
            * `encoding` (`pulumi.Input[str]`)
            * `fieldDelimiter` (`pulumi.Input[str]`)
            * `quote` (`pulumi.Input[str]`)
            * `skipLeadingRows` (`pulumi.Input[float]`)

          * `googleSheetsOptions` (`pulumi.Input[dict]`)
            * `range` (`pulumi.Input[str]`)
            * `skipLeadingRows` (`pulumi.Input[float]`)

          * `ignoreUnknownValues` (`pulumi.Input[bool]`)
          * `maxBadRecords` (`pulumi.Input[float]`)
          * `sourceFormat` (`pulumi.Input[str]`)
          * `sourceUris` (`pulumi.Input[list]`)

        The **range_partitioning** object supports the following:

          * `field` (`pulumi.Input[str]`)
          * `range` (`pulumi.Input[dict]`)
            * `end` (`pulumi.Input[float]`)
            * `interval` (`pulumi.Input[float]`)
            * `start` (`pulumi.Input[float]`)

        The **time_partitioning** object supports the following:

          * `expirationMs` (`pulumi.Input[float]`)
          * `field` (`pulumi.Input[str]`)
          * `requirePartitionFilter` (`pulumi.Input[bool]`)
          * `type` (`pulumi.Input[str]`) - Describes the table type.

        The **view** object supports the following:

          * `query` (`pulumi.Input[str]`)
          * `useLegacySql` (`pulumi.Input[bool]`)
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

            __props__['clusterings'] = clusterings
            if dataset_id is None:
                raise TypeError("Missing required property 'dataset_id'")
            __props__['dataset_id'] = dataset_id
            __props__['description'] = description
            __props__['encryption_configuration'] = encryption_configuration
            __props__['expiration_time'] = expiration_time
            __props__['external_data_configuration'] = external_data_configuration
            __props__['friendly_name'] = friendly_name
            __props__['labels'] = labels
            __props__['project'] = project
            __props__['range_partitioning'] = range_partitioning
            __props__['schema'] = schema
            if table_id is None:
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
    def get(resource_name, id, opts=None, clusterings=None, creation_time=None, dataset_id=None, description=None, encryption_configuration=None, etag=None, expiration_time=None, external_data_configuration=None, friendly_name=None, labels=None, last_modified_time=None, location=None, num_bytes=None, num_long_term_bytes=None, num_rows=None, project=None, range_partitioning=None, schema=None, self_link=None, table_id=None, time_partitioning=None, type=None, view=None):
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] clusterings: Specifies column names to use for data clustering.
               Up to four top-level columns are allowed, and should be specified in
               descending priority order.
        :param pulumi.Input[float] creation_time: The time when this table was created, in milliseconds since the epoch.
        :param pulumi.Input[str] dataset_id: The dataset ID to create the table in.
               Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The field description.
        :param pulumi.Input[dict] encryption_configuration: Specifies how the table should be encrypted.
               If left blank, the table will be encrypted with a Google-managed key; that process
               is transparent to the user.  Structure is documented below.
        :param pulumi.Input[str] etag: A hash of the resource.
        :param pulumi.Input[float] expiration_time: The time when this table expires, in
               milliseconds since the epoch. If not present, the table will persist
               indefinitely. Expired tables will be deleted and their storage
               reclaimed.
        :param pulumi.Input[dict] external_data_configuration: Describes the data format,
               location, and other properties of a table stored outside of BigQuery.
               By defining these properties, the data source can then be queried as
               if it were a standard BigQuery table. Structure is documented below.
        :param pulumi.Input[str] friendly_name: A descriptive name for the table.
        :param pulumi.Input[dict] labels: A mapping of labels to assign to the resource.
        :param pulumi.Input[float] last_modified_time: The time when this table was last modified, in milliseconds since the epoch.
        :param pulumi.Input[str] location: The geographic location where the table resides. This value is inherited from the dataset.
        :param pulumi.Input[float] num_bytes: The size of this table in bytes, excluding any data in the streaming buffer.
        :param pulumi.Input[float] num_long_term_bytes: The number of bytes in the table that are considered "long-term storage".
        :param pulumi.Input[float] num_rows: The number of rows of data in this table, excluding any data in the streaming buffer.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[dict] range_partitioning: If specified, configures range-based
               partitioning for this table. Structure is documented below.
        :param pulumi.Input[str] schema: A JSON schema for the table. Schema is required
               for CSV and JSON formats and is disallowed for Google Cloud
               Bigtable, Cloud Datastore backups, and Avro formats when using
               external tables. For more information see the
               [BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
               ~>**NOTE**: Because this field expects a JSON string, any changes to the
               string will create a diff, even if the JSON itself hasn't changed.
               If the API returns a different value for the same schema, e.g. it
               switched the order of values or replaced `STRUCT` field type with `RECORD`
               field type, we currently cannot suppress the recurring diff this causes.
               As a workaround, we recommend using the schema as returned by the API.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[str] table_id: A unique ID for the resource.
               Changing this forces a new resource to be created.
        :param pulumi.Input[dict] time_partitioning: If specified, configures time-based
               partitioning for this table. Structure is documented below.
        :param pulumi.Input[str] type: Describes the table type.
        :param pulumi.Input[dict] view: If specified, configures this table as a view.
               Structure is documented below.

        The **encryption_configuration** object supports the following:

          * `kms_key_name` (`pulumi.Input[str]`)

        The **external_data_configuration** object supports the following:

          * `autodetect` (`pulumi.Input[bool]`)
          * `compression` (`pulumi.Input[str]`)
          * `csvOptions` (`pulumi.Input[dict]`)
            * `allowJaggedRows` (`pulumi.Input[bool]`)
            * `allowQuotedNewlines` (`pulumi.Input[bool]`)
            * `encoding` (`pulumi.Input[str]`)
            * `fieldDelimiter` (`pulumi.Input[str]`)
            * `quote` (`pulumi.Input[str]`)
            * `skipLeadingRows` (`pulumi.Input[float]`)

          * `googleSheetsOptions` (`pulumi.Input[dict]`)
            * `range` (`pulumi.Input[str]`)
            * `skipLeadingRows` (`pulumi.Input[float]`)

          * `ignoreUnknownValues` (`pulumi.Input[bool]`)
          * `maxBadRecords` (`pulumi.Input[float]`)
          * `sourceFormat` (`pulumi.Input[str]`)
          * `sourceUris` (`pulumi.Input[list]`)

        The **range_partitioning** object supports the following:

          * `field` (`pulumi.Input[str]`)
          * `range` (`pulumi.Input[dict]`)
            * `end` (`pulumi.Input[float]`)
            * `interval` (`pulumi.Input[float]`)
            * `start` (`pulumi.Input[float]`)

        The **time_partitioning** object supports the following:

          * `expirationMs` (`pulumi.Input[float]`)
          * `field` (`pulumi.Input[str]`)
          * `requirePartitionFilter` (`pulumi.Input[bool]`)
          * `type` (`pulumi.Input[str]`) - Describes the table type.

        The **view** object supports the following:

          * `query` (`pulumi.Input[str]`)
          * `useLegacySql` (`pulumi.Input[bool]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["clusterings"] = clusterings
        __props__["creation_time"] = creation_time
        __props__["dataset_id"] = dataset_id
        __props__["description"] = description
        __props__["encryption_configuration"] = encryption_configuration
        __props__["etag"] = etag
        __props__["expiration_time"] = expiration_time
        __props__["external_data_configuration"] = external_data_configuration
        __props__["friendly_name"] = friendly_name
        __props__["labels"] = labels
        __props__["last_modified_time"] = last_modified_time
        __props__["location"] = location
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
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

