// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class URLMapPathMatcherDefaultRouteActionUrlRewriteGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Prior to forwarding the request to the selected service, the request's host header is replaced
        /// with contents of hostRewrite.
        /// The value must be between 1 and 255 characters.
        /// </summary>
        [Input("hostRewrite")]
        public Input<string>? HostRewrite { get; set; }

        /// <summary>
        /// Prior to forwarding the request to the selected backend service, the matching portion of the
        /// request's path is replaced by pathPrefixRewrite.
        /// The value must be between 1 and 1024 characters.
        /// </summary>
        [Input("pathPrefixRewrite")]
        public Input<string>? PathPrefixRewrite { get; set; }

        public URLMapPathMatcherDefaultRouteActionUrlRewriteGetArgs()
        {
        }
    }
}
