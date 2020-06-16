// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Inputs
{

    public sealed class UptimeCheckConfigContentMatcherGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// String or regex content to match (max 1024 bytes)
        /// </summary>
        [Input("content", required: true)]
        public Input<string> Content { get; set; } = null!;

        /// <summary>
        /// The type of content matcher that will be applied to the server output, compared to the content string when the check is run.
        /// </summary>
        [Input("matcher")]
        public Input<string>? Matcher { get; set; }

        public UptimeCheckConfigContentMatcherGetArgs()
        {
        }
    }
}
