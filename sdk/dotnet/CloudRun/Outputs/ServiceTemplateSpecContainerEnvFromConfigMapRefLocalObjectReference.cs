// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudRun.Outputs
{

    [OutputType]
    public sealed class ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReference
    {
        /// <summary>
        /// Name of the port.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReference(string name)
        {
            Name = name;
        }
    }
}
