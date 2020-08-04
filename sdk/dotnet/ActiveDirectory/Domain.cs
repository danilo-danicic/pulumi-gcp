// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.ActiveDirectory
{
    /// <summary>
    /// Creates a Microsoft AD domain
    /// 
    /// To get more information about Domain, see:
    /// 
    /// * [API documentation](https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains)
    /// * How-to Guides
    ///     * [Managed Microsoft Active Directory Quickstart](https://cloud.google.com/managed-microsoft-ad/docs/quickstarts)
    /// 
    /// ## Example Usage
    /// </summary>
    public partial class Domain : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of delegated administrator account used to perform Active Directory operations.
        /// If not specified, setupadmin will be used.
        /// </summary>
        [Output("admin")]
        public Output<string?> Admin { get; private set; } = null!;

        /// <summary>
        /// The full names of the Google Compute Engine networks the domain instance is connected to. The domain is only available on networks listed in authorizedNetworks.
        /// If CIDR subnets overlap between networks, domain creation will fail.
        /// </summary>
        [Output("authorizedNetworks")]
        public Output<ImmutableArray<string>> AuthorizedNetworks { get; private set; } = null!;

        /// <summary>
        /// The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions,
        /// https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.
        /// </summary>
        [Output("domainName")]
        public Output<string> DomainName { get; private set; } = null!;

        /// <summary>
        /// The fully-qualified domain name of the exposed domain used by clients to connect to the service. Similar to what would
        /// be chosen for an Active Directory set up on an internal network.
        /// </summary>
        [Output("fqdn")]
        public Output<string> Fqdn { get; private set; } = null!;

        /// <summary>
        /// Resource labels that can contain user-provided metadata
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// Locations where domain needs to be provisioned. [regions][compute/docs/regions-zones/]
        /// e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block.
        /// </summary>
        [Output("locations")]
        public Output<ImmutableArray<string>> Locations { get; private set; } = null!;

        /// <summary>
        /// The unique name of the domain using the format: 'projects/{project}/locations/global/domains/{domainName}'.
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
        /// The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger.
        /// Ranges must be unique and non-overlapping with existing subnets in authorizedNetworks
        /// </summary>
        [Output("reservedIpRange")]
        public Output<string> ReservedIpRange { get; private set; } = null!;


        /// <summary>
        /// Create a Domain resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Domain(string name, DomainArgs args, CustomResourceOptions? options = null)
            : base("gcp:activedirectory/domain:Domain", name, args ?? new DomainArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Domain(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null)
            : base("gcp:activedirectory/domain:Domain", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Domain resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Domain Get(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null)
        {
            return new Domain(name, id, state, options);
        }
    }

    public sealed class DomainArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of delegated administrator account used to perform Active Directory operations.
        /// If not specified, setupadmin will be used.
        /// </summary>
        [Input("admin")]
        public Input<string>? Admin { get; set; }

        [Input("authorizedNetworks")]
        private InputList<string>? _authorizedNetworks;

        /// <summary>
        /// The full names of the Google Compute Engine networks the domain instance is connected to. The domain is only available on networks listed in authorizedNetworks.
        /// If CIDR subnets overlap between networks, domain creation will fail.
        /// </summary>
        public InputList<string> AuthorizedNetworks
        {
            get => _authorizedNetworks ?? (_authorizedNetworks = new InputList<string>());
            set => _authorizedNetworks = value;
        }

        /// <summary>
        /// The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions,
        /// https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.
        /// </summary>
        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Resource labels that can contain user-provided metadata
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("locations", required: true)]
        private InputList<string>? _locations;

        /// <summary>
        /// Locations where domain needs to be provisioned. [regions][compute/docs/regions-zones/]
        /// e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block.
        /// </summary>
        public InputList<string> Locations
        {
            get => _locations ?? (_locations = new InputList<string>());
            set => _locations = value;
        }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger.
        /// Ranges must be unique and non-overlapping with existing subnets in authorizedNetworks
        /// </summary>
        [Input("reservedIpRange", required: true)]
        public Input<string> ReservedIpRange { get; set; } = null!;

        public DomainArgs()
        {
        }
    }

    public sealed class DomainState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of delegated administrator account used to perform Active Directory operations.
        /// If not specified, setupadmin will be used.
        /// </summary>
        [Input("admin")]
        public Input<string>? Admin { get; set; }

        [Input("authorizedNetworks")]
        private InputList<string>? _authorizedNetworks;

        /// <summary>
        /// The full names of the Google Compute Engine networks the domain instance is connected to. The domain is only available on networks listed in authorizedNetworks.
        /// If CIDR subnets overlap between networks, domain creation will fail.
        /// </summary>
        public InputList<string> AuthorizedNetworks
        {
            get => _authorizedNetworks ?? (_authorizedNetworks = new InputList<string>());
            set => _authorizedNetworks = value;
        }

        /// <summary>
        /// The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions,
        /// https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.
        /// </summary>
        [Input("domainName")]
        public Input<string>? DomainName { get; set; }

        /// <summary>
        /// The fully-qualified domain name of the exposed domain used by clients to connect to the service. Similar to what would
        /// be chosen for an Active Directory set up on an internal network.
        /// </summary>
        [Input("fqdn")]
        public Input<string>? Fqdn { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Resource labels that can contain user-provided metadata
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("locations")]
        private InputList<string>? _locations;

        /// <summary>
        /// Locations where domain needs to be provisioned. [regions][compute/docs/regions-zones/]
        /// e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block.
        /// </summary>
        public InputList<string> Locations
        {
            get => _locations ?? (_locations = new InputList<string>());
            set => _locations = value;
        }

        /// <summary>
        /// The unique name of the domain using the format: 'projects/{project}/locations/global/domains/{domainName}'.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger.
        /// Ranges must be unique and non-overlapping with existing subnets in authorizedNetworks
        /// </summary>
        [Input("reservedIpRange")]
        public Input<string>? ReservedIpRange { get; set; }

        public DomainState()
        {
        }
    }
}
