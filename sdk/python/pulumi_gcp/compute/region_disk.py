# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class RegionDisk(pulumi.CustomResource):
    creation_timestamp: pulumi.Output[str]
    description: pulumi.Output[str]
    disk_encryption_key: pulumi.Output[dict]
    label_fingerprint: pulumi.Output[str]
    labels: pulumi.Output[dict]
    last_attach_timestamp: pulumi.Output[str]
    last_detach_timestamp: pulumi.Output[str]
    name: pulumi.Output[str]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    region: pulumi.Output[str]
    replica_zones: pulumi.Output[list]
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    size: pulumi.Output[float]
    snapshot: pulumi.Output[str]
    source_snapshot_encryption_key: pulumi.Output[dict]
    source_snapshot_id: pulumi.Output[str]
    type: pulumi.Output[str]
    users: pulumi.Output[list]
    def __init__(__self__, resource_name, opts=None, description=None, disk_encryption_key=None, labels=None, name=None, project=None, region=None, replica_zones=None, size=None, snapshot=None, source_snapshot_encryption_key=None, type=None, __name__=None, __opts__=None):
        """
        Persistent disks are durable storage devices that function similarly to
        the physical disks in a desktop or a server. Compute Engine manages the
        hardware behind these devices to ensure data redundancy and optimize
        performance for you. Persistent disks are available as either standard
        hard disk drives (HDD) or solid-state drives (SSD).
        
        Persistent disks are located independently from your virtual machine
        instances, so you can detach or move persistent disks to keep your data
        even after you delete your instances. Persistent disk performance scales
        automatically with size, so you can resize your existing persistent disks
        or add more persistent disks to an instance to meet your performance and
        storage space requirements.
        
        Add a persistent disk to your instance when you need reliable and
        affordable storage with consistent performance characteristics.
        
        
        To get more information about RegionDisk, see:
        
        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/regionDisks)
        * How-to Guides
            * [Adding or Resizing Regional Persistent Disks](https://cloud.google.com/compute/docs/disks/regional-persistent-disk)
        
        > **Warning:** All arguments including the disk encryption key will be stored in the raw
        state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
        
        <div class = "oics-button" style="float: right; margin: 0 0 -15px">
          <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=region_disk_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
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

        __props__['description'] = description

        __props__['disk_encryption_key'] = disk_encryption_key

        __props__['labels'] = labels

        __props__['name'] = name

        __props__['project'] = project

        __props__['region'] = region

        if replica_zones is None:
            raise TypeError('Missing required property replica_zones')
        __props__['replica_zones'] = replica_zones

        __props__['size'] = size

        __props__['snapshot'] = snapshot

        __props__['source_snapshot_encryption_key'] = source_snapshot_encryption_key

        __props__['type'] = type

        __props__['creation_timestamp'] = None
        __props__['label_fingerprint'] = None
        __props__['last_attach_timestamp'] = None
        __props__['last_detach_timestamp'] = None
        __props__['self_link'] = None
        __props__['source_snapshot_id'] = None
        __props__['users'] = None

        super(RegionDisk, __self__).__init__(
            'gcp:compute/regionDisk:RegionDisk',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

