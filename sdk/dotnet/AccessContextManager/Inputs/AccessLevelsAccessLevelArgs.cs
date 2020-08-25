// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AccessContextManager.Inputs
{

    public sealed class AccessLevelsAccessLevelArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A set of predefined conditions for the access level and a combining function.
        /// Structure is documented below.
        /// </summary>
        [Input("basic")]
        public Input<Inputs.AccessLevelsAccessLevelBasicArgs>? Basic { get; set; }

        /// <summary>
        /// Custom access level conditions are set using the Cloud Common Expression Language to represent the necessary conditions for the level to apply to a request.
        /// See CEL spec at: https://github.com/google/cel-spec.
        /// Structure is documented below.
        /// </summary>
        [Input("custom")]
        public Input<Inputs.AccessLevelsAccessLevelCustomArgs>? Custom { get; set; }

        /// <summary>
        /// Description of the expression
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Resource name for the Access Level. The short_name component must begin
        /// with a letter and only include alphanumeric and '_'.
        /// Format: accessPolicies/{policy_id}/accessLevels/{short_name}
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Title for the expression, i.e. a short string describing its purpose.
        /// </summary>
        [Input("title", required: true)]
        public Input<string> Title { get; set; } = null!;

        public AccessLevelsAccessLevelArgs()
        {
        }
    }
}
