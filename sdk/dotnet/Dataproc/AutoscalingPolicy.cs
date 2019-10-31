// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Dataproc
{
    /// <summary>
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dataproc_autoscaling_policy.html.markdown.
    /// </summary>
    public partial class AutoscalingPolicy : Pulumi.CustomResource
    {
        [Output("basicAlgorithm")]
        public Output<Outputs.AutoscalingPolicyBasicAlgorithm?> BasicAlgorithm { get; private set; } = null!;

        [Output("location")]
        public Output<string?> Location { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("policyId")]
        public Output<string> PolicyId { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        [Output("secondaryWorkerConfig")]
        public Output<Outputs.AutoscalingPolicySecondaryWorkerConfig?> SecondaryWorkerConfig { get; private set; } = null!;

        [Output("workerConfig")]
        public Output<Outputs.AutoscalingPolicyWorkerConfig?> WorkerConfig { get; private set; } = null!;


        /// <summary>
        /// Create a AutoscalingPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AutoscalingPolicy(string name, AutoscalingPolicyArgs args, CustomResourceOptions? options = null)
            : base("gcp:dataproc/autoscalingPolicy:AutoscalingPolicy", name, args, MakeResourceOptions(options, ""))
        {
        }

        private AutoscalingPolicy(string name, Input<string> id, AutoscalingPolicyState? state = null, CustomResourceOptions? options = null)
            : base("gcp:dataproc/autoscalingPolicy:AutoscalingPolicy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AutoscalingPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AutoscalingPolicy Get(string name, Input<string> id, AutoscalingPolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new AutoscalingPolicy(name, id, state, options);
        }
    }

    public sealed class AutoscalingPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("basicAlgorithm")]
        public Input<Inputs.AutoscalingPolicyBasicAlgorithmArgs>? BasicAlgorithm { get; set; }

        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("policyId", required: true)]
        public Input<string> PolicyId { get; set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("secondaryWorkerConfig")]
        public Input<Inputs.AutoscalingPolicySecondaryWorkerConfigArgs>? SecondaryWorkerConfig { get; set; }

        [Input("workerConfig")]
        public Input<Inputs.AutoscalingPolicyWorkerConfigArgs>? WorkerConfig { get; set; }

        public AutoscalingPolicyArgs()
        {
        }
    }

    public sealed class AutoscalingPolicyState : Pulumi.ResourceArgs
    {
        [Input("basicAlgorithm")]
        public Input<Inputs.AutoscalingPolicyBasicAlgorithmGetArgs>? BasicAlgorithm { get; set; }

        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("policyId")]
        public Input<string>? PolicyId { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("secondaryWorkerConfig")]
        public Input<Inputs.AutoscalingPolicySecondaryWorkerConfigGetArgs>? SecondaryWorkerConfig { get; set; }

        [Input("workerConfig")]
        public Input<Inputs.AutoscalingPolicyWorkerConfigGetArgs>? WorkerConfig { get; set; }

        public AutoscalingPolicyState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class AutoscalingPolicyBasicAlgorithmArgs : Pulumi.ResourceArgs
    {
        [Input("cooldownPeriod")]
        public Input<string>? CooldownPeriod { get; set; }

        [Input("yarnConfig", required: true)]
        public Input<AutoscalingPolicyBasicAlgorithmYarnConfigArgs> YarnConfig { get; set; } = null!;

        public AutoscalingPolicyBasicAlgorithmArgs()
        {
        }
    }

    public sealed class AutoscalingPolicyBasicAlgorithmGetArgs : Pulumi.ResourceArgs
    {
        [Input("cooldownPeriod")]
        public Input<string>? CooldownPeriod { get; set; }

        [Input("yarnConfig", required: true)]
        public Input<AutoscalingPolicyBasicAlgorithmYarnConfigGetArgs> YarnConfig { get; set; } = null!;

        public AutoscalingPolicyBasicAlgorithmGetArgs()
        {
        }
    }

    public sealed class AutoscalingPolicyBasicAlgorithmYarnConfigArgs : Pulumi.ResourceArgs
    {
        [Input("gracefulDecommissionTimeout", required: true)]
        public Input<string> GracefulDecommissionTimeout { get; set; } = null!;

        [Input("scaleDownFactor", required: true)]
        public Input<double> ScaleDownFactor { get; set; } = null!;

        [Input("scaleDownMinWorkerFraction")]
        public Input<double>? ScaleDownMinWorkerFraction { get; set; }

        [Input("scaleUpFactor", required: true)]
        public Input<double> ScaleUpFactor { get; set; } = null!;

        [Input("scaleUpMinWorkerFraction")]
        public Input<double>? ScaleUpMinWorkerFraction { get; set; }

        public AutoscalingPolicyBasicAlgorithmYarnConfigArgs()
        {
        }
    }

    public sealed class AutoscalingPolicyBasicAlgorithmYarnConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("gracefulDecommissionTimeout", required: true)]
        public Input<string> GracefulDecommissionTimeout { get; set; } = null!;

        [Input("scaleDownFactor", required: true)]
        public Input<double> ScaleDownFactor { get; set; } = null!;

        [Input("scaleDownMinWorkerFraction")]
        public Input<double>? ScaleDownMinWorkerFraction { get; set; }

        [Input("scaleUpFactor", required: true)]
        public Input<double> ScaleUpFactor { get; set; } = null!;

        [Input("scaleUpMinWorkerFraction")]
        public Input<double>? ScaleUpMinWorkerFraction { get; set; }

        public AutoscalingPolicyBasicAlgorithmYarnConfigGetArgs()
        {
        }
    }

    public sealed class AutoscalingPolicySecondaryWorkerConfigArgs : Pulumi.ResourceArgs
    {
        [Input("maxInstances")]
        public Input<int>? MaxInstances { get; set; }

        [Input("minInstances")]
        public Input<int>? MinInstances { get; set; }

        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public AutoscalingPolicySecondaryWorkerConfigArgs()
        {
        }
    }

    public sealed class AutoscalingPolicySecondaryWorkerConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("maxInstances")]
        public Input<int>? MaxInstances { get; set; }

        [Input("minInstances")]
        public Input<int>? MinInstances { get; set; }

        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public AutoscalingPolicySecondaryWorkerConfigGetArgs()
        {
        }
    }

    public sealed class AutoscalingPolicyWorkerConfigArgs : Pulumi.ResourceArgs
    {
        [Input("maxInstances", required: true)]
        public Input<int> MaxInstances { get; set; } = null!;

        [Input("minInstances")]
        public Input<int>? MinInstances { get; set; }

        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public AutoscalingPolicyWorkerConfigArgs()
        {
        }
    }

    public sealed class AutoscalingPolicyWorkerConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("maxInstances", required: true)]
        public Input<int> MaxInstances { get; set; } = null!;

        [Input("minInstances")]
        public Input<int>? MinInstances { get; set; }

        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public AutoscalingPolicyWorkerConfigGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class AutoscalingPolicyBasicAlgorithm
    {
        public readonly string? CooldownPeriod;
        public readonly AutoscalingPolicyBasicAlgorithmYarnConfig YarnConfig;

        [OutputConstructor]
        private AutoscalingPolicyBasicAlgorithm(
            string? cooldownPeriod,
            AutoscalingPolicyBasicAlgorithmYarnConfig yarnConfig)
        {
            CooldownPeriod = cooldownPeriod;
            YarnConfig = yarnConfig;
        }
    }

    [OutputType]
    public sealed class AutoscalingPolicyBasicAlgorithmYarnConfig
    {
        public readonly string GracefulDecommissionTimeout;
        public readonly double ScaleDownFactor;
        public readonly double? ScaleDownMinWorkerFraction;
        public readonly double ScaleUpFactor;
        public readonly double? ScaleUpMinWorkerFraction;

        [OutputConstructor]
        private AutoscalingPolicyBasicAlgorithmYarnConfig(
            string gracefulDecommissionTimeout,
            double scaleDownFactor,
            double? scaleDownMinWorkerFraction,
            double scaleUpFactor,
            double? scaleUpMinWorkerFraction)
        {
            GracefulDecommissionTimeout = gracefulDecommissionTimeout;
            ScaleDownFactor = scaleDownFactor;
            ScaleDownMinWorkerFraction = scaleDownMinWorkerFraction;
            ScaleUpFactor = scaleUpFactor;
            ScaleUpMinWorkerFraction = scaleUpMinWorkerFraction;
        }
    }

    [OutputType]
    public sealed class AutoscalingPolicySecondaryWorkerConfig
    {
        public readonly int? MaxInstances;
        public readonly int? MinInstances;
        public readonly int? Weight;

        [OutputConstructor]
        private AutoscalingPolicySecondaryWorkerConfig(
            int? maxInstances,
            int? minInstances,
            int? weight)
        {
            MaxInstances = maxInstances;
            MinInstances = minInstances;
            Weight = weight;
        }
    }

    [OutputType]
    public sealed class AutoscalingPolicyWorkerConfig
    {
        public readonly int MaxInstances;
        public readonly int? MinInstances;
        public readonly int? Weight;

        [OutputConstructor]
        private AutoscalingPolicyWorkerConfig(
            int maxInstances,
            int? minInstances,
            int? weight)
        {
            MaxInstances = maxInstances;
            MinInstances = minInstances;
            Weight = weight;
        }
    }
    }
}
