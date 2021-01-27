// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CertificateAuthority.Outputs
{

    [OutputType]
    public sealed class AuthorityConfigReusableConfig
    {
        /// <summary>
        /// A resource path to a ReusableConfig in the format
        /// `projects/*/locations/*/reusableConfigs/*`.
        /// . Alternatively, one of the short names
        /// found by running `gcloud beta privateca reusable-configs list`.
        /// </summary>
        public readonly string ReusableConfig;

        [OutputConstructor]
        private AuthorityConfigReusableConfig(string reusableConfig)
        {
            ReusableConfig = reusableConfig;
        }
    }
}