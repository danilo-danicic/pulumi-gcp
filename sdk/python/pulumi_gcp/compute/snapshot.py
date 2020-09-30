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

__all__ = ['Snapshot']


class Snapshot(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 snapshot_encryption_key: Optional[pulumi.Input[pulumi.InputType['SnapshotSnapshotEncryptionKeyArgs']]] = None,
                 source_disk: Optional[pulumi.Input[str]] = None,
                 source_disk_encryption_key: Optional[pulumi.Input[pulumi.InputType['SnapshotSourceDiskEncryptionKeyArgs']]] = None,
                 storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Represents a Persistent Disk Snapshot resource.

        Use snapshots to back up data from your persistent disks. Snapshots are
        different from public images and custom images, which are used primarily
        to create instances or configure instance templates. Snapshots are useful
        for periodic backup of the data on your persistent disks. You can create
        snapshots from persistent disks even while they are attached to running
        instances.

        Snapshots are incremental, so you can create regular snapshots on a
        persistent disk faster and at a much lower cost than if you regularly
        created a full image of the disk.

        To get more information about Snapshot, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/snapshots)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/compute/docs/disks/create-snapshots)

        > **Warning:** All arguments including `snapshot_encryption_key.raw_key` and `source_disk_encryption_key.raw_key` will be stored in the raw
        state as plain-text. [Read more about secrets in state](https://www.pulumi.com/docs/intro/concepts/programming-model/#secrets).

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels to apply to this Snapshot.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['SnapshotSnapshotEncryptionKeyArgs']] snapshot_encryption_key: The customer-supplied encryption key of the snapshot. Required if the
               source snapshot is protected by a customer-supplied encryption key.
               Structure is documented below.
        :param pulumi.Input[str] source_disk: A reference to the disk used to create this snapshot.
        :param pulumi.Input[pulumi.InputType['SnapshotSourceDiskEncryptionKeyArgs']] source_disk_encryption_key: The customer-supplied encryption key of the source snapshot. Required
               if the source snapshot is protected by a customer-supplied encryption
               key.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_locations: Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
        :param pulumi.Input[str] zone: A reference to the zone where the disk is hosted.
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
            __props__['labels'] = labels
            __props__['name'] = name
            __props__['project'] = project
            __props__['snapshot_encryption_key'] = snapshot_encryption_key
            if source_disk is None:
                raise TypeError("Missing required property 'source_disk'")
            __props__['source_disk'] = source_disk
            __props__['source_disk_encryption_key'] = source_disk_encryption_key
            __props__['storage_locations'] = storage_locations
            __props__['zone'] = zone
            __props__['creation_timestamp'] = None
            __props__['disk_size_gb'] = None
            __props__['label_fingerprint'] = None
            __props__['licenses'] = None
            __props__['self_link'] = None
            __props__['snapshot_id'] = None
            __props__['source_disk_link'] = None
            __props__['storage_bytes'] = None
        super(Snapshot, __self__).__init__(
            'gcp:compute/snapshot:Snapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            creation_timestamp: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            disk_size_gb: Optional[pulumi.Input[int]] = None,
            label_fingerprint: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            licenses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            snapshot_encryption_key: Optional[pulumi.Input[pulumi.InputType['SnapshotSnapshotEncryptionKeyArgs']]] = None,
            snapshot_id: Optional[pulumi.Input[int]] = None,
            source_disk: Optional[pulumi.Input[str]] = None,
            source_disk_encryption_key: Optional[pulumi.Input[pulumi.InputType['SnapshotSourceDiskEncryptionKeyArgs']]] = None,
            source_disk_link: Optional[pulumi.Input[str]] = None,
            storage_bytes: Optional[pulumi.Input[int]] = None,
            storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'Snapshot':
        """
        Get an existing Snapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[int] disk_size_gb: Size of the snapshot, specified in GB.
        :param pulumi.Input[str] label_fingerprint: The fingerprint used for optimistic locking of this resource. Used internally during updates.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels to apply to this Snapshot.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] licenses: A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses
               attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied
               encryption key.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[pulumi.InputType['SnapshotSnapshotEncryptionKeyArgs']] snapshot_encryption_key: The customer-supplied encryption key of the snapshot. Required if the
               source snapshot is protected by a customer-supplied encryption key.
               Structure is documented below.
        :param pulumi.Input[int] snapshot_id: The unique identifier for the resource.
        :param pulumi.Input[str] source_disk: A reference to the disk used to create this snapshot.
        :param pulumi.Input[pulumi.InputType['SnapshotSourceDiskEncryptionKeyArgs']] source_disk_encryption_key: The customer-supplied encryption key of the source snapshot. Required
               if the source snapshot is protected by a customer-supplied encryption
               key.
               Structure is documented below.
        :param pulumi.Input[int] storage_bytes: A size of the storage used by the snapshot. As snapshots share storage, this number is expected to change with snapshot
               creation/deletion.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_locations: Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
        :param pulumi.Input[str] zone: A reference to the zone where the disk is hosted.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["creation_timestamp"] = creation_timestamp
        __props__["description"] = description
        __props__["disk_size_gb"] = disk_size_gb
        __props__["label_fingerprint"] = label_fingerprint
        __props__["labels"] = labels
        __props__["licenses"] = licenses
        __props__["name"] = name
        __props__["project"] = project
        __props__["self_link"] = self_link
        __props__["snapshot_encryption_key"] = snapshot_encryption_key
        __props__["snapshot_id"] = snapshot_id
        __props__["source_disk"] = source_disk
        __props__["source_disk_encryption_key"] = source_disk_encryption_key
        __props__["source_disk_link"] = source_disk_link
        __props__["storage_bytes"] = storage_bytes
        __props__["storage_locations"] = storage_locations
        __props__["zone"] = zone
        return Snapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> pulumi.Output[int]:
        """
        Size of the snapshot, specified in GB.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[str]:
        """
        The fingerprint used for optimistic locking of this resource. Used internally during updates.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Labels to apply to this Snapshot.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def licenses(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of public visible licenses that apply to this snapshot. This can be because the original image had licenses
        attached (such as a Windows image). snapshotEncryptionKey nested object Encrypts the snapshot using a customer-supplied
        encryption key.
        """
        return pulumi.get(self, "licenses")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource; provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression `a-z?` which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.
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
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="snapshotEncryptionKey")
    def snapshot_encryption_key(self) -> pulumi.Output[Optional['outputs.SnapshotSnapshotEncryptionKey']]:
        """
        The customer-supplied encryption key of the snapshot. Required if the
        source snapshot is protected by a customer-supplied encryption key.
        Structure is documented below.
        """
        return pulumi.get(self, "snapshot_encryption_key")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[int]:
        """
        The unique identifier for the resource.
        """
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> pulumi.Output[str]:
        """
        A reference to the disk used to create this snapshot.
        """
        return pulumi.get(self, "source_disk")

    @property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(self) -> pulumi.Output[Optional['outputs.SnapshotSourceDiskEncryptionKey']]:
        """
        The customer-supplied encryption key of the source snapshot. Required
        if the source snapshot is protected by a customer-supplied encryption
        key.
        Structure is documented below.
        """
        return pulumi.get(self, "source_disk_encryption_key")

    @property
    @pulumi.getter(name="sourceDiskLink")
    def source_disk_link(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_disk_link")

    @property
    @pulumi.getter(name="storageBytes")
    def storage_bytes(self) -> pulumi.Output[int]:
        """
        A size of the storage used by the snapshot. As snapshots share storage, this number is expected to change with snapshot
        creation/deletion.
        """
        return pulumi.get(self, "storage_bytes")

    @property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> pulumi.Output[Sequence[str]]:
        """
        Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
        """
        return pulumi.get(self, "storage_locations")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        A reference to the zone where the disk is hosted.
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

