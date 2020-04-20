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
    public sealed class RegionUrlMapPathMatcherPathRuleRouteAction
    {
        public readonly Outputs.RegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy? CorsPolicy;
        public readonly Outputs.RegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy? FaultInjectionPolicy;
        public readonly Outputs.RegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy? RequestMirrorPolicy;
        public readonly Outputs.RegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy? RetryPolicy;
        public readonly Outputs.RegionUrlMapPathMatcherPathRuleRouteActionTimeout? Timeout;
        public readonly Outputs.RegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite? UrlRewrite;
        public readonly ImmutableArray<Outputs.RegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendService> WeightedBackendServices;

        [OutputConstructor]
        private RegionUrlMapPathMatcherPathRuleRouteAction(
            Outputs.RegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy? corsPolicy,

            Outputs.RegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy? faultInjectionPolicy,

            Outputs.RegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy? requestMirrorPolicy,

            Outputs.RegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy? retryPolicy,

            Outputs.RegionUrlMapPathMatcherPathRuleRouteActionTimeout? timeout,

            Outputs.RegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite? urlRewrite,

            ImmutableArray<Outputs.RegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendService> weightedBackendServices)
        {
            CorsPolicy = corsPolicy;
            FaultInjectionPolicy = faultInjectionPolicy;
            RequestMirrorPolicy = requestMirrorPolicy;
            RetryPolicy = retryPolicy;
            Timeout = timeout;
            UrlRewrite = urlRewrite;
            WeightedBackendServices = weightedBackendServices;
        }
    }
}