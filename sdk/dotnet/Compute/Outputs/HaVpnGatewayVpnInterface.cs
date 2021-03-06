// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Outputs
{

    [OutputType]
    public sealed class HaVpnGatewayVpnInterface
    {
        /// <summary>
        /// an identifier for the resource with format `projects/{{project}}/regions/{{region}}/vpnGateways/{{name}}`
        /// </summary>
        public readonly int? Id;
        public readonly string? IpAddress;

        [OutputConstructor]
        private HaVpnGatewayVpnInterface(
            int? id,

            string? ipAddress)
        {
            Id = id;
            IpAddress = ipAddress;
        }
    }
}
