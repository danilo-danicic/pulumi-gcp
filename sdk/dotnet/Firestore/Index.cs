// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Firestore
{
    /// <summary>
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/firestore_index.html.markdown.
    /// </summary>
    public partial class Index : Pulumi.CustomResource
    {
        [Output("collection")]
        public Output<string> Collection { get; private set; } = null!;

        [Output("database")]
        public Output<string?> Database { get; private set; } = null!;

        [Output("fields")]
        public Output<ImmutableArray<Outputs.IndexFields>> Fields { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        [Output("queryScope")]
        public Output<string?> QueryScope { get; private set; } = null!;


        /// <summary>
        /// Create a Index resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Index(string name, IndexArgs args, CustomResourceOptions? options = null)
            : base("gcp:firestore/index:Index", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Index(string name, Input<string> id, IndexState? state = null, CustomResourceOptions? options = null)
            : base("gcp:firestore/index:Index", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Index resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Index Get(string name, Input<string> id, IndexState? state = null, CustomResourceOptions? options = null)
        {
            return new Index(name, id, state, options);
        }
    }

    public sealed class IndexArgs : Pulumi.ResourceArgs
    {
        [Input("collection", required: true)]
        public Input<string> Collection { get; set; } = null!;

        [Input("database")]
        public Input<string>? Database { get; set; }

        [Input("fields", required: true)]
        private InputList<Inputs.IndexFieldsArgs>? _fields;
        public InputList<Inputs.IndexFieldsArgs> Fields
        {
            get => _fields ?? (_fields = new InputList<Inputs.IndexFieldsArgs>());
            set => _fields = value;
        }

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("queryScope")]
        public Input<string>? QueryScope { get; set; }

        public IndexArgs()
        {
        }
    }

    public sealed class IndexState : Pulumi.ResourceArgs
    {
        [Input("collection")]
        public Input<string>? Collection { get; set; }

        [Input("database")]
        public Input<string>? Database { get; set; }

        [Input("fields")]
        private InputList<Inputs.IndexFieldsGetArgs>? _fields;
        public InputList<Inputs.IndexFieldsGetArgs> Fields
        {
            get => _fields ?? (_fields = new InputList<Inputs.IndexFieldsGetArgs>());
            set => _fields = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("queryScope")]
        public Input<string>? QueryScope { get; set; }

        public IndexState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class IndexFieldsArgs : Pulumi.ResourceArgs
    {
        [Input("arrayConfig")]
        public Input<string>? ArrayConfig { get; set; }

        [Input("fieldPath")]
        public Input<string>? FieldPath { get; set; }

        [Input("order")]
        public Input<string>? Order { get; set; }

        public IndexFieldsArgs()
        {
        }
    }

    public sealed class IndexFieldsGetArgs : Pulumi.ResourceArgs
    {
        [Input("arrayConfig")]
        public Input<string>? ArrayConfig { get; set; }

        [Input("fieldPath")]
        public Input<string>? FieldPath { get; set; }

        [Input("order")]
        public Input<string>? Order { get; set; }

        public IndexFieldsGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class IndexFields
    {
        public readonly string? ArrayConfig;
        public readonly string? FieldPath;
        public readonly string? Order;

        [OutputConstructor]
        private IndexFields(
            string? arrayConfig,
            string? fieldPath,
            string? order)
        {
            ArrayConfig = arrayConfig;
            FieldPath = fieldPath;
            Order = order;
        }
    }
    }
}
