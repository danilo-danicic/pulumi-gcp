// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Storage.Inputs
{

    public sealed class BucketLifecycleRuleActionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `ARCHIVE`.
        /// </summary>
        [Input("storageClass")]
        public Input<string>? StorageClass { get; set; }

        /// <summary>
        /// The type of the action of this Lifecycle Rule. Supported values include: `Delete` and `SetStorageClass`.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public BucketLifecycleRuleActionArgs()
        {
        }
    }
}
