// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Container.Outputs
{

    [OutputType]
    public sealed class ClusterDatabaseEncryption
    {
        /// <summary>
        /// the key to use to encrypt/decrypt secrets.  See the [DatabaseEncryption definition](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#Cluster.DatabaseEncryption) for more information.
        /// </summary>
        public readonly string? KeyName;
        /// <summary>
        /// `ENCRYPTED` or `DECRYPTED`
        /// </summary>
        public readonly string State;

        [OutputConstructor]
        private ClusterDatabaseEncryption(
            string? keyName,

            string state)
        {
            KeyName = keyName;
            State = state;
        }
    }
}