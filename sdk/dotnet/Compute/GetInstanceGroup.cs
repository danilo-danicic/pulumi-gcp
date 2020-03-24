// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    public static partial class Invokes
    {
        /// <summary>
        /// Get a Compute Instance Group within GCE.
        /// For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups)
        /// and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroups)
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/google_compute_instance_group.html.markdown.
        /// </summary>
        [Obsolete("Use GetInstanceGroup.InvokeAsync() instead")]
        public static Task<GetInstanceGroupResult> GetInstanceGroup(GetInstanceGroupArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInstanceGroupResult>("gcp:compute/getInstanceGroup:getInstanceGroup", args ?? InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetInstanceGroup
    {
        /// <summary>
        /// Get a Compute Instance Group within GCE.
        /// For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups)
        /// and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroups)
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/google_compute_instance_group.html.markdown.
        /// </summary>
        public static Task<GetInstanceGroupResult> InvokeAsync(GetInstanceGroupArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInstanceGroupResult>("gcp:compute/getInstanceGroup:getInstanceGroup", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetInstanceGroupArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the instance group. Either `name` or `self_link` must be provided.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs. If it
        /// is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        /// <summary>
        /// The self link of the instance group. Either `name` or `self_link` must be provided.
        /// </summary>
        [Input("selfLink")]
        public string? SelfLink { get; set; }

        /// <summary>
        /// The zone of the instance group. If referencing the instance group by name
        /// and `zone` is not provided, the provider zone is used.
        /// </summary>
        [Input("zone")]
        public string? Zone { get; set; }

        public GetInstanceGroupArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetInstanceGroupResult
    {
        /// <summary>
        /// Textual description of the instance group.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// List of instances in the group.
        /// </summary>
        public readonly ImmutableArray<string> Instances;
        public readonly string? Name;
        /// <summary>
        /// List of named ports in the group.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetInstanceGroupNamedPortsResult> NamedPorts;
        /// <summary>
        /// The URL of the network the instance group is in.
        /// </summary>
        public readonly string Network;
        public readonly string Project;
        /// <summary>
        /// The URI of the resource.
        /// </summary>
        public readonly string SelfLink;
        /// <summary>
        /// The number of instances in the group.
        /// </summary>
        public readonly int Size;
        public readonly string Zone;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetInstanceGroupResult(
            string description,
            ImmutableArray<string> instances,
            string? name,
            ImmutableArray<Outputs.GetInstanceGroupNamedPortsResult> namedPorts,
            string network,
            string project,
            string selfLink,
            int size,
            string zone,
            string id)
        {
            Description = description;
            Instances = instances;
            Name = name;
            NamedPorts = namedPorts;
            Network = network;
            Project = project;
            SelfLink = selfLink;
            Size = size;
            Zone = zone;
            Id = id;
        }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetInstanceGroupNamedPortsResult
    {
        /// <summary>
        /// The name of the instance group. Either `name` or `self_link` must be provided.
        /// </summary>
        public readonly string Name;
        public readonly int Port;

        [OutputConstructor]
        private GetInstanceGroupNamedPortsResult(
            string name,
            int port)
        {
            Name = name;
            Port = port;
        }
    }
    }
}
