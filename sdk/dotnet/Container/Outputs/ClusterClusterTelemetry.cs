// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Container.Outputs
{

    [OutputType]
    public sealed class ClusterClusterTelemetry
    {
        /// <summary>
        /// The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private ClusterClusterTelemetry(string type)
        {
            Type = type;
        }
    }
}
