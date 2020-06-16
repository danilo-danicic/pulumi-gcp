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
    public sealed class URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicy
    {
        /// <summary>
        /// The specification for how client requests are aborted as part of fault injection.  Structure is documented below.
        /// </summary>
        public readonly Outputs.URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyAbort? Abort;
        /// <summary>
        /// The specification for how client requests are delayed as part of fault injection, before being sent to a backend service.  Structure is documented below.
        /// </summary>
        public readonly Outputs.URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelay? Delay;

        [OutputConstructor]
        private URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicy(
            Outputs.URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyAbort? abort,

            Outputs.URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelay? delay)
        {
            Abort = abort;
            Delay = delay;
        }
    }
}
