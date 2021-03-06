// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class BackendBucketCdnPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("cacheMode")]
        public Input<string>? CacheMode { get; set; }

        [Input("clientTtl")]
        public Input<int>? ClientTtl { get; set; }

        [Input("defaultTtl")]
        public Input<int>? DefaultTtl { get; set; }

        [Input("maxTtl")]
        public Input<int>? MaxTtl { get; set; }

        [Input("negativeCaching")]
        public Input<bool>? NegativeCaching { get; set; }

        [Input("negativeCachingPolicies")]
        private InputList<Inputs.BackendBucketCdnPolicyNegativeCachingPolicyArgs>? _negativeCachingPolicies;
        public InputList<Inputs.BackendBucketCdnPolicyNegativeCachingPolicyArgs> NegativeCachingPolicies
        {
            get => _negativeCachingPolicies ?? (_negativeCachingPolicies = new InputList<Inputs.BackendBucketCdnPolicyNegativeCachingPolicyArgs>());
            set => _negativeCachingPolicies = value;
        }

        [Input("serveWhileStale")]
        public Input<int>? ServeWhileStale { get; set; }

        /// <summary>
        /// Maximum number of seconds the response to a signed URL request will
        /// be considered fresh. After this time period,
        /// the response will be revalidated before being served.
        /// When serving responses to signed URL requests,
        /// Cloud CDN will internally behave as though
        /// all responses from this backend had a "Cache-Control: public,
        /// max-age=[TTL]" header, regardless of any existing Cache-Control
        /// header. The actual headers served in responses will not be altered.
        /// </summary>
        [Input("signedUrlCacheMaxAgeSec")]
        public Input<int>? SignedUrlCacheMaxAgeSec { get; set; }

        public BackendBucketCdnPolicyArgs()
        {
        }
    }
}
