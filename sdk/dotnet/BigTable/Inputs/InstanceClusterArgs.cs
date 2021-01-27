// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.BigTable.Inputs
{

    public sealed class InstanceClusterArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Cloud Bigtable cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// The number of nodes in your Cloud Bigtable cluster.
        /// Required, with a minimum of `1` for a `PRODUCTION` instance. Must be left unset
        /// for a `DEVELOPMENT` instance.
        /// </summary>
        [Input("numNodes")]
        public Input<int>? NumNodes { get; set; }

        /// <summary>
        /// The storage type to use. One of `"SSD"` or
        /// `"HDD"`. Defaults to `"SSD"`.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        /// <summary>
        /// The zone to create the Cloud Bigtable cluster in. If it not
        /// specified, the provider zone is used. Each cluster must have a different zone in the same region. Zones that support
        /// Bigtable instances are noted on the [Cloud Bigtable locations page](https://cloud.google.com/bigtable/docs/locations).
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstanceClusterArgs()
        {
        }
    }
}
