// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    /// <summary>
    /// Enables the Google Compute Engine
    /// [Shared VPC](https://cloud.google.com/compute/docs/shared-vpc)
    /// feature for a project, assigning it as a Shared VPC host project.
    /// 
    /// For more information, see,
    /// [the Project API documentation](https://cloud.google.com/compute/docs/reference/latest/projects),
    /// where the Shared VPC feature is referred to by its former name "XPN".
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_shared_vpc_host_project.html.markdown.
    /// </summary>
    public partial class SharedVPCHostProject : Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the project that will serve as a Shared VPC host project
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;


        /// <summary>
        /// Create a SharedVPCHostProject resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SharedVPCHostProject(string name, SharedVPCHostProjectArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/sharedVPCHostProject:SharedVPCHostProject", name, args, MakeResourceOptions(options, ""))
        {
        }

        private SharedVPCHostProject(string name, Input<string> id, SharedVPCHostProjectState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/sharedVPCHostProject:SharedVPCHostProject", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SharedVPCHostProject resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SharedVPCHostProject Get(string name, Input<string> id, SharedVPCHostProjectState? state = null, CustomResourceOptions? options = null)
        {
            return new SharedVPCHostProject(name, id, state, options);
        }
    }

    public sealed class SharedVPCHostProjectArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the project that will serve as a Shared VPC host project
        /// </summary>
        [Input("project", required: true)]
        public Input<string> Project { get; set; } = null!;

        public SharedVPCHostProjectArgs()
        {
        }
    }

    public sealed class SharedVPCHostProjectState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the project that will serve as a Shared VPC host project
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        public SharedVPCHostProjectState()
        {
        }
    }
}
