// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Inputs
{

    public sealed class UptimeCheckConfigMonitoredResourceArgs : Pulumi.ResourceArgs
    {
        [Input("labels", required: true)]
        private InputMap<string>? _labels;
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public UptimeCheckConfigMonitoredResourceArgs()
        {
        }
    }
}