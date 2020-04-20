// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Dataproc.Outputs
{

    [OutputType]
    public sealed class ClusterClusterConfigMasterConfigDiskConfig
    {
        /// <summary>
        /// Size of the primary disk attached to each preemptible worker node, specified
        /// in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
        /// computed value if not set (currently 500GB). Note: If SSDs are not
        /// attached, it also contains the HDFS data blocks and Hadoop working directories.
        /// </summary>
        public readonly int? BootDiskSizeGb;
        /// <summary>
        /// The disk type of the primary disk attached to each preemptible worker node.
        /// One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
        /// </summary>
        public readonly string? BootDiskType;
        /// <summary>
        /// The amount of local SSD disks that will be
        /// attached to each preemptible worker node. Defaults to 0.
        /// </summary>
        public readonly int? NumLocalSsds;

        [OutputConstructor]
        private ClusterClusterConfigMasterConfigDiskConfig(
            int? bootDiskSizeGb,

            string? bootDiskType,

            int? numLocalSsds)
        {
            BootDiskSizeGb = bootDiskSizeGb;
            BootDiskType = bootDiskType;
            NumLocalSsds = numLocalSsds;
        }
    }
}