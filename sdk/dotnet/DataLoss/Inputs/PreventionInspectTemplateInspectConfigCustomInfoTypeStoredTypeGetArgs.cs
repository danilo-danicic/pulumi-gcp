// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.DataLoss.Inputs
{

    public sealed class PreventionInspectTemplateInspectConfigCustomInfoTypeStoredTypeGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Resource name of the requested StoredInfoType, for example `organizations/433245324/storedInfoTypes/432452342`
        /// or `projects/project-id/storedInfoTypes/432452342`.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public PreventionInspectTemplateInspectConfigCustomInfoTypeStoredTypeGetArgs()
        {
        }
    }
}
