// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.GameServices
{
    /// <summary>
    /// A game server deployment resource.
    /// 
    /// To get more information about GameServerDeployment, see:
    /// 
    /// * [API documentation](https://cloud.google.com/game-servers/docs/reference/rest/v1beta/projects.locations.gameServerDeployments)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/game-servers/docs)
    /// 
    /// ## Example Usage
    /// 
    /// ### Game Service Deployment Basic
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Gcp = Pulumi.Gcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var @default = new Gcp.GameServices.GameServerDeployment("default", new Gcp.GameServices.GameServerDeploymentArgs
    ///         {
    ///             DeploymentId = "tf-test-deployment",
    ///             Description = "a deployment description",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class GameServerDeployment : Pulumi.CustomResource
    {
        /// <summary>
        /// A unique id for the deployment.
        /// </summary>
        [Output("deploymentId")]
        public Output<string> DeploymentId { get; private set; } = null!;

        /// <summary>
        /// Human readable description of the game server deployment.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The labels associated with this game server deployment. Each label is a
        /// key-value pair.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// Location of the Deployment.
        /// </summary>
        [Output("location")]
        public Output<string?> Location { get; private set; } = null!;

        /// <summary>
        /// The resource id of the game server deployment, eg:
        /// 'projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}'. For example,
        /// 'projects/my-project/locations/{location}/gameServerDeployments/my-deployment'.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;


        /// <summary>
        /// Create a GameServerDeployment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GameServerDeployment(string name, GameServerDeploymentArgs args, CustomResourceOptions? options = null)
            : base("gcp:gameservices/gameServerDeployment:GameServerDeployment", name, args ?? new GameServerDeploymentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GameServerDeployment(string name, Input<string> id, GameServerDeploymentState? state = null, CustomResourceOptions? options = null)
            : base("gcp:gameservices/gameServerDeployment:GameServerDeployment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing GameServerDeployment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GameServerDeployment Get(string name, Input<string> id, GameServerDeploymentState? state = null, CustomResourceOptions? options = null)
        {
            return new GameServerDeployment(name, id, state, options);
        }
    }

    public sealed class GameServerDeploymentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A unique id for the deployment.
        /// </summary>
        [Input("deploymentId", required: true)]
        public Input<string> DeploymentId { get; set; } = null!;

        /// <summary>
        /// Human readable description of the game server deployment.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// The labels associated with this game server deployment. Each label is a
        /// key-value pair.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// Location of the Deployment.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        public GameServerDeploymentArgs()
        {
        }
    }

    public sealed class GameServerDeploymentState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A unique id for the deployment.
        /// </summary>
        [Input("deploymentId")]
        public Input<string>? DeploymentId { get; set; }

        /// <summary>
        /// Human readable description of the game server deployment.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// The labels associated with this game server deployment. Each label is a
        /// key-value pair.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// Location of the Deployment.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The resource id of the game server deployment, eg:
        /// 'projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}'. For example,
        /// 'projects/my-project/locations/{location}/gameServerDeployments/my-deployment'.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        public GameServerDeploymentState()
        {
        }
    }
}
