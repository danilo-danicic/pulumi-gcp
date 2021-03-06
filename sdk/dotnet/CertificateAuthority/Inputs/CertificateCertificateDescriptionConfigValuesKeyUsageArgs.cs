// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CertificateAuthority.Inputs
{

    public sealed class CertificateCertificateDescriptionConfigValuesKeyUsageArgs : Pulumi.ResourceArgs
    {
        [Input("baseKeyUsage")]
        public Input<Inputs.CertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageArgs>? BaseKeyUsage { get; set; }

        [Input("extendedKeyUsage")]
        public Input<Inputs.CertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageArgs>? ExtendedKeyUsage { get; set; }

        [Input("unknownExtendedKeyUsages", required: true)]
        private InputList<Inputs.CertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsageArgs>? _unknownExtendedKeyUsages;
        public InputList<Inputs.CertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsageArgs> UnknownExtendedKeyUsages
        {
            get => _unknownExtendedKeyUsages ?? (_unknownExtendedKeyUsages = new InputList<Inputs.CertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsageArgs>());
            set => _unknownExtendedKeyUsages = value;
        }

        public CertificateCertificateDescriptionConfigValuesKeyUsageArgs()
        {
        }
    }
}
