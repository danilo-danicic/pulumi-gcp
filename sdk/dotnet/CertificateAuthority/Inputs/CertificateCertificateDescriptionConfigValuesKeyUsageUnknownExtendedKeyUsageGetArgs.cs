// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CertificateAuthority.Inputs
{

    public sealed class CertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsageGetArgs : Pulumi.ResourceArgs
    {
        [Input("obectId", required: true)]
        public Input<Inputs.CertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsageObectIdGetArgs> ObectId { get; set; } = null!;

        public CertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsageGetArgs()
        {
        }
    }
}
