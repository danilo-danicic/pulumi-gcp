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
        /// Get the IP address from a static address. For more information see
        /// the official [API](https://cloud.google.com/compute/docs/reference/latest/addresses/get) documentation.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_compute_address.html.markdown.
        /// </summary>
        public static Task<GetAddressResult> GetAddress(GetAddressArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAddressResult>("gcp:compute/getAddress:getAddress", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetAddressArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// A unique name for the resource, required by GCE.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The project in which the resource belongs. If it
        /// is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        /// <summary>
        /// The Region in which the created address reside.
        /// If it is not provided, the provider region is used.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        public GetAddressArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetAddressResult
    {
        /// <summary>
        /// The IP of the created resource.
        /// </summary>
        public readonly string Address;
        public readonly string Name;
        public readonly string Project;
        public readonly string Region;
        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        public readonly string SelfLink;
        /// <summary>
        /// Indicates if the address is used. Possible values are: RESERVED or IN_USE.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetAddressResult(
            string address,
            string name,
            string project,
            string region,
            string selfLink,
            string status,
            string id)
        {
            Address = address;
            Name = name;
            Project = project;
            Region = region;
            SelfLink = selfLink;
            Status = status;
            Id = id;
        }
    }
}
