// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AccessContextManager.Outputs
{

    [OutputType]
    public sealed class AccessLevelConditionDevicePolicy
    {
        /// <summary>
        /// A list of allowed device management levels.
        /// An empty list allows all management levels.
        /// Each value may be one of `MANAGEMENT_UNSPECIFIED`, `NONE`, `BASIC`, and `COMPLETE`.
        /// </summary>
        public readonly ImmutableArray<string> AllowedDeviceManagementLevels;
        /// <summary>
        /// A list of allowed encryptions statuses.
        /// An empty list allows all statuses.
        /// Each value may be one of `ENCRYPTION_UNSPECIFIED`, `ENCRYPTION_UNSUPPORTED`, `UNENCRYPTED`, and `ENCRYPTED`.
        /// </summary>
        public readonly ImmutableArray<string> AllowedEncryptionStatuses;
        /// <summary>
        /// A list of allowed OS versions.
        /// An empty list allows all types and all versions.
        /// Structure is documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.AccessLevelConditionDevicePolicyOsConstraint> OsConstraints;
        /// <summary>
        /// Whether the device needs to be approved by the customer admin.
        /// </summary>
        public readonly bool? RequireAdminApproval;
        /// <summary>
        /// Whether the device needs to be corp owned.
        /// </summary>
        public readonly bool? RequireCorpOwned;
        /// <summary>
        /// Whether or not screenlock is required for the DevicePolicy
        /// to be true. Defaults to false.
        /// </summary>
        public readonly bool? RequireScreenLock;

        [OutputConstructor]
        private AccessLevelConditionDevicePolicy(
            ImmutableArray<string> allowedDeviceManagementLevels,

            ImmutableArray<string> allowedEncryptionStatuses,

            ImmutableArray<Outputs.AccessLevelConditionDevicePolicyOsConstraint> osConstraints,

            bool? requireAdminApproval,

            bool? requireCorpOwned,

            bool? requireScreenLock)
        {
            AllowedDeviceManagementLevels = allowedDeviceManagementLevels;
            AllowedEncryptionStatuses = allowedEncryptionStatuses;
            OsConstraints = osConstraints;
            RequireAdminApproval = requireAdminApproval;
            RequireCorpOwned = requireCorpOwned;
            RequireScreenLock = requireScreenLock;
        }
    }
}
