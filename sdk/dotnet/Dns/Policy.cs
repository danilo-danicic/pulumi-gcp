// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Dns
{
    /// <summary>
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_policy.html.markdown.
    /// </summary>
    public partial class Policy : Pulumi.CustomResource
    {
        [Output("alternativeNameServerConfig")]
        public Output<Outputs.PolicyAlternativeNameServerConfig?> AlternativeNameServerConfig { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("enableInboundForwarding")]
        public Output<bool?> EnableInboundForwarding { get; private set; } = null!;

        [Output("enableLogging")]
        public Output<bool?> EnableLogging { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("networks")]
        public Output<ImmutableArray<Outputs.PolicyNetworks>> Networks { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;


        /// <summary>
        /// Create a Policy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Policy(string name, PolicyArgs? args = null, CustomResourceOptions? options = null)
            : base("gcp:dns/policy:Policy", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Policy(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null)
            : base("gcp:dns/policy:Policy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Policy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Policy Get(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new Policy(name, id, state, options);
        }
    }

    public sealed class PolicyArgs : Pulumi.ResourceArgs
    {
        [Input("alternativeNameServerConfig")]
        public Input<Inputs.PolicyAlternativeNameServerConfigArgs>? AlternativeNameServerConfig { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("enableInboundForwarding")]
        public Input<bool>? EnableInboundForwarding { get; set; }

        [Input("enableLogging")]
        public Input<bool>? EnableLogging { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networks")]
        private InputList<Inputs.PolicyNetworksArgs>? _networks;
        public InputList<Inputs.PolicyNetworksArgs> Networks
        {
            get => _networks ?? (_networks = new InputList<Inputs.PolicyNetworksArgs>());
            set => _networks = value;
        }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        public PolicyArgs()
        {
        }
    }

    public sealed class PolicyState : Pulumi.ResourceArgs
    {
        [Input("alternativeNameServerConfig")]
        public Input<Inputs.PolicyAlternativeNameServerConfigGetArgs>? AlternativeNameServerConfig { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("enableInboundForwarding")]
        public Input<bool>? EnableInboundForwarding { get; set; }

        [Input("enableLogging")]
        public Input<bool>? EnableLogging { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networks")]
        private InputList<Inputs.PolicyNetworksGetArgs>? _networks;
        public InputList<Inputs.PolicyNetworksGetArgs> Networks
        {
            get => _networks ?? (_networks = new InputList<Inputs.PolicyNetworksGetArgs>());
            set => _networks = value;
        }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        public PolicyState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class PolicyAlternativeNameServerConfigArgs : Pulumi.ResourceArgs
    {
        [Input("targetNameServers")]
        private InputList<PolicyAlternativeNameServerConfigTargetNameServersArgs>? _targetNameServers;
        public InputList<PolicyAlternativeNameServerConfigTargetNameServersArgs> TargetNameServers
        {
            get => _targetNameServers ?? (_targetNameServers = new InputList<PolicyAlternativeNameServerConfigTargetNameServersArgs>());
            set => _targetNameServers = value;
        }

        public PolicyAlternativeNameServerConfigArgs()
        {
        }
    }

    public sealed class PolicyAlternativeNameServerConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("targetNameServers")]
        private InputList<PolicyAlternativeNameServerConfigTargetNameServersGetArgs>? _targetNameServers;
        public InputList<PolicyAlternativeNameServerConfigTargetNameServersGetArgs> TargetNameServers
        {
            get => _targetNameServers ?? (_targetNameServers = new InputList<PolicyAlternativeNameServerConfigTargetNameServersGetArgs>());
            set => _targetNameServers = value;
        }

        public PolicyAlternativeNameServerConfigGetArgs()
        {
        }
    }

    public sealed class PolicyAlternativeNameServerConfigTargetNameServersArgs : Pulumi.ResourceArgs
    {
        [Input("ipv4Address")]
        public Input<string>? Ipv4Address { get; set; }

        public PolicyAlternativeNameServerConfigTargetNameServersArgs()
        {
        }
    }

    public sealed class PolicyAlternativeNameServerConfigTargetNameServersGetArgs : Pulumi.ResourceArgs
    {
        [Input("ipv4Address")]
        public Input<string>? Ipv4Address { get; set; }

        public PolicyAlternativeNameServerConfigTargetNameServersGetArgs()
        {
        }
    }

    public sealed class PolicyNetworksArgs : Pulumi.ResourceArgs
    {
        [Input("networkUrl")]
        public Input<string>? NetworkUrl { get; set; }

        public PolicyNetworksArgs()
        {
        }
    }

    public sealed class PolicyNetworksGetArgs : Pulumi.ResourceArgs
    {
        [Input("networkUrl")]
        public Input<string>? NetworkUrl { get; set; }

        public PolicyNetworksGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class PolicyAlternativeNameServerConfig
    {
        public readonly ImmutableArray<PolicyAlternativeNameServerConfigTargetNameServers> TargetNameServers;

        [OutputConstructor]
        private PolicyAlternativeNameServerConfig(ImmutableArray<PolicyAlternativeNameServerConfigTargetNameServers> targetNameServers)
        {
            TargetNameServers = targetNameServers;
        }
    }

    [OutputType]
    public sealed class PolicyAlternativeNameServerConfigTargetNameServers
    {
        public readonly string? Ipv4Address;

        [OutputConstructor]
        private PolicyAlternativeNameServerConfigTargetNameServers(string? ipv4Address)
        {
            Ipv4Address = ipv4Address;
        }
    }

    [OutputType]
    public sealed class PolicyNetworks
    {
        public readonly string? NetworkUrl;

        [OutputConstructor]
        private PolicyNetworks(string? networkUrl)
        {
            NetworkUrl = networkUrl;
        }
    }
    }
}
