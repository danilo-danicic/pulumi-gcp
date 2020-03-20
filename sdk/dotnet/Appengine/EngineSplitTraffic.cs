// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AppEngine
{
    public partial class EngineSplitTraffic : Pulumi.CustomResource
    {
        /// <summary>
        /// If set to true traffic will be migrated to this version.
        /// </summary>
        [Output("migrateTraffic")]
        public Output<bool?> MigrateTraffic { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The name of the service these settings apply to.
        /// </summary>
        [Output("service")]
        public Output<string> Service { get; private set; } = null!;

        /// <summary>
        /// Mapping that defines fractional HTTP traffic diversion to different versions within the service.
        /// </summary>
        [Output("split")]
        public Output<Outputs.EngineSplitTrafficSplit> Split { get; private set; } = null!;


        /// <summary>
        /// Create a EngineSplitTraffic resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EngineSplitTraffic(string name, EngineSplitTrafficArgs args, CustomResourceOptions? options = null)
            : base("gcp:appengine/engineSplitTraffic:EngineSplitTraffic", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private EngineSplitTraffic(string name, Input<string> id, EngineSplitTrafficState? state = null, CustomResourceOptions? options = null)
            : base("gcp:appengine/engineSplitTraffic:EngineSplitTraffic", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing EngineSplitTraffic resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EngineSplitTraffic Get(string name, Input<string> id, EngineSplitTrafficState? state = null, CustomResourceOptions? options = null)
        {
            return new EngineSplitTraffic(name, id, state, options);
        }
    }

    public sealed class EngineSplitTrafficArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If set to true traffic will be migrated to this version.
        /// </summary>
        [Input("migrateTraffic")]
        public Input<bool>? MigrateTraffic { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The name of the service these settings apply to.
        /// </summary>
        [Input("service", required: true)]
        public Input<string> Service { get; set; } = null!;

        /// <summary>
        /// Mapping that defines fractional HTTP traffic diversion to different versions within the service.
        /// </summary>
        [Input("split", required: true)]
        public Input<Inputs.EngineSplitTrafficSplitArgs> Split { get; set; } = null!;

        public EngineSplitTrafficArgs()
        {
        }
    }

    public sealed class EngineSplitTrafficState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If set to true traffic will be migrated to this version.
        /// </summary>
        [Input("migrateTraffic")]
        public Input<bool>? MigrateTraffic { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The name of the service these settings apply to.
        /// </summary>
        [Input("service")]
        public Input<string>? Service { get; set; }

        /// <summary>
        /// Mapping that defines fractional HTTP traffic diversion to different versions within the service.
        /// </summary>
        [Input("split")]
        public Input<Inputs.EngineSplitTrafficSplitGetArgs>? Split { get; set; }

        public EngineSplitTrafficState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class EngineSplitTrafficSplitArgs : Pulumi.ResourceArgs
    {
        [Input("allocations", required: true)]
        private InputMap<string>? _allocations;
        public InputMap<string> Allocations
        {
            get => _allocations ?? (_allocations = new InputMap<string>());
            set => _allocations = value;
        }

        [Input("shardBy")]
        public Input<string>? ShardBy { get; set; }

        public EngineSplitTrafficSplitArgs()
        {
        }
    }

    public sealed class EngineSplitTrafficSplitGetArgs : Pulumi.ResourceArgs
    {
        [Input("allocations", required: true)]
        private InputMap<string>? _allocations;
        public InputMap<string> Allocations
        {
            get => _allocations ?? (_allocations = new InputMap<string>());
            set => _allocations = value;
        }

        [Input("shardBy")]
        public Input<string>? ShardBy { get; set; }

        public EngineSplitTrafficSplitGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class EngineSplitTrafficSplit
    {
        public readonly ImmutableDictionary<string, string> Allocations;
        public readonly string? ShardBy;

        [OutputConstructor]
        private EngineSplitTrafficSplit(
            ImmutableDictionary<string, string> allocations,
            string? shardBy)
        {
            Allocations = allocations;
            ShardBy = shardBy;
        }
    }
    }
}
