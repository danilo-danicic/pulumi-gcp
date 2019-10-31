// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Tpu
{
    /// <summary>
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/tpu_node.html.markdown.
    /// </summary>
    public partial class Node : Pulumi.CustomResource
    {
        [Output("acceleratorType")]
        public Output<string> AcceleratorType { get; private set; } = null!;

        [Output("cidrBlock")]
        public Output<string> CidrBlock { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("network")]
        public Output<string> Network { get; private set; } = null!;

        [Output("networkEndpoints")]
        public Output<ImmutableArray<Outputs.NodeNetworkEndpoints>> NetworkEndpoints { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        [Output("schedulingConfig")]
        public Output<Outputs.NodeSchedulingConfig?> SchedulingConfig { get; private set; } = null!;

        [Output("serviceAccount")]
        public Output<string> ServiceAccount { get; private set; } = null!;

        [Output("tensorflowVersion")]
        public Output<string> TensorflowVersion { get; private set; } = null!;

        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a Node resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Node(string name, NodeArgs args, CustomResourceOptions? options = null)
            : base("gcp:tpu/node:Node", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Node(string name, Input<string> id, NodeState? state = null, CustomResourceOptions? options = null)
            : base("gcp:tpu/node:Node", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Node resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Node Get(string name, Input<string> id, NodeState? state = null, CustomResourceOptions? options = null)
        {
            return new Node(name, id, state, options);
        }
    }

    public sealed class NodeArgs : Pulumi.ResourceArgs
    {
        [Input("acceleratorType", required: true)]
        public Input<string> AcceleratorType { get; set; } = null!;

        [Input("cidrBlock", required: true)]
        public Input<string> CidrBlock { get; set; } = null!;

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("network")]
        public Input<string>? Network { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("schedulingConfig")]
        public Input<Inputs.NodeSchedulingConfigArgs>? SchedulingConfig { get; set; }

        [Input("tensorflowVersion", required: true)]
        public Input<string> TensorflowVersion { get; set; } = null!;

        [Input("zone", required: true)]
        public Input<string> Zone { get; set; } = null!;

        public NodeArgs()
        {
        }
    }

    public sealed class NodeState : Pulumi.ResourceArgs
    {
        [Input("acceleratorType")]
        public Input<string>? AcceleratorType { get; set; }

        [Input("cidrBlock")]
        public Input<string>? CidrBlock { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("network")]
        public Input<string>? Network { get; set; }

        [Input("networkEndpoints")]
        private InputList<Inputs.NodeNetworkEndpointsGetArgs>? _networkEndpoints;
        public InputList<Inputs.NodeNetworkEndpointsGetArgs> NetworkEndpoints
        {
            get => _networkEndpoints ?? (_networkEndpoints = new InputList<Inputs.NodeNetworkEndpointsGetArgs>());
            set => _networkEndpoints = value;
        }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("schedulingConfig")]
        public Input<Inputs.NodeSchedulingConfigGetArgs>? SchedulingConfig { get; set; }

        [Input("serviceAccount")]
        public Input<string>? ServiceAccount { get; set; }

        [Input("tensorflowVersion")]
        public Input<string>? TensorflowVersion { get; set; }

        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public NodeState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class NodeNetworkEndpointsGetArgs : Pulumi.ResourceArgs
    {
        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        [Input("port")]
        public Input<int>? Port { get; set; }

        public NodeNetworkEndpointsGetArgs()
        {
        }
    }

    public sealed class NodeSchedulingConfigArgs : Pulumi.ResourceArgs
    {
        [Input("preemptible")]
        public Input<bool>? Preemptible { get; set; }

        public NodeSchedulingConfigArgs()
        {
        }
    }

    public sealed class NodeSchedulingConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("preemptible")]
        public Input<bool>? Preemptible { get; set; }

        public NodeSchedulingConfigGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class NodeNetworkEndpoints
    {
        public readonly string IpAddress;
        public readonly int Port;

        [OutputConstructor]
        private NodeNetworkEndpoints(
            string ipAddress,
            int port)
        {
            IpAddress = ipAddress;
            Port = port;
        }
    }

    [OutputType]
    public sealed class NodeSchedulingConfig
    {
        public readonly bool? Preemptible;

        [OutputConstructor]
        private NodeSchedulingConfig(bool? preemptible)
        {
            Preemptible = preemptible;
        }
    }
    }
}
