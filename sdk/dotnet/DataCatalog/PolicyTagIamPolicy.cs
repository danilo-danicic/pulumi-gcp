// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.DataCatalog
{
    public partial class PolicyTagIamPolicy : Pulumi.CustomResource
    {
        /// <summary>
        /// (Computed) The etag of the IAM policy.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// The policy data generated by
        /// a `gcp.organizations.getIAMPolicy` data source.
        /// </summary>
        [Output("policyData")]
        public Output<string> PolicyData { get; private set; } = null!;

        /// <summary>
        /// Used to find the parent resource to bind the IAM policy to
        /// </summary>
        [Output("policyTag")]
        public Output<string> PolicyTag { get; private set; } = null!;


        /// <summary>
        /// Create a PolicyTagIamPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PolicyTagIamPolicy(string name, PolicyTagIamPolicyArgs args, CustomResourceOptions? options = null)
            : base("gcp:datacatalog/policyTagIamPolicy:PolicyTagIamPolicy", name, args ?? new PolicyTagIamPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PolicyTagIamPolicy(string name, Input<string> id, PolicyTagIamPolicyState? state = null, CustomResourceOptions? options = null)
            : base("gcp:datacatalog/policyTagIamPolicy:PolicyTagIamPolicy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing PolicyTagIamPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PolicyTagIamPolicy Get(string name, Input<string> id, PolicyTagIamPolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new PolicyTagIamPolicy(name, id, state, options);
        }
    }

    public sealed class PolicyTagIamPolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The policy data generated by
        /// a `gcp.organizations.getIAMPolicy` data source.
        /// </summary>
        [Input("policyData", required: true)]
        public Input<string> PolicyData { get; set; } = null!;

        /// <summary>
        /// Used to find the parent resource to bind the IAM policy to
        /// </summary>
        [Input("policyTag", required: true)]
        public Input<string> PolicyTag { get; set; } = null!;

        public PolicyTagIamPolicyArgs()
        {
        }
    }

    public sealed class PolicyTagIamPolicyState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// (Computed) The etag of the IAM policy.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// The policy data generated by
        /// a `gcp.organizations.getIAMPolicy` data source.
        /// </summary>
        [Input("policyData")]
        public Input<string>? PolicyData { get; set; }

        /// <summary>
        /// Used to find the parent resource to bind the IAM policy to
        /// </summary>
        [Input("policyTag")]
        public Input<string>? PolicyTag { get; set; }

        public PolicyTagIamPolicyState()
        {
        }
    }
}
