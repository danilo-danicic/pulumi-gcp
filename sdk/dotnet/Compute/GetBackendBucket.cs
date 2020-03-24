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
        /// Get information about a BackendBucket.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_compute_backend_bucket.html.markdown.
        /// </summary>
        [Obsolete("Use GetBackendBucket.InvokeAsync() instead")]
        public static Task<GetBackendBucketResult> GetBackendBucket(GetBackendBucketArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetBackendBucketResult>("gcp:compute/getBackendBucket:getBackendBucket", args ?? InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetBackendBucket
    {
        /// <summary>
        /// Get information about a BackendBucket.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_compute_backend_bucket.html.markdown.
        /// </summary>
        public static Task<GetBackendBucketResult> InvokeAsync(GetBackendBucketArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetBackendBucketResult>("gcp:compute/getBackendBucket:getBackendBucket", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetBackendBucketArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the resource.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs. If it
        /// is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        public GetBackendBucketArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetBackendBucketResult
    {
        /// <summary>
        /// Cloud Storage bucket name.
        /// </summary>
        public readonly string BucketName;
        /// <summary>
        /// Cloud CDN configuration for this Backend Bucket. Structure is documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetBackendBucketCdnPoliciesResult> CdnPolicies;
        /// <summary>
        /// Creation timestamp in RFC3339 text format.
        /// </summary>
        public readonly string CreationTimestamp;
        /// <summary>
        /// An optional textual description of the resource; provided by the client when the resource is created.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Whether Cloud CDN is enabled for this BackendBucket.
        /// </summary>
        public readonly bool EnableCdn;
        public readonly string Name;
        public readonly string? Project;
        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        public readonly string SelfLink;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetBackendBucketResult(
            string bucketName,
            ImmutableArray<Outputs.GetBackendBucketCdnPoliciesResult> cdnPolicies,
            string creationTimestamp,
            string description,
            bool enableCdn,
            string name,
            string? project,
            string selfLink,
            string id)
        {
            BucketName = bucketName;
            CdnPolicies = cdnPolicies;
            CreationTimestamp = creationTimestamp;
            Description = description;
            EnableCdn = enableCdn;
            Name = name;
            Project = project;
            SelfLink = selfLink;
            Id = id;
        }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetBackendBucketCdnPoliciesResult
    {
        /// <summary>
        /// Maximum number of seconds the response to a signed URL request will be considered fresh. After this time period, the response will be revalidated before being served. When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a "Cache-Control: public, max-age=[TTL]" header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered.
        /// </summary>
        public readonly int SignedUrlCacheMaxAgeSec;

        [OutputConstructor]
        private GetBackendBucketCdnPoliciesResult(int signedUrlCacheMaxAgeSec)
        {
            SignedUrlCacheMaxAgeSec = signedUrlCacheMaxAgeSec;
        }
    }
    }
}
