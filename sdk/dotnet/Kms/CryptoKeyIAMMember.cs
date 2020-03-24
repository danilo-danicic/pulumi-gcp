// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Kms
{
    /// <summary>
    /// Three different resources help you manage your IAM policy for KMS crypto key. Each of these resources serves a different use case:
    /// 
    /// * `gcp.kms.CryptoKeyIAMPolicy`: Authoritative. Sets the IAM policy for the crypto key and replaces any existing policy already attached.
    /// * `gcp.kms.CryptoKeyIAMBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the crypto key are preserved.
    /// * `gcp.kms.CryptoKeyIAMMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the crypto key are preserved.
    /// 
    /// &gt; **Note:** `gcp.kms.CryptoKeyIAMPolicy` **cannot** be used in conjunction with `gcp.kms.CryptoKeyIAMBinding` and `gcp.kms.CryptoKeyIAMMember` or they will fight over what your policy should be.
    /// 
    /// &gt; **Note:** `gcp.kms.CryptoKeyIAMBinding` resources **can be** used in conjunction with `gcp.kms.CryptoKeyIAMMember` resources **only if** they do not grant privilege to the same role.
    /// 
    /// With IAM Conditions:
    /// 
    /// 
    /// With IAM Conditions:
    /// 
    /// 
    /// With IAM Conditions:
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_kms_crypto_key_iam.html.markdown.
    /// </summary>
    public partial class CryptoKeyIAMMember : Pulumi.CustomResource
    {
        /// <summary>
        /// An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
        /// Structure is documented below.
        /// </summary>
        [Output("condition")]
        public Output<Outputs.CryptoKeyIAMMemberCondition?> Condition { get; private set; } = null!;

        /// <summary>
        /// The crypto key ID, in the form
        /// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
        /// `{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
        /// the provider's project setting will be used as a fallback.
        /// </summary>
        [Output("cryptoKeyId")]
        public Output<string> CryptoKeyId { get; private set; } = null!;

        /// <summary>
        /// (Computed) The etag of the project's IAM policy.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        [Output("member")]
        public Output<string> Member { get; private set; } = null!;

        /// <summary>
        /// The role that should be applied. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Output("role")]
        public Output<string> Role { get; private set; } = null!;


        /// <summary>
        /// Create a CryptoKeyIAMMember resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CryptoKeyIAMMember(string name, CryptoKeyIAMMemberArgs args, CustomResourceOptions? options = null)
            : base("gcp:kms/cryptoKeyIAMMember:CryptoKeyIAMMember", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private CryptoKeyIAMMember(string name, Input<string> id, CryptoKeyIAMMemberState? state = null, CustomResourceOptions? options = null)
            : base("gcp:kms/cryptoKeyIAMMember:CryptoKeyIAMMember", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing CryptoKeyIAMMember resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CryptoKeyIAMMember Get(string name, Input<string> id, CryptoKeyIAMMemberState? state = null, CustomResourceOptions? options = null)
        {
            return new CryptoKeyIAMMember(name, id, state, options);
        }
    }

    public sealed class CryptoKeyIAMMemberArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
        /// Structure is documented below.
        /// </summary>
        [Input("condition")]
        public Input<Inputs.CryptoKeyIAMMemberConditionArgs>? Condition { get; set; }

        /// <summary>
        /// The crypto key ID, in the form
        /// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
        /// `{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
        /// the provider's project setting will be used as a fallback.
        /// </summary>
        [Input("cryptoKeyId", required: true)]
        public Input<string> CryptoKeyId { get; set; } = null!;

        [Input("member", required: true)]
        public Input<string> Member { get; set; } = null!;

        /// <summary>
        /// The role that should be applied. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Input("role", required: true)]
        public Input<string> Role { get; set; } = null!;

        public CryptoKeyIAMMemberArgs()
        {
        }
    }

    public sealed class CryptoKeyIAMMemberState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
        /// Structure is documented below.
        /// </summary>
        [Input("condition")]
        public Input<Inputs.CryptoKeyIAMMemberConditionGetArgs>? Condition { get; set; }

        /// <summary>
        /// The crypto key ID, in the form
        /// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
        /// `{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
        /// the provider's project setting will be used as a fallback.
        /// </summary>
        [Input("cryptoKeyId")]
        public Input<string>? CryptoKeyId { get; set; }

        /// <summary>
        /// (Computed) The etag of the project's IAM policy.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        [Input("member")]
        public Input<string>? Member { get; set; }

        /// <summary>
        /// The role that should be applied. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        public CryptoKeyIAMMemberState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class CryptoKeyIAMMemberConditionArgs : Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("expression", required: true)]
        public Input<string> Expression { get; set; } = null!;

        [Input("title", required: true)]
        public Input<string> Title { get; set; } = null!;

        public CryptoKeyIAMMemberConditionArgs()
        {
        }
    }

    public sealed class CryptoKeyIAMMemberConditionGetArgs : Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("expression", required: true)]
        public Input<string> Expression { get; set; } = null!;

        [Input("title", required: true)]
        public Input<string> Title { get; set; } = null!;

        public CryptoKeyIAMMemberConditionGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class CryptoKeyIAMMemberCondition
    {
        public readonly string? Description;
        public readonly string Expression;
        public readonly string Title;

        [OutputConstructor]
        private CryptoKeyIAMMemberCondition(
            string? description,
            string expression,
            string title)
        {
            Description = description;
            Expression = expression;
            Title = title;
        }
    }
    }
}
