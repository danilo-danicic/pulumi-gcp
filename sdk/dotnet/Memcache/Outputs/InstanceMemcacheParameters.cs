// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Memcache.Outputs
{

    [OutputType]
    public sealed class InstanceMemcacheParameters
    {
        /// <summary>
        /// -
        /// This is a unique ID associated with this set of parameters.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// User-defined set of parameters to use in the memcache process.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Params;

        [OutputConstructor]
        private InstanceMemcacheParameters(
            string? id,

            ImmutableDictionary<string, string>? @params)
        {
            Id = id;
            Params = @params;
        }
    }
}
