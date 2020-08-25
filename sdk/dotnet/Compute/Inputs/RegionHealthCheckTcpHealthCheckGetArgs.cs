// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class RegionHealthCheckTcpHealthCheckGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The port number for the health check request.
        /// Must be specified if portName and portSpecification are not set
        /// or if port_specification is USE_FIXED_PORT. Valid values are 1 through 65535.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// Port name as defined in InstanceGroup#NamedPort#name. If both port and
        /// port_name are defined, port takes precedence.
        /// </summary>
        [Input("portName")]
        public Input<string>? PortName { get; set; }

        /// <summary>
        /// Specifies how port is selected for health checking, can be one of the
        /// following values:
        /// * `USE_FIXED_PORT`: The port number in `port` is used for health checking.
        /// * `USE_NAMED_PORT`: The `portName` is used for health checking.
        /// * `USE_SERVING_PORT`: For NetworkEndpointGroup, the port specified for each
        /// network endpoint is used for health checking. For other backends, the
        /// port or named port specified in the Backend Service is used for health
        /// checking.
        /// If not specified, gRPC health check follows behavior specified in `port` and
        /// `portName` fields.
        /// Possible values are `USE_FIXED_PORT`, `USE_NAMED_PORT`, and `USE_SERVING_PORT`.
        /// </summary>
        [Input("portSpecification")]
        public Input<string>? PortSpecification { get; set; }

        /// <summary>
        /// Specifies the type of proxy header to append before sending data to the
        /// backend.
        /// Default value is `NONE`.
        /// Possible values are `NONE` and `PROXY_V1`.
        /// </summary>
        [Input("proxyHeader")]
        public Input<string>? ProxyHeader { get; set; }

        /// <summary>
        /// The application data to send once the SSL connection has been
        /// established (default value is empty). If both request and response are
        /// empty, the connection establishment alone will indicate health. The request
        /// data can only be ASCII.
        /// </summary>
        [Input("request")]
        public Input<string>? Request { get; set; }

        /// <summary>
        /// The bytes to match against the beginning of the response data. If left empty
        /// (the default value), any response will indicate health. The response data
        /// can only be ASCII.
        /// </summary>
        [Input("response")]
        public Input<string>? Response { get; set; }

        public RegionHealthCheckTcpHealthCheckGetArgs()
        {
        }
    }
}
