// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class URLMapPathMatcherRouteRuleArgs : Pulumi.ResourceArgs
    {
        [Input("headerAction")]
        public Input<Inputs.URLMapPathMatcherRouteRuleHeaderActionArgs>? HeaderAction { get; set; }

        [Input("matchRules")]
        private InputList<Inputs.URLMapPathMatcherRouteRuleMatchRuleArgs>? _matchRules;
        public InputList<Inputs.URLMapPathMatcherRouteRuleMatchRuleArgs> MatchRules
        {
            get => _matchRules ?? (_matchRules = new InputList<Inputs.URLMapPathMatcherRouteRuleMatchRuleArgs>());
            set => _matchRules = value;
        }

        [Input("priority", required: true)]
        public Input<int> Priority { get; set; } = null!;

        [Input("routeAction")]
        public Input<Inputs.URLMapPathMatcherRouteRuleRouteActionArgs>? RouteAction { get; set; }

        [Input("service")]
        public Input<string>? Service { get; set; }

        [Input("urlRedirect")]
        public Input<Inputs.URLMapPathMatcherRouteRuleUrlRedirectArgs>? UrlRedirect { get; set; }

        public URLMapPathMatcherRouteRuleArgs()
        {
        }
    }
}