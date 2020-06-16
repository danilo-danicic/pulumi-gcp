// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Memcache.Inputs
{

    public sealed class InstanceMemcacheParametersGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// -
        /// This is a unique ID associated with this set of parameters.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("params")]
        private InputMap<string>? _params;

        /// <summary>
        /// User-defined set of parameters to use in the memcache process.
        /// </summary>
        public InputMap<string> Params
        {
            get => _params ?? (_params = new InputMap<string>());
            set => _params = value;
        }

        public InstanceMemcacheParametersGetArgs()
        {
        }
    }
}
