// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.NetworkManagement.Inputs
{

    public sealed class ConnectivityTestSourceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A Compute Engine instance URI.
        /// </summary>
        [Input("instance")]
        public Input<string>? Instance { get; set; }

        /// <summary>
        /// The IP address of the endpoint, which can be an external or
        /// internal IP. An IPv6 address is only allowed when the test's
        /// destination is a global load balancer VIP.
        /// </summary>
        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        /// <summary>
        /// A Compute Engine network URI.
        /// </summary>
        [Input("network")]
        public Input<string>? Network { get; set; }

        /// <summary>
        /// Type of the network where the endpoint is located.
        /// </summary>
        [Input("networkType")]
        public Input<string>? NetworkType { get; set; }

        /// <summary>
        /// The IP protocol port of the endpoint. Only applicable when
        /// protocol is TCP or UDP.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// Project ID where the endpoint is located. The Project ID can be
        /// derived from the URI if you provide a VM instance or network URI.
        /// The following are two cases where you must provide the project ID:
        /// 1. Only the IP address is specified, and the IP address is within
        /// a GCP project. 2. When you are using Shared VPC and the IP address
        /// that you provide is from the service project. In this case, the
        /// network that the IP address resides in is defined in the host
        /// project.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        public ConnectivityTestSourceArgs()
        {
        }
    }
}
