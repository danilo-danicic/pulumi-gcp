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
    public sealed class URLMapPathMatcherPathRuleRouteActionRetryPolicy
    {
        /// <summary>
        /// Specifies the allowed number retries. This number must be &gt; 0. If not specified, defaults to 1.
        /// </summary>
        public readonly int? NumRetries;
        /// <summary>
        /// Specifies a non-zero timeout per retry attempt.
        /// If not specified, will use the timeout set in HttpRouteAction. If timeout in HttpRouteAction is not set,
        /// will use the largest timeout among all backend services associated with the route.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.URLMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout? PerTryTimeout;
        /// <summary>
        /// Specfies one or more conditions when this retry rule applies. Valid values are:
        /// * 5xx: Loadbalancer will attempt a retry if the backend service responds with any 5xx response code,
        /// or if the backend service does not respond at all, example: disconnects, reset, read timeout,
        /// * connection failure, and refused streams.
        /// * gateway-error: Similar to 5xx, but only applies to response codes 502, 503 or 504.
        /// * connect-failure: Loadbalancer will retry on failures connecting to backend services,
        /// for example due to connection timeouts.
        /// * retriable-4xx: Loadbalancer will retry for retriable 4xx response codes.
        /// Currently the only retriable error supported is 409.
        /// * refused-stream:Loadbalancer will retry if the backend service resets the stream with a REFUSED_STREAM error code.
        /// This reset type indicates that it is safe to retry.
        /// * cancelled: Loadbalancer will retry if the gRPC status code in the response header is set to cancelled
        /// * deadline-exceeded: Loadbalancer will retry if the gRPC status code in the response header is set to deadline-exceeded
        /// * resource-exhausted: Loadbalancer will retry if the gRPC status code in the response header is set to resource-exhausted
        /// * unavailable: Loadbalancer will retry if the gRPC status code in the response header is set to unavailable
        /// </summary>
        public readonly ImmutableArray<string> RetryConditions;

        [OutputConstructor]
        private URLMapPathMatcherPathRuleRouteActionRetryPolicy(
            int? numRetries,

            Outputs.URLMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout? perTryTimeout,

            ImmutableArray<string> retryConditions)
        {
            NumRetries = numRetries;
            PerTryTimeout = perTryTimeout;
            RetryConditions = retryConditions;
        }
    }
}
