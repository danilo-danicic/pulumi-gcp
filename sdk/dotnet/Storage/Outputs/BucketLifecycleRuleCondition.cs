// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Storage.Outputs
{

    [OutputType]
    public sealed class BucketLifecycleRuleCondition
    {
        /// <summary>
        /// Minimum age of an object in days to satisfy this condition.
        /// </summary>
        public readonly int? Age;
        /// <summary>
        /// Creation date of an object in RFC 3339 (e.g. `2017-06-13`) to satisfy this condition.
        /// </summary>
        public readonly string? CreatedBefore;
        /// <summary>
        /// Creation date of an object in RFC 3339 (e.g. `2017-06-13`) to satisfy this condition.
        /// </summary>
        public readonly string? CustomTimeBefore;
        /// <summary>
        /// Date in RFC 3339 (e.g. `2017-06-13`) when an object's Custom-Time metadata is earlier than the date specified in this condition.
        /// </summary>
        public readonly int? DaysSinceCustomTime;
        /// <summary>
        /// Relevant only for versioned objects. Number of days elapsed since the noncurrent timestamp of an object.
        /// </summary>
        public readonly int? DaysSinceNoncurrentTime;
        /// <summary>
        /// [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects to satisfy this condition. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `ARCHIVE`, `STANDARD`, `DURABLE_REDUCED_AVAILABILITY`.
        /// </summary>
        public readonly ImmutableArray<string> MatchesStorageClasses;
        /// <summary>
        /// Relevant only for versioned objects. The date in RFC 3339 (e.g. `2017-06-13`) when the object became nonconcurrent.
        /// </summary>
        public readonly string? NoncurrentTimeBefore;
        /// <summary>
        /// Relevant only for versioned objects. The number of newer versions of an object to satisfy this condition.
        /// </summary>
        public readonly int? NumNewerVersions;
        /// <summary>
        /// Match to live and/or archived objects. Unversioned buckets have only live objects. Supported values include: `"LIVE"`, `"ARCHIVED"`, `"ANY"`.
        /// </summary>
        public readonly string? WithState;

        [OutputConstructor]
        private BucketLifecycleRuleCondition(
            int? age,

            string? createdBefore,

            string? customTimeBefore,

            int? daysSinceCustomTime,

            int? daysSinceNoncurrentTime,

            ImmutableArray<string> matchesStorageClasses,

            string? noncurrentTimeBefore,

            int? numNewerVersions,

            string? withState)
        {
            Age = age;
            CreatedBefore = createdBefore;
            CustomTimeBefore = customTimeBefore;
            DaysSinceCustomTime = daysSinceCustomTime;
            DaysSinceNoncurrentTime = daysSinceNoncurrentTime;
            MatchesStorageClasses = matchesStorageClasses;
            NoncurrentTimeBefore = noncurrentTimeBefore;
            NumNewerVersions = numNewerVersions;
            WithState = withState;
        }
    }
}
