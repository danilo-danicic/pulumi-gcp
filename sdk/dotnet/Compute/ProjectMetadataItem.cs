// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    /// <summary>
    /// Manages a single key/value pair on metadata common to all instances for
    /// a project in GCE. Using `gcp.compute.ProjectMetadataItem` lets you
    /// manage a single key/value setting with this provider rather than the entire
    /// project metadata map.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_metadata_item.html.markdown.
    /// </summary>
    public partial class ProjectMetadataItem : Pulumi.CustomResource
    {
        /// <summary>
        /// The metadata key to set.
        /// </summary>
        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs. If it
        /// is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The value to set for the given metadata key.
        /// </summary>
        [Output("value")]
        public Output<string> Value { get; private set; } = null!;


        /// <summary>
        /// Create a ProjectMetadataItem resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ProjectMetadataItem(string name, ProjectMetadataItemArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/projectMetadataItem:ProjectMetadataItem", name, args, MakeResourceOptions(options, ""))
        {
        }

        private ProjectMetadataItem(string name, Input<string> id, ProjectMetadataItemState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/projectMetadataItem:ProjectMetadataItem", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ProjectMetadataItem resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ProjectMetadataItem Get(string name, Input<string> id, ProjectMetadataItemState? state = null, CustomResourceOptions? options = null)
        {
            return new ProjectMetadataItem(name, id, state, options);
        }
    }

    public sealed class ProjectMetadataItemArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The metadata key to set.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs. If it
        /// is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The value to set for the given metadata key.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ProjectMetadataItemArgs()
        {
        }
    }

    public sealed class ProjectMetadataItemState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The metadata key to set.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs. If it
        /// is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The value to set for the given metadata key.
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public ProjectMetadataItemState()
        {
        }
    }
}
