// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Kms
{
    /// <summary>
    /// Allows creation and management of a single binding within IAM policy for
    /// an existing Google Cloud KMS crypto key.
    /// 
    /// &gt; **Note:** On create, this resource will overwrite members of any existing roles.
    ///     Use `import` and inspect the preview output to ensure
    ///     your existing members are preserved.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/kms_crypto_key_iam_binding.html.markdown.
    /// </summary>
    public partial class CryptoKeyIAMBinding : Pulumi.CustomResource
    {
        /// <summary>
        /// The crypto key ID, in the form
        /// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
        /// `{location_name}/{key_ring_name}/{crypto_key_name}`.
        /// In the second form, the provider's project setting will be used as a fallback.
        /// </summary>
        [Output("cryptoKeyId")]
        public Output<string> CryptoKeyId { get; private set; } = null!;

        /// <summary>
        /// (Computed) The etag of the crypto key's IAM policy.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// A list of users that the role should apply to. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
        /// </summary>
        [Output("members")]
        public Output<ImmutableArray<string>> Members { get; private set; } = null!;

        /// <summary>
        /// The role that should be applied. Only one
        /// `gcp.kms.CryptoKeyIAMBinding` can be used per role. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Output("role")]
        public Output<string> Role { get; private set; } = null!;


        /// <summary>
        /// Create a CryptoKeyIAMBinding resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CryptoKeyIAMBinding(string name, CryptoKeyIAMBindingArgs args, CustomResourceOptions? options = null)
            : base("gcp:kms/cryptoKeyIAMBinding:CryptoKeyIAMBinding", name, args, MakeResourceOptions(options, ""))
        {
        }

        private CryptoKeyIAMBinding(string name, Input<string> id, CryptoKeyIAMBindingState? state = null, CustomResourceOptions? options = null)
            : base("gcp:kms/cryptoKeyIAMBinding:CryptoKeyIAMBinding", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing CryptoKeyIAMBinding resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CryptoKeyIAMBinding Get(string name, Input<string> id, CryptoKeyIAMBindingState? state = null, CustomResourceOptions? options = null)
        {
            return new CryptoKeyIAMBinding(name, id, state, options);
        }
    }

    public sealed class CryptoKeyIAMBindingArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The crypto key ID, in the form
        /// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
        /// `{location_name}/{key_ring_name}/{crypto_key_name}`.
        /// In the second form, the provider's project setting will be used as a fallback.
        /// </summary>
        [Input("cryptoKeyId", required: true)]
        public Input<string> CryptoKeyId { get; set; } = null!;

        [Input("members", required: true)]
        private InputList<string>? _members;

        /// <summary>
        /// A list of users that the role should apply to. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
        /// </summary>
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        /// <summary>
        /// The role that should be applied. Only one
        /// `gcp.kms.CryptoKeyIAMBinding` can be used per role. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Input("role", required: true)]
        public Input<string> Role { get; set; } = null!;

        public CryptoKeyIAMBindingArgs()
        {
        }
    }

    public sealed class CryptoKeyIAMBindingState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The crypto key ID, in the form
        /// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
        /// `{location_name}/{key_ring_name}/{crypto_key_name}`.
        /// In the second form, the provider's project setting will be used as a fallback.
        /// </summary>
        [Input("cryptoKeyId")]
        public Input<string>? CryptoKeyId { get; set; }

        /// <summary>
        /// (Computed) The etag of the crypto key's IAM policy.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        [Input("members")]
        private InputList<string>? _members;

        /// <summary>
        /// A list of users that the role should apply to. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
        /// </summary>
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        /// <summary>
        /// The role that should be applied. Only one
        /// `gcp.kms.CryptoKeyIAMBinding` can be used per role. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        public CryptoKeyIAMBindingState()
        {
        }
    }
}
