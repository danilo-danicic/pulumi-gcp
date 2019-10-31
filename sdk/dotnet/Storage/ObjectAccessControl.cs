// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Storage
{
    /// <summary>
    /// The ObjectAccessControls resources represent the Access Control Lists
    /// (ACLs) for objects within Google Cloud Storage. ACLs let you specify
    /// who has access to your data and to what extent.
    /// 
    /// There are two roles that can be assigned to an entity:
    /// 
    /// READERs can get an object, though the acl property will not be revealed.
    /// OWNERs are READERs, and they can get the acl property, update an object,
    /// and call all objectAccessControls methods on the object. The owner of an
    /// object is always an OWNER.
    /// For more information, see Access Control, with the caveat that this API
    /// uses READER and OWNER instead of READ and FULL_CONTROL.
    /// 
    /// 
    /// To get more information about ObjectAccessControl, see:
    /// 
    /// * [API documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/storage/docs/access-control/create-manage-lists)
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/storage_object_access_control.html.markdown.
    /// </summary>
    public partial class ObjectAccessControl : Pulumi.CustomResource
    {
        [Output("bucket")]
        public Output<string> Bucket { get; private set; } = null!;

        [Output("domain")]
        public Output<string> Domain { get; private set; } = null!;

        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        [Output("entity")]
        public Output<string> Entity { get; private set; } = null!;

        [Output("entityId")]
        public Output<string> EntityId { get; private set; } = null!;

        [Output("generation")]
        public Output<int> Generation { get; private set; } = null!;

        [Output("object")]
        public Output<string> Object { get; private set; } = null!;

        [Output("projectTeam")]
        public Output<Outputs.ObjectAccessControlProjectTeam> ProjectTeam { get; private set; } = null!;

        [Output("role")]
        public Output<string> Role { get; private set; } = null!;


        /// <summary>
        /// Create a ObjectAccessControl resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ObjectAccessControl(string name, ObjectAccessControlArgs args, CustomResourceOptions? options = null)
            : base("gcp:storage/objectAccessControl:ObjectAccessControl", name, args, MakeResourceOptions(options, ""))
        {
        }

        private ObjectAccessControl(string name, Input<string> id, ObjectAccessControlState? state = null, CustomResourceOptions? options = null)
            : base("gcp:storage/objectAccessControl:ObjectAccessControl", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ObjectAccessControl resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ObjectAccessControl Get(string name, Input<string> id, ObjectAccessControlState? state = null, CustomResourceOptions? options = null)
        {
            return new ObjectAccessControl(name, id, state, options);
        }
    }

    public sealed class ObjectAccessControlArgs : Pulumi.ResourceArgs
    {
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        [Input("entity", required: true)]
        public Input<string> Entity { get; set; } = null!;

        [Input("object", required: true)]
        public Input<string> Object { get; set; } = null!;

        [Input("role", required: true)]
        public Input<string> Role { get; set; } = null!;

        public ObjectAccessControlArgs()
        {
        }
    }

    public sealed class ObjectAccessControlState : Pulumi.ResourceArgs
    {
        [Input("bucket")]
        public Input<string>? Bucket { get; set; }

        [Input("domain")]
        public Input<string>? Domain { get; set; }

        [Input("email")]
        public Input<string>? Email { get; set; }

        [Input("entity")]
        public Input<string>? Entity { get; set; }

        [Input("entityId")]
        public Input<string>? EntityId { get; set; }

        [Input("generation")]
        public Input<int>? Generation { get; set; }

        [Input("object")]
        public Input<string>? Object { get; set; }

        [Input("projectTeam")]
        public Input<Inputs.ObjectAccessControlProjectTeamGetArgs>? ProjectTeam { get; set; }

        [Input("role")]
        public Input<string>? Role { get; set; }

        public ObjectAccessControlState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class ObjectAccessControlProjectTeamGetArgs : Pulumi.ResourceArgs
    {
        [Input("projectNumber")]
        public Input<string>? ProjectNumber { get; set; }

        [Input("team")]
        public Input<string>? Team { get; set; }

        public ObjectAccessControlProjectTeamGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class ObjectAccessControlProjectTeam
    {
        public readonly string? ProjectNumber;
        public readonly string? Team;

        [OutputConstructor]
        private ObjectAccessControlProjectTeam(
            string? projectNumber,
            string? team)
        {
            ProjectNumber = projectNumber;
            Team = team;
        }
    }
    }
}
