// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    /// <summary>
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_ssl_proxy.html.markdown.
    /// </summary>
    public partial class TargetSSLProxy : Pulumi.CustomResource
    {
        [Output("backendService")]
        public Output<string> BackendService { get; private set; } = null!;

        [Output("creationTimestamp")]
        public Output<string> CreationTimestamp { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        [Output("proxyHeader")]
        public Output<string?> ProxyHeader { get; private set; } = null!;

        [Output("proxyId")]
        public Output<int> ProxyId { get; private set; } = null!;

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        [Output("sslCertificates")]
        public Output<string> SslCertificates { get; private set; } = null!;

        [Output("sslPolicy")]
        public Output<string?> SslPolicy { get; private set; } = null!;


        /// <summary>
        /// Create a TargetSSLProxy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TargetSSLProxy(string name, TargetSSLProxyArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/targetSSLProxy:TargetSSLProxy", name, args, MakeResourceOptions(options, ""))
        {
        }

        private TargetSSLProxy(string name, Input<string> id, TargetSSLProxyState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/targetSSLProxy:TargetSSLProxy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing TargetSSLProxy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TargetSSLProxy Get(string name, Input<string> id, TargetSSLProxyState? state = null, CustomResourceOptions? options = null)
        {
            return new TargetSSLProxy(name, id, state, options);
        }
    }

    public sealed class TargetSSLProxyArgs : Pulumi.ResourceArgs
    {
        [Input("backendService", required: true)]
        public Input<string> BackendService { get; set; } = null!;

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("proxyHeader")]
        public Input<string>? ProxyHeader { get; set; }

        [Input("sslCertificates", required: true)]
        public Input<string> SslCertificates { get; set; } = null!;

        [Input("sslPolicy")]
        public Input<string>? SslPolicy { get; set; }

        public TargetSSLProxyArgs()
        {
        }
    }

    public sealed class TargetSSLProxyState : Pulumi.ResourceArgs
    {
        [Input("backendService")]
        public Input<string>? BackendService { get; set; }

        [Input("creationTimestamp")]
        public Input<string>? CreationTimestamp { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("proxyHeader")]
        public Input<string>? ProxyHeader { get; set; }

        [Input("proxyId")]
        public Input<int>? ProxyId { get; set; }

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        [Input("sslCertificates")]
        public Input<string>? SslCertificates { get; set; }

        [Input("sslPolicy")]
        public Input<string>? SslPolicy { get; set; }

        public TargetSSLProxyState()
        {
        }
    }
}
