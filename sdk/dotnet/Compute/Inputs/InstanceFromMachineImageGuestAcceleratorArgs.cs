// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class InstanceFromMachineImageGuestAcceleratorArgs : Pulumi.ResourceArgs
    {
        [Input("count", required: true)]
        public Input<int> Count { get; set; } = null!;

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public InstanceFromMachineImageGuestAcceleratorArgs()
        {
        }
    }
}
