// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Iam
{
    public static class GetWorkloadIdentityPoolProvider
    {
        public static Task<GetWorkloadIdentityPoolProviderResult> InvokeAsync(GetWorkloadIdentityPoolProviderArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetWorkloadIdentityPoolProviderResult>("gcp:iam/getWorkloadIdentityPoolProvider:getWorkloadIdentityPoolProvider", args ?? new GetWorkloadIdentityPoolProviderArgs(), options.WithVersion());
    }


    public sealed class GetWorkloadIdentityPoolProviderArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The project in which the resource belongs. If it
        /// is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        /// <summary>
        /// The id of the pool which is the
        /// final component of the pool resource name.
        /// </summary>
        [Input("workloadIdentityPoolId", required: true)]
        public string WorkloadIdentityPoolId { get; set; } = null!;

        /// <summary>
        /// The id of the provider which is the
        /// final component of the resource name.
        /// </summary>
        [Input("workloadIdentityPoolProviderId", required: true)]
        public string WorkloadIdentityPoolProviderId { get; set; } = null!;

        public GetWorkloadIdentityPoolProviderArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetWorkloadIdentityPoolProviderResult
    {
        public readonly string AttributeCondition;
        public readonly ImmutableDictionary<string, string> AttributeMapping;
        public readonly ImmutableArray<Outputs.GetWorkloadIdentityPoolProviderAwResult> Aws;
        public readonly string Description;
        public readonly bool Disabled;
        public readonly string DisplayName;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly ImmutableArray<Outputs.GetWorkloadIdentityPoolProviderOidcResult> Oidcs;
        public readonly string? Project;
        public readonly string State;
        public readonly string WorkloadIdentityPoolId;
        public readonly string WorkloadIdentityPoolProviderId;

        [OutputConstructor]
        private GetWorkloadIdentityPoolProviderResult(
            string attributeCondition,

            ImmutableDictionary<string, string> attributeMapping,

            ImmutableArray<Outputs.GetWorkloadIdentityPoolProviderAwResult> aws,

            string description,

            bool disabled,

            string displayName,

            string id,

            string name,

            ImmutableArray<Outputs.GetWorkloadIdentityPoolProviderOidcResult> oidcs,

            string? project,

            string state,

            string workloadIdentityPoolId,

            string workloadIdentityPoolProviderId)
        {
            AttributeCondition = attributeCondition;
            AttributeMapping = attributeMapping;
            Aws = aws;
            Description = description;
            Disabled = disabled;
            DisplayName = displayName;
            Id = id;
            Name = name;
            Oidcs = oidcs;
            Project = project;
            State = state;
            WorkloadIdentityPoolId = workloadIdentityPoolId;
            WorkloadIdentityPoolProviderId = workloadIdentityPoolProviderId;
        }
    }
}