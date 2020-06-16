// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Outputs
{

    [OutputType]
    public sealed class URLMapDefaultRouteActionWeightedBackendServiceHeaderActionRequestHeadersToAdd
    {
        /// <summary>
        /// The name of the header to add.
        /// </summary>
        public readonly string? HeaderName;
        /// <summary>
        /// The value of the header to add.
        /// </summary>
        public readonly string? HeaderValue;
        /// <summary>
        /// If false, headerValue is appended to any values that already exist for the header.
        /// If true, headerValue is set for the header, discarding any values that were set for that header.
        /// </summary>
        public readonly bool? Replace;

        [OutputConstructor]
        private URLMapDefaultRouteActionWeightedBackendServiceHeaderActionRequestHeadersToAdd(
            string? headerName,

            string? headerValue,

            bool? replace)
        {
            HeaderName = headerName;
            HeaderValue = headerValue;
            Replace = replace;
        }
    }
}
