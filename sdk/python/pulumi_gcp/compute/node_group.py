# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class NodeGroup(pulumi.CustomResource):
    autoscaling_policy: pulumi.Output[dict]
    """
    -
    If you use sole-tenant nodes for your workloads, you can use the node
    group autoscaler to automatically manage the sizes of your node groups.  Structure is documented below.

      * `maxNodes` (`float`) - Maximum size of the node group. Set to a value less than or equal
        to 100 and greater than or equal to min-nodes.
      * `minNodes` (`float`) - Minimum size of the node group. Must be less
        than or equal to max-nodes. The default value is 0.
      * `mode` (`str`) - The autoscaling mode. Set to one of the following:
        - OFF: Disables the autoscaler.
        - ON: Enables scaling in and scaling out.
        - ONLY_SCALE_OUT: Enables only scaling out.
        You must use this mode if your node groups are configured to
        restart their hosted VMs on minimal servers.
    """
    creation_timestamp: pulumi.Output[str]
    """
    Creation timestamp in RFC3339 text format.
    """
    description: pulumi.Output[str]
    """
    An optional textual description of the resource.
    """
    name: pulumi.Output[str]
    """
    Name of the resource.
    """
    node_template: pulumi.Output[str]
    """
    The URL of the node template to which this node group belongs.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    size: pulumi.Output[float]
    """
    The total number of nodes in the node group.
    """
    zone: pulumi.Output[str]
    """
    Zone where this node group is located
    """
    def __init__(__self__, resource_name, opts=None, autoscaling_policy=None, description=None, name=None, node_template=None, project=None, size=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        Represents a NodeGroup resource to manage a group of sole-tenant nodes.


        To get more information about NodeGroup, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/nodeGroups)
        * How-to Guides
            * [Sole-Tenant Nodes](https://cloud.google.com/compute/docs/nodes/)

        > **Warning:** Due to limitations of the API, this provider cannot update the
        number of nodes in a node group and changes to node group size either
        through provider config or through external changes will cause
        the provider to delete and recreate the node group.

        ## Example Usage

        ### Node Group Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        central1a = gcp.compute.get_node_types(zone="us-central1-a")
        soletenant_tmpl = gcp.compute.NodeTemplate("soletenant-tmpl",
            region="us-central1",
            node_type=central1a.names[0])
        nodes = gcp.compute.NodeGroup("nodes",
            zone="us-central1-a",
            description="example google_compute_node_group for the Google Provider",
            size=1,
            node_template=soletenant_tmpl.id)
        ```

        ### Node Group Autoscaling Policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        central1a = gcp.compute.get_node_types(zone="us-central1-a")
        soletenant_tmpl = gcp.compute.NodeTemplate("soletenant-tmpl",
            region="us-central1",
            node_type=central1a.names[0])
        nodes = gcp.compute.NodeGroup("nodes",
            zone="us-central1-a",
            description="example google_compute_node_group for the Google Provider",
            size=1,
            node_template=soletenant_tmpl.id,
            autoscaling_policy={
                "mode": "ON",
                "minNodes": 1,
                "maxNodes": 10,
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] autoscaling_policy: -
               If you use sole-tenant nodes for your workloads, you can use the node
               group autoscaler to automatically manage the sizes of your node groups.  Structure is documented below.
        :param pulumi.Input[str] description: An optional textual description of the resource.
        :param pulumi.Input[str] name: Name of the resource.
        :param pulumi.Input[str] node_template: The URL of the node template to which this node group belongs.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[float] size: The total number of nodes in the node group.
        :param pulumi.Input[str] zone: Zone where this node group is located

        The **autoscaling_policy** object supports the following:

          * `maxNodes` (`pulumi.Input[float]`) - Maximum size of the node group. Set to a value less than or equal
            to 100 and greater than or equal to min-nodes.
          * `minNodes` (`pulumi.Input[float]`) - Minimum size of the node group. Must be less
            than or equal to max-nodes. The default value is 0.
          * `mode` (`pulumi.Input[str]`) - The autoscaling mode. Set to one of the following:
            - OFF: Disables the autoscaler.
            - ON: Enables scaling in and scaling out.
            - ONLY_SCALE_OUT: Enables only scaling out.
            You must use this mode if your node groups are configured to
            restart their hosted VMs on minimal servers.
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

            __props__['autoscaling_policy'] = autoscaling_policy
            __props__['description'] = description
            __props__['name'] = name
            if node_template is None:
                raise TypeError("Missing required property 'node_template'")
            __props__['node_template'] = node_template
            __props__['project'] = project
            if size is None:
                raise TypeError("Missing required property 'size'")
            __props__['size'] = size
            __props__['zone'] = zone
            __props__['creation_timestamp'] = None
            __props__['self_link'] = None
        super(NodeGroup, __self__).__init__(
            'gcp:compute/nodeGroup:NodeGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, autoscaling_policy=None, creation_timestamp=None, description=None, name=None, node_template=None, project=None, self_link=None, size=None, zone=None):
        """
        Get an existing NodeGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] autoscaling_policy: -
               If you use sole-tenant nodes for your workloads, you can use the node
               group autoscaler to automatically manage the sizes of your node groups.  Structure is documented below.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional textual description of the resource.
        :param pulumi.Input[str] name: Name of the resource.
        :param pulumi.Input[str] node_template: The URL of the node template to which this node group belongs.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[float] size: The total number of nodes in the node group.
        :param pulumi.Input[str] zone: Zone where this node group is located

        The **autoscaling_policy** object supports the following:

          * `maxNodes` (`pulumi.Input[float]`) - Maximum size of the node group. Set to a value less than or equal
            to 100 and greater than or equal to min-nodes.
          * `minNodes` (`pulumi.Input[float]`) - Minimum size of the node group. Must be less
            than or equal to max-nodes. The default value is 0.
          * `mode` (`pulumi.Input[str]`) - The autoscaling mode. Set to one of the following:
            - OFF: Disables the autoscaler.
            - ON: Enables scaling in and scaling out.
            - ONLY_SCALE_OUT: Enables only scaling out.
            You must use this mode if your node groups are configured to
            restart their hosted VMs on minimal servers.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["autoscaling_policy"] = autoscaling_policy
        __props__["creation_timestamp"] = creation_timestamp
        __props__["description"] = description
        __props__["name"] = name
        __props__["node_template"] = node_template
        __props__["project"] = project
        __props__["self_link"] = self_link
        __props__["size"] = size
        __props__["zone"] = zone
        return NodeGroup(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

