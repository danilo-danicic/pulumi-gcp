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
        /// Provides access to available Google Compute zones in a region for a given project.
        /// See more about [regions and zones](https://cloud.google.com/compute/docs/regions-zones/regions-zones) in the upstream docs.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/google_compute_zones.html.markdown.
        /// </summary>
        public static Task<GetZonesResult> GetZones(GetZonesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetZonesResult>("gcp:compute/getZones:getZones", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetZonesArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Project from which to list available zones. Defaults to project declared in the provider.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        /// <summary>
        /// Region from which to list available zones. Defaults to region declared in the provider.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        /// <summary>
        /// Allows to filter list of zones based on their current status. Status can be either `UP` or `DOWN`.
        /// Defaults to no filtering (all available zones - both `UP` and `DOWN`).
        /// </summary>
        [Input("status")]
        public string? Status { get; set; }

        public GetZonesArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetZonesResult
    {
        /// <summary>
        /// A list of zones available in the given region
        /// </summary>
        public readonly ImmutableArray<string> Names;
        public readonly string Project;
        public readonly string? Region;
        public readonly string? Status;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetZonesResult(
            ImmutableArray<string> names,
            string project,
            string? region,
            string? status,
            string id)
        {
            Names = names;
            Project = project;
            Region = region;
            Status = status;
            Id = id;
        }
    }
}
