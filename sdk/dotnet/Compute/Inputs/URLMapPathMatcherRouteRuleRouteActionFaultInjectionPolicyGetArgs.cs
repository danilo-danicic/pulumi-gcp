// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The specification for how client requests are aborted as part of fault injection.  Structure is documented below.
        /// </summary>
        [Input("abort")]
        public Input<Inputs.URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyAbortGetArgs>? Abort { get; set; }

        /// <summary>
        /// The specification for how client requests are delayed as part of fault injection, before being sent to a backend service.  Structure is documented below.
        /// </summary>
        [Input("delay")]
        public Input<Inputs.URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelayGetArgs>? Delay { get; set; }

        public URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyGetArgs()
        {
        }
    }
}
