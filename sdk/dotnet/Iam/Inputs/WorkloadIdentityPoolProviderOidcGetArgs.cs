// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Iam.Inputs
{

    public sealed class WorkloadIdentityPoolProviderOidcGetArgs : Pulumi.ResourceArgs
    {
        [Input("allowedAudiences")]
        private InputList<string>? _allowedAudiences;

        /// <summary>
        /// Acceptable values for the `aud` field (audience) in the OIDC token. Token exchange
        /// requests are rejected if the token audience does not match one of the configured
        /// values. Each audience may be at most 256 characters. A maximum of 10 audiences may
        /// be configured.
        /// If this list is empty, the OIDC token audience must be equal to the full canonical
        /// resource name of the WorkloadIdentityPoolProvider, with or without the HTTPS prefix.
        /// For example:
        /// ```csharp
        /// using Pulumi;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///     }
        /// 
        /// }
        /// ```
        /// </summary>
        public InputList<string> AllowedAudiences
        {
            get => _allowedAudiences ?? (_allowedAudiences = new InputList<string>());
            set => _allowedAudiences = value;
        }

        /// <summary>
        /// The OIDC issuer URL.
        /// </summary>
        [Input("issuerUri", required: true)]
        public Input<string> IssuerUri { get; set; } = null!;

        public WorkloadIdentityPoolProviderOidcGetArgs()
        {
        }
    }
}
