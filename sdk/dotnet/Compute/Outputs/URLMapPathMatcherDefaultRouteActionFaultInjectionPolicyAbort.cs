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
    public sealed class URLMapPathMatcherDefaultRouteActionFaultInjectionPolicyAbort
    {
        /// <summary>
        /// The HTTP status code used to abort the request.
        /// The value must be between 200 and 599 inclusive.
        /// </summary>
        public readonly int? HttpStatus;
        /// <summary>
        /// The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection.
        /// The value must be between 0.0 and 100.0 inclusive.
        /// </summary>
        public readonly double? Percentage;

        [OutputConstructor]
        private URLMapPathMatcherDefaultRouteActionFaultInjectionPolicyAbort(
            int? httpStatus,

            double? percentage)
        {
            HttpStatus = httpStatus;
            Percentage = percentage;
        }
    }
}
