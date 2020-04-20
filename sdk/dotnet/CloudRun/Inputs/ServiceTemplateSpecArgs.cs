// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudRun.Inputs
{

    public sealed class ServiceTemplateSpecArgs : Pulumi.ResourceArgs
    {
        [Input("containerConcurrency")]
        public Input<int>? ContainerConcurrency { get; set; }

        [Input("containers")]
        private InputList<Inputs.ServiceTemplateSpecContainerArgs>? _containers;
        public InputList<Inputs.ServiceTemplateSpecContainerArgs> Containers
        {
            get => _containers ?? (_containers = new InputList<Inputs.ServiceTemplateSpecContainerArgs>());
            set => _containers = value;
        }

        [Input("serviceAccountName")]
        public Input<string>? ServiceAccountName { get; set; }

        [Input("servingState")]
        public Input<string>? ServingState { get; set; }

        public ServiceTemplateSpecArgs()
        {
        }
    }
}