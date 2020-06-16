// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class URLMapPathMatcherRouteRuleRouteActionGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The specification for allowing client side cross-origin requests. Please see
        /// [W3C Recommendation for Cross Origin Resource Sharing](https://www.w3.org/TR/cors/)  Structure is documented below.
        /// </summary>
        [Input("corsPolicy")]
        public Input<Inputs.URLMapPathMatcherRouteRuleRouteActionCorsPolicyGetArgs>? CorsPolicy { get; set; }

        /// <summary>
        /// The specification for fault injection introduced into traffic to test the resiliency of clients to backend service failure.
        /// As part of fault injection, when clients send requests to a backend service, delays can be introduced by Loadbalancer on a
        /// percentage of requests before sending those request to the backend service. Similarly requests from clients can be aborted
        /// by the Loadbalancer for a percentage of requests.
        /// timeout and retryPolicy will be ignored by clients that are configured with a faultInjectionPolicy.  Structure is documented below.
        /// </summary>
        [Input("faultInjectionPolicy")]
        public Input<Inputs.URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyGetArgs>? FaultInjectionPolicy { get; set; }

        /// <summary>
        /// Specifies the policy on how requests intended for the route's backends are shadowed to a separate mirrored backend service.
        /// Loadbalancer does not wait for responses from the shadow service. Prior to sending traffic to the shadow service,
        /// the host / authority header is suffixed with -shadow.  Structure is documented below.
        /// </summary>
        [Input("requestMirrorPolicy")]
        public Input<Inputs.URLMapPathMatcherRouteRuleRouteActionRequestMirrorPolicyGetArgs>? RequestMirrorPolicy { get; set; }

        /// <summary>
        /// Specifies the retry policy associated with this route.  Structure is documented below.
        /// </summary>
        [Input("retryPolicy")]
        public Input<Inputs.URLMapPathMatcherRouteRuleRouteActionRetryPolicyGetArgs>? RetryPolicy { get; set; }

        /// <summary>
        /// Specifies the timeout for the selected route. Timeout is computed from the time the request has been
        /// fully processed (i.e. end-of-stream) up until the response has been completely processed. Timeout includes all retries.
        /// If not specified, will use the largest timeout among all backend services associated with the route.  Structure is documented below.
        /// </summary>
        [Input("timeout")]
        public Input<Inputs.URLMapPathMatcherRouteRuleRouteActionTimeoutGetArgs>? Timeout { get; set; }

        /// <summary>
        /// The spec to modify the URL of the request, prior to forwarding the request to the matched service.  Structure is documented below.
        /// </summary>
        [Input("urlRewrite")]
        public Input<Inputs.URLMapPathMatcherRouteRuleRouteActionUrlRewriteGetArgs>? UrlRewrite { get; set; }

        [Input("weightedBackendServices")]
        private InputList<Inputs.URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceGetArgs>? _weightedBackendServices;

        /// <summary>
        /// A list of weighted backend services to send traffic to when a route match occurs.
        /// The weights determine the fraction of traffic that flows to their corresponding backend service.
        /// If all traffic needs to go to a single backend service, there must be one weightedBackendService
        /// with weight set to a non 0 number.
        /// Once a backendService is identified and before forwarding the request to the backend service,
        /// advanced routing actions like Url rewrites and header transformations are applied depending on
        /// additional settings specified in this HttpRouteAction.  Structure is documented below.
        /// </summary>
        public InputList<Inputs.URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceGetArgs> WeightedBackendServices
        {
            get => _weightedBackendServices ?? (_weightedBackendServices = new InputList<Inputs.URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceGetArgs>());
            set => _weightedBackendServices = value;
        }

        public URLMapPathMatcherRouteRuleRouteActionGetArgs()
        {
        }
    }
}
