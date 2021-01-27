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
    public sealed class AuthorityAccessUrl
    {
        public readonly string? CaCertificateAccessUrl;
        public readonly string? CrlAccessUrl;

        [OutputConstructor]
        private AuthorityAccessUrl(
            string? caCertificateAccessUrl,

            string? crlAccessUrl)
        {
            CaCertificateAccessUrl = caCertificateAccessUrl;
            CrlAccessUrl = crlAccessUrl;
        }
    }
}
