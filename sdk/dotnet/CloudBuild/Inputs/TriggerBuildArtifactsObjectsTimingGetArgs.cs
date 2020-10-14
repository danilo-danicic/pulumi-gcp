// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudBuild.Inputs
{

    public sealed class TriggerBuildArtifactsObjectsTimingGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// End of time span.
        /// A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to
        /// nine fractional digits. Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        /// </summary>
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        /// <summary>
        /// Start of time span.
        /// A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to
        /// nine fractional digits. Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        /// </summary>
        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        public TriggerBuildArtifactsObjectsTimingGetArgs()
        {
        }
    }
}