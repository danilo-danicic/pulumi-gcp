// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    /// <summary>
    /// Represents an Autoscaler resource.
    /// 
    /// Autoscalers allow you to automatically scale virtual machine instances in
    /// managed instance groups according to an autoscaling policy that you
    /// define.
    /// 
    /// To get more information about Autoscaler, see:
    /// 
    /// * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/autoscalers)
    /// * How-to Guides
    ///     * [Autoscaling Groups of Instances](https://cloud.google.com/compute/docs/autoscaler/)
    /// 
    /// ## Example Usage
    /// </summary>
    [Obsolete(@"gcp.compute.Autoscalar has been deprecated in favor of gcp.compute.Autoscaler")]
    public partial class Autoscalar : Pulumi.CustomResource
    {
        /// <summary>
        /// The configuration parameters for the autoscaling algorithm. You can
        /// define one or more of the policies for an autoscaler: cpuUtilization,
        /// customMetricUtilizations, and loadBalancingUtilization.
        /// If none of these are specified, the default will be to autoscale based
        /// on cpuUtilization to 0.6 or 60%.  Structure is documented below.
        /// </summary>
        [Output("autoscalingPolicy")]
        public Output<Outputs.AutoscalarAutoscalingPolicy> AutoscalingPolicy { get; private set; } = null!;

        /// <summary>
        /// Creation timestamp in RFC3339 text format.
        /// </summary>
        [Output("creationTimestamp")]
        public Output<string> CreationTimestamp { get; private set; } = null!;

        /// <summary>
        /// An optional description of this resource.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The identifier (type) of the Stackdriver Monitoring metric.
        /// The metric cannot have negative values.
        /// The metric must have a value type of INT64 or DOUBLE.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        /// <summary>
        /// Fraction of backend capacity utilization (set in HTTP(s) load
        /// balancing configuration) that autoscaler should maintain. Must
        /// be a positive float value. If not defined, the default is 0.8.
        /// </summary>
        [Output("target")]
        public Output<string> Target { get; private set; } = null!;

        /// <summary>
        /// URL of the zone where the instance group resides.
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a Autoscalar resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Autoscalar(string name, AutoscalarArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/autoscalar:Autoscalar", name, args ?? new AutoscalarArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Autoscalar(string name, Input<string> id, AutoscalarState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/autoscalar:Autoscalar", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Autoscalar resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Autoscalar Get(string name, Input<string> id, AutoscalarState? state = null, CustomResourceOptions? options = null)
        {
            return new Autoscalar(name, id, state, options);
        }
    }

    public sealed class AutoscalarArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The configuration parameters for the autoscaling algorithm. You can
        /// define one or more of the policies for an autoscaler: cpuUtilization,
        /// customMetricUtilizations, and loadBalancingUtilization.
        /// If none of these are specified, the default will be to autoscale based
        /// on cpuUtilization to 0.6 or 60%.  Structure is documented below.
        /// </summary>
        [Input("autoscalingPolicy", required: true)]
        public Input<Inputs.AutoscalarAutoscalingPolicyArgs> AutoscalingPolicy { get; set; } = null!;

        /// <summary>
        /// An optional description of this resource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The identifier (type) of the Stackdriver Monitoring metric.
        /// The metric cannot have negative values.
        /// The metric must have a value type of INT64 or DOUBLE.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// Fraction of backend capacity utilization (set in HTTP(s) load
        /// balancing configuration) that autoscaler should maintain. Must
        /// be a positive float value. If not defined, the default is 0.8.
        /// </summary>
        [Input("target", required: true)]
        public Input<string> Target { get; set; } = null!;

        /// <summary>
        /// URL of the zone where the instance group resides.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public AutoscalarArgs()
        {
        }
    }

    public sealed class AutoscalarState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The configuration parameters for the autoscaling algorithm. You can
        /// define one or more of the policies for an autoscaler: cpuUtilization,
        /// customMetricUtilizations, and loadBalancingUtilization.
        /// If none of these are specified, the default will be to autoscale based
        /// on cpuUtilization to 0.6 or 60%.  Structure is documented below.
        /// </summary>
        [Input("autoscalingPolicy")]
        public Input<Inputs.AutoscalarAutoscalingPolicyGetArgs>? AutoscalingPolicy { get; set; }

        /// <summary>
        /// Creation timestamp in RFC3339 text format.
        /// </summary>
        [Input("creationTimestamp")]
        public Input<string>? CreationTimestamp { get; set; }

        /// <summary>
        /// An optional description of this resource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The identifier (type) of the Stackdriver Monitoring metric.
        /// The metric cannot have negative values.
        /// The metric must have a value type of INT64 or DOUBLE.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        /// <summary>
        /// Fraction of backend capacity utilization (set in HTTP(s) load
        /// balancing configuration) that autoscaler should maintain. Must
        /// be a positive float value. If not defined, the default is 0.8.
        /// </summary>
        [Input("target")]
        public Input<string>? Target { get; set; }

        /// <summary>
        /// URL of the zone where the instance group resides.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public AutoscalarState()
        {
        }
    }
}
