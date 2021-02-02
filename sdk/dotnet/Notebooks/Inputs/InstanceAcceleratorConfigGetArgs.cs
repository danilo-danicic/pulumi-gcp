// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Notebooks.Inputs
{

    public sealed class InstanceAcceleratorConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Count of cores of this accelerator.
        /// </summary>
        [Input("coreCount", required: true)]
        public Input<int> CoreCount { get; set; } = null!;

        /// <summary>
        /// Type of this accelerator.
        /// Possible values are `ACCELERATOR_TYPE_UNSPECIFIED`, `NVIDIA_TESLA_K80`, `NVIDIA_TESLA_P100`, `NVIDIA_TESLA_V100`, `NVIDIA_TESLA_P4`, `NVIDIA_TESLA_T4`, `NVIDIA_TESLA_T4_VWS`, `NVIDIA_TESLA_P100_VWS`, `NVIDIA_TESLA_P4_VWS`, `NVIDIA_TESLA_A100`, `TPU_V2`, and `TPU_V3`.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public InstanceAcceleratorConfigGetArgs()
        {
        }
    }
}
