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
    /// ## Import
    /// 
    /// For all import syntaxes, the "resource in question" can take any of the following forms* projects/{{project}}/regions/{{region}}/subnetworks/{{name}} * {{project}}/{{region}}/{{name}} * {{region}}/{{name}} * {{name}} Any variables not passed in the import command will be taken from the provider configuration. Compute Engine subnetwork IAM resources can be imported using the resource identifiers, role, and member. IAM member imports use space-delimited identifiersthe resource in question, the role, and the member identity, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import gcp:compute/subnetworkIAMMember:SubnetworkIAMMember editor "projects/{{project}}/regions/{{region}}/subnetworks/{{subnetwork}} roles/compute.networkUser user:jane@example.com"
    /// ```
    /// 
    ///  IAM binding imports use space-delimited identifiersthe resource in question and the role, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import gcp:compute/subnetworkIAMMember:SubnetworkIAMMember editor "projects/{{project}}/regions/{{region}}/subnetworks/{{subnetwork}} roles/compute.networkUser"
    /// ```
    /// 
    ///  IAM policy imports use the identifier of the resource in question, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import gcp:compute/subnetworkIAMMember:SubnetworkIAMMember editor projects/{{project}}/regions/{{region}}/subnetworks/{{subnetwork}}
    /// ```
    /// 
    ///  -&gt; **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the
    /// 
    /// full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.
    /// </summary>
    [GcpResourceType("gcp:compute/subnetworkIAMMember:SubnetworkIAMMember")]
    public partial class SubnetworkIAMMember : Pulumi.CustomResource
    {
        /// <summary>
        /// ) An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
        /// Structure is documented below.
        /// </summary>
        [Output("condition")]
        public Output<Outputs.SubnetworkIAMMemberCondition?> Condition { get; private set; } = null!;

        /// <summary>
        /// (Computed) The etag of the IAM policy.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        [Output("member")]
        public Output<string> Member { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The GCP region for this subnetwork.
        /// Used to find the parent resource to bind the IAM policy to. If not specified,
        /// the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
        /// region is specified, it is taken from the provider configuration.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The role that should be applied. Only one
        /// `gcp.compute.SubnetworkIAMBinding` can be used per role. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Output("role")]
        public Output<string> Role { get; private set; } = null!;

        /// <summary>
        /// Used to find the parent resource to bind the IAM policy to
        /// </summary>
        [Output("subnetwork")]
        public Output<string> Subnetwork { get; private set; } = null!;


        /// <summary>
        /// Create a SubnetworkIAMMember resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SubnetworkIAMMember(string name, SubnetworkIAMMemberArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/subnetworkIAMMember:SubnetworkIAMMember", name, args ?? new SubnetworkIAMMemberArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SubnetworkIAMMember(string name, Input<string> id, SubnetworkIAMMemberState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/subnetworkIAMMember:SubnetworkIAMMember", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SubnetworkIAMMember resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SubnetworkIAMMember Get(string name, Input<string> id, SubnetworkIAMMemberState? state = null, CustomResourceOptions? options = null)
        {
            return new SubnetworkIAMMember(name, id, state, options);
        }
    }

    public sealed class SubnetworkIAMMemberArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ) An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
        /// Structure is documented below.
        /// </summary>
        [Input("condition")]
        public Input<Inputs.SubnetworkIAMMemberConditionArgs>? Condition { get; set; }

        [Input("member", required: true)]
        public Input<string> Member { get; set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The GCP region for this subnetwork.
        /// Used to find the parent resource to bind the IAM policy to. If not specified,
        /// the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
        /// region is specified, it is taken from the provider configuration.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The role that should be applied. Only one
        /// `gcp.compute.SubnetworkIAMBinding` can be used per role. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Input("role", required: true)]
        public Input<string> Role { get; set; } = null!;

        /// <summary>
        /// Used to find the parent resource to bind the IAM policy to
        /// </summary>
        [Input("subnetwork", required: true)]
        public Input<string> Subnetwork { get; set; } = null!;

        public SubnetworkIAMMemberArgs()
        {
        }
    }

    public sealed class SubnetworkIAMMemberState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ) An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
        /// Structure is documented below.
        /// </summary>
        [Input("condition")]
        public Input<Inputs.SubnetworkIAMMemberConditionGetArgs>? Condition { get; set; }

        /// <summary>
        /// (Computed) The etag of the IAM policy.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        [Input("member")]
        public Input<string>? Member { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The GCP region for this subnetwork.
        /// Used to find the parent resource to bind the IAM policy to. If not specified,
        /// the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
        /// region is specified, it is taken from the provider configuration.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The role that should be applied. Only one
        /// `gcp.compute.SubnetworkIAMBinding` can be used per role. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        /// <summary>
        /// Used to find the parent resource to bind the IAM policy to
        /// </summary>
        [Input("subnetwork")]
        public Input<string>? Subnetwork { get; set; }

        public SubnetworkIAMMemberState()
        {
        }
    }
}
