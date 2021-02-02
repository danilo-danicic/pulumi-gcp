// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.RuntimeConfig
{
    public static class GetConfig
    {
        /// <summary>
        /// To get more information about RuntimeConfigs, see:
        /// 
        /// * [API documentation](https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs)
        /// * How-to Guides
        ///     * [Runtime Configurator Fundamentals](https://cloud.google.com/deployment-manager/runtime-configurator/)
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Gcp = Pulumi.Gcp;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var run_service = Output.Create(Gcp.RuntimeConfig.GetConfig.InvokeAsync(new Gcp.RuntimeConfig.GetConfigArgs
        ///         {
        ///             Name = "my-service",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetConfigResult> InvokeAsync(GetConfigArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetConfigResult>("gcp:runtimeconfig/getConfig:getConfig", args ?? new GetConfigArgs(), options.WithVersion());
    }


    public sealed class GetConfigArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Cloud Run Service.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The project in which the resource belongs. If it
        /// is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        public GetConfigArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetConfigResult
    {
        public readonly string Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly string? Project;

        [OutputConstructor]
        private GetConfigResult(
            string description,

            string id,

            string name,

            string? project)
        {
            Description = description;
            Id = id;
            Name = name;
            Project = project;
        }
    }
}
