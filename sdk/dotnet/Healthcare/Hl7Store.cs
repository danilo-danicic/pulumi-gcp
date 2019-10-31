// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Healthcare
{
    /// <summary>
    /// A Hl7V2Store is a datastore inside a Healthcare dataset that conforms to the FHIR (https://www.hl7.org/hl7V2/STU3/)
    /// standard for Healthcare information exchange
    /// 
    /// To get more information about Hl7V2Store, see:
    /// 
    /// * [API documentation](https://cloud.google.com/healthcare/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores)
    /// * How-to Guides
    ///     * [Creating a HL7v2 Store](https://cloud.google.com/healthcare/docs/how-tos/hl7v2)
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/healthcare_hl7_v2_store.html.markdown.
    /// </summary>
    public partial class Hl7Store : Pulumi.CustomResource
    {
        [Output("dataset")]
        public Output<string> Dataset { get; private set; } = null!;

        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("notificationConfig")]
        public Output<Outputs.Hl7StoreNotificationConfig?> NotificationConfig { get; private set; } = null!;

        [Output("parserConfig")]
        public Output<Outputs.Hl7StoreParserConfig?> ParserConfig { get; private set; } = null!;

        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;


        /// <summary>
        /// Create a Hl7Store resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Hl7Store(string name, Hl7StoreArgs args, CustomResourceOptions? options = null)
            : base("gcp:healthcare/hl7Store:Hl7Store", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Hl7Store(string name, Input<string> id, Hl7StoreState? state = null, CustomResourceOptions? options = null)
            : base("gcp:healthcare/hl7Store:Hl7Store", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Hl7Store resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Hl7Store Get(string name, Input<string> id, Hl7StoreState? state = null, CustomResourceOptions? options = null)
        {
            return new Hl7Store(name, id, state, options);
        }
    }

    public sealed class Hl7StoreArgs : Pulumi.ResourceArgs
    {
        [Input("dataset", required: true)]
        public Input<string> Dataset { get; set; } = null!;

        [Input("labels")]
        private InputMap<string>? _labels;
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("notificationConfig")]
        public Input<Inputs.Hl7StoreNotificationConfigArgs>? NotificationConfig { get; set; }

        [Input("parserConfig")]
        public Input<Inputs.Hl7StoreParserConfigArgs>? ParserConfig { get; set; }

        public Hl7StoreArgs()
        {
        }
    }

    public sealed class Hl7StoreState : Pulumi.ResourceArgs
    {
        [Input("dataset")]
        public Input<string>? Dataset { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("notificationConfig")]
        public Input<Inputs.Hl7StoreNotificationConfigGetArgs>? NotificationConfig { get; set; }

        [Input("parserConfig")]
        public Input<Inputs.Hl7StoreParserConfigGetArgs>? ParserConfig { get; set; }

        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        public Hl7StoreState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class Hl7StoreNotificationConfigArgs : Pulumi.ResourceArgs
    {
        [Input("pubsubTopic", required: true)]
        public Input<string> PubsubTopic { get; set; } = null!;

        public Hl7StoreNotificationConfigArgs()
        {
        }
    }

    public sealed class Hl7StoreNotificationConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("pubsubTopic", required: true)]
        public Input<string> PubsubTopic { get; set; } = null!;

        public Hl7StoreNotificationConfigGetArgs()
        {
        }
    }

    public sealed class Hl7StoreParserConfigArgs : Pulumi.ResourceArgs
    {
        [Input("allowNullHeader")]
        public Input<bool>? AllowNullHeader { get; set; }

        [Input("segmentTerminator")]
        public Input<string>? SegmentTerminator { get; set; }

        public Hl7StoreParserConfigArgs()
        {
        }
    }

    public sealed class Hl7StoreParserConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("allowNullHeader")]
        public Input<bool>? AllowNullHeader { get; set; }

        [Input("segmentTerminator")]
        public Input<string>? SegmentTerminator { get; set; }

        public Hl7StoreParserConfigGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class Hl7StoreNotificationConfig
    {
        public readonly string PubsubTopic;

        [OutputConstructor]
        private Hl7StoreNotificationConfig(string pubsubTopic)
        {
            PubsubTopic = pubsubTopic;
        }
    }

    [OutputType]
    public sealed class Hl7StoreParserConfig
    {
        public readonly bool? AllowNullHeader;
        public readonly string? SegmentTerminator;

        [OutputConstructor]
        private Hl7StoreParserConfig(
            bool? allowNullHeader,
            string? segmentTerminator)
        {
            AllowNullHeader = allowNullHeader;
            SegmentTerminator = segmentTerminator;
        }
    }
    }
}
