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
        /// Provides available node types for Compute Engine sole-tenant nodes in a zone
        /// for a given project. For more information, see [the official documentation](https://cloud.google.com/compute/docs/nodes/#types) and [API](https://cloud.google.com/compute/docs/reference/rest/v1/nodeTypes).
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/google_compute_node_types.html.markdown.
        /// </summary>
        public static Task<GetNodeTypesResult> GetNodeTypes(GetNodeTypesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNodeTypesResult>("gcp:compute/getNodeTypes:getNodeTypes", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetNodeTypesArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the project to list available node types for.
        /// Should match the project the nodes of this type will be deployed to.
        /// Defaults to the project that the provider is authenticated with.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        /// <summary>
        /// The zone to list node types for. Should be in zone of intended node groups and region of referencing node template. If `zone` is not specified, the provider-level zone must be set and is used
        /// instead.
        /// </summary>
        [Input("zone")]
        public string? Zone { get; set; }

        public GetNodeTypesArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetNodeTypesResult
    {
        /// <summary>
        /// A list of node types available in the given zone and project.
        /// </summary>
        public readonly ImmutableArray<string> Names;
        public readonly string Project;
        public readonly string Zone;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetNodeTypesResult(
            ImmutableArray<string> names,
            string project,
            string zone,
            string id)
        {
            Names = names;
            Project = project;
            Zone = zone;
            Id = id;
        }
    }
}
