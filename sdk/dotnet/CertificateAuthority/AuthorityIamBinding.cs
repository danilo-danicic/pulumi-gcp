// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CertificateAuthority
{
    [GcpResourceType("gcp:certificateauthority/authorityIamBinding:AuthorityIamBinding")]
    public partial class AuthorityIamBinding : Pulumi.CustomResource
    {
        [Output("certificateAuthority")]
        public Output<string> CertificateAuthority { get; private set; } = null!;

        [Output("condition")]
        public Output<Outputs.AuthorityIamBindingCondition?> Condition { get; private set; } = null!;

        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        [Output("members")]
        public Output<ImmutableArray<string>> Members { get; private set; } = null!;

        [Output("role")]
        public Output<string> Role { get; private set; } = null!;


        /// <summary>
        /// Create a AuthorityIamBinding resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AuthorityIamBinding(string name, AuthorityIamBindingArgs args, CustomResourceOptions? options = null)
            : base("gcp:certificateauthority/authorityIamBinding:AuthorityIamBinding", name, args ?? new AuthorityIamBindingArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AuthorityIamBinding(string name, Input<string> id, AuthorityIamBindingState? state = null, CustomResourceOptions? options = null)
            : base("gcp:certificateauthority/authorityIamBinding:AuthorityIamBinding", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AuthorityIamBinding resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AuthorityIamBinding Get(string name, Input<string> id, AuthorityIamBindingState? state = null, CustomResourceOptions? options = null)
        {
            return new AuthorityIamBinding(name, id, state, options);
        }
    }

    public sealed class AuthorityIamBindingArgs : Pulumi.ResourceArgs
    {
        [Input("certificateAuthority", required: true)]
        public Input<string> CertificateAuthority { get; set; } = null!;

        [Input("condition")]
        public Input<Inputs.AuthorityIamBindingConditionArgs>? Condition { get; set; }

        [Input("members", required: true)]
        private InputList<string>? _members;
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        [Input("role", required: true)]
        public Input<string> Role { get; set; } = null!;

        public AuthorityIamBindingArgs()
        {
        }
    }

    public sealed class AuthorityIamBindingState : Pulumi.ResourceArgs
    {
        [Input("certificateAuthority")]
        public Input<string>? CertificateAuthority { get; set; }

        [Input("condition")]
        public Input<Inputs.AuthorityIamBindingConditionGetArgs>? Condition { get; set; }

        [Input("etag")]
        public Input<string>? Etag { get; set; }

        [Input("members")]
        private InputList<string>? _members;
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        [Input("role")]
        public Input<string>? Role { get; set; }

        public AuthorityIamBindingState()
        {
        }
    }
}
