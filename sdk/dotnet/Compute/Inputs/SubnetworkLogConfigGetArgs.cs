// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class SubnetworkLogConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Can only be specified if VPC flow logging for this subnetwork is enabled.
        /// Toggles the aggregation interval for collecting flow logs. Increasing the
        /// interval time will reduce the amount of generated flow logs for long
        /// lasting connections. Default is an interval of 5 seconds per connection.
        /// Default value is `INTERVAL_5_SEC`.
        /// Possible values are `INTERVAL_5_SEC`, `INTERVAL_30_SEC`, `INTERVAL_1_MIN`, `INTERVAL_5_MIN`, `INTERVAL_10_MIN`, and `INTERVAL_15_MIN`.
        /// </summary>
        [Input("aggregationInterval")]
        public Input<string>? AggregationInterval { get; set; }

        /// <summary>
        /// Export filter used to define which VPC flow logs should be logged, as as CEL expression. See
        /// https://cloud.google.com/vpc/docs/flow-logs#filtering for details on how to format this field.
        /// The default value is 'true', which evaluates to include everything.
        /// </summary>
        [Input("filterExpr")]
        public Input<string>? FilterExpr { get; set; }

        /// <summary>
        /// Can only be specified if VPC flow logging for this subnetwork is enabled.
        /// The value of the field must be in [0, 1]. Set the sampling rate of VPC
        /// flow logs within the subnetwork where 1.0 means all collected logs are
        /// reported and 0.0 means no logs are reported. Default is 0.5 which means
        /// half of all collected logs are reported.
        /// </summary>
        [Input("flowSampling")]
        public Input<double>? FlowSampling { get; set; }

        /// <summary>
        /// Can only be specified if VPC flow logging for this subnetwork is enabled.
        /// Configures whether metadata fields should be added to the reported VPC
        /// flow logs.
        /// Default value is `INCLUDE_ALL_METADATA`.
        /// Possible values are `EXCLUDE_ALL_METADATA`, `INCLUDE_ALL_METADATA`, and `CUSTOM_METADATA`.
        /// </summary>
        [Input("metadata")]
        public Input<string>? Metadata { get; set; }

        [Input("metadataFields")]
        private InputList<string>? _metadataFields;

        /// <summary>
        /// List of metadata fields that should be added to reported logs.
        /// Can only be specified if VPC flow logs for this subnetwork is enabled and "metadata" is set to CUSTOM_METADATA.
        /// </summary>
        public InputList<string> MetadataFields
        {
            get => _metadataFields ?? (_metadataFields = new InputList<string>());
            set => _metadataFields = value;
        }

        public SubnetworkLogConfigGetArgs()
        {
        }
    }
}
