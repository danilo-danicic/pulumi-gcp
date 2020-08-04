// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudRun
{
    /// <summary>
    /// Service acts as a top-level container that manages a set of Routes and
    /// Configurations which implement a network service. Service exists to provide a
    /// singular abstraction which can be access controlled, reasoned about, and
    /// which encapsulates software lifecycle decisions such as rollout policy and
    /// team resource ownership. Service acts only as an orchestrator of the
    /// underlying Routes and Configurations (much as a kubernetes Deployment
    /// orchestrates ReplicaSets).
    /// 
    /// The Service's controller will track the statuses of its owned Configuration
    /// and Route, reflecting their statuses and conditions as its own.
    /// 
    /// See also:
    /// https://github.com/knative/serving/blob/master/docs/spec/overview.md#service
    /// 
    /// To get more information about Service, see:
    /// 
    /// * [API documentation](https://cloud.google.com/run/docs/reference/rest/v1/projects.locations.services)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/run/docs/)
    /// 
    /// ## Example Usage
    /// </summary>
    public partial class Service : Pulumi.CustomResource
    {
        /// <summary>
        /// If set to `true`, the revision name (template.metadata.name) will be omitted and 
        /// autogenerated by Cloud Run. This cannot be set to `true` while `template.metadata.name`
        /// is also set.
        /// (For legacy support, if `template.metadata.name` is unset in state while
        /// this field is set to false, the revision name will still autogenerate.)
        /// </summary>
        [Output("autogenerateRevisionName")]
        public Output<bool?> AutogenerateRevisionName { get; private set; } = null!;

        /// <summary>
        /// The location of the cloud run instance. eg us-central1
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// Metadata associated with this Service, including name, namespace, labels,
        /// and annotations.  Structure is documented below.
        /// </summary>
        [Output("metadata")]
        public Output<Outputs.ServiceMetadata> Metadata { get; private set; } = null!;

        /// <summary>
        /// Name of the port.
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
        /// The current status of the Service.
        /// </summary>
        [Output("status")]
        public Output<Outputs.ServiceStatus> Status { get; private set; } = null!;

        /// <summary>
        /// template holds the latest specification for the Revision to
        /// be stamped out. The template references the container image, and may also
        /// include labels and annotations that should be attached to the Revision.
        /// To correlate a Revision, and/or to force a Revision to be created when the
        /// spec doesn't otherwise change, a nonce label may be provided in the
        /// template metadata. For more details, see:
        /// https://github.com/knative/serving/blob/master/docs/client-conventions.md#associate-modifications-with-revisions
        /// Cloud Run does not currently support referencing a build that is
        /// responsible for materializing the container image from source.  Structure is documented below.
        /// </summary>
        [Output("template")]
        public Output<Outputs.ServiceTemplate?> Template { get; private set; } = null!;

        /// <summary>
        /// Traffic specifies how to distribute traffic over a collection of Knative Revisions
        /// and Configurations  Structure is documented below.
        /// </summary>
        [Output("traffics")]
        public Output<ImmutableArray<Outputs.ServiceTraffic>> Traffics { get; private set; } = null!;


        /// <summary>
        /// Create a Service resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Service(string name, ServiceArgs args, CustomResourceOptions? options = null)
            : base("gcp:cloudrun/service:Service", name, args ?? new ServiceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Service(string name, Input<string> id, ServiceState? state = null, CustomResourceOptions? options = null)
            : base("gcp:cloudrun/service:Service", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Service resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Service Get(string name, Input<string> id, ServiceState? state = null, CustomResourceOptions? options = null)
        {
            return new Service(name, id, state, options);
        }
    }

    public sealed class ServiceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If set to `true`, the revision name (template.metadata.name) will be omitted and 
        /// autogenerated by Cloud Run. This cannot be set to `true` while `template.metadata.name`
        /// is also set.
        /// (For legacy support, if `template.metadata.name` is unset in state while
        /// this field is set to false, the revision name will still autogenerate.)
        /// </summary>
        [Input("autogenerateRevisionName")]
        public Input<bool>? AutogenerateRevisionName { get; set; }

        /// <summary>
        /// The location of the cloud run instance. eg us-central1
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// Metadata associated with this Service, including name, namespace, labels,
        /// and annotations.  Structure is documented below.
        /// </summary>
        [Input("metadata")]
        public Input<Inputs.ServiceMetadataArgs>? Metadata { get; set; }

        /// <summary>
        /// Name of the port.
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
        /// template holds the latest specification for the Revision to
        /// be stamped out. The template references the container image, and may also
        /// include labels and annotations that should be attached to the Revision.
        /// To correlate a Revision, and/or to force a Revision to be created when the
        /// spec doesn't otherwise change, a nonce label may be provided in the
        /// template metadata. For more details, see:
        /// https://github.com/knative/serving/blob/master/docs/client-conventions.md#associate-modifications-with-revisions
        /// Cloud Run does not currently support referencing a build that is
        /// responsible for materializing the container image from source.  Structure is documented below.
        /// </summary>
        [Input("template")]
        public Input<Inputs.ServiceTemplateArgs>? Template { get; set; }

        [Input("traffics")]
        private InputList<Inputs.ServiceTrafficArgs>? _traffics;

        /// <summary>
        /// Traffic specifies how to distribute traffic over a collection of Knative Revisions
        /// and Configurations  Structure is documented below.
        /// </summary>
        public InputList<Inputs.ServiceTrafficArgs> Traffics
        {
            get => _traffics ?? (_traffics = new InputList<Inputs.ServiceTrafficArgs>());
            set => _traffics = value;
        }

        public ServiceArgs()
        {
        }
    }

    public sealed class ServiceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If set to `true`, the revision name (template.metadata.name) will be omitted and 
        /// autogenerated by Cloud Run. This cannot be set to `true` while `template.metadata.name`
        /// is also set.
        /// (For legacy support, if `template.metadata.name` is unset in state while
        /// this field is set to false, the revision name will still autogenerate.)
        /// </summary>
        [Input("autogenerateRevisionName")]
        public Input<bool>? AutogenerateRevisionName { get; set; }

        /// <summary>
        /// The location of the cloud run instance. eg us-central1
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Metadata associated with this Service, including name, namespace, labels,
        /// and annotations.  Structure is documented below.
        /// </summary>
        [Input("metadata")]
        public Input<Inputs.ServiceMetadataGetArgs>? Metadata { get; set; }

        /// <summary>
        /// Name of the port.
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
        /// The current status of the Service.
        /// </summary>
        [Input("status")]
        public Input<Inputs.ServiceStatusGetArgs>? Status { get; set; }

        /// <summary>
        /// template holds the latest specification for the Revision to
        /// be stamped out. The template references the container image, and may also
        /// include labels and annotations that should be attached to the Revision.
        /// To correlate a Revision, and/or to force a Revision to be created when the
        /// spec doesn't otherwise change, a nonce label may be provided in the
        /// template metadata. For more details, see:
        /// https://github.com/knative/serving/blob/master/docs/client-conventions.md#associate-modifications-with-revisions
        /// Cloud Run does not currently support referencing a build that is
        /// responsible for materializing the container image from source.  Structure is documented below.
        /// </summary>
        [Input("template")]
        public Input<Inputs.ServiceTemplateGetArgs>? Template { get; set; }

        [Input("traffics")]
        private InputList<Inputs.ServiceTrafficGetArgs>? _traffics;

        /// <summary>
        /// Traffic specifies how to distribute traffic over a collection of Knative Revisions
        /// and Configurations  Structure is documented below.
        /// </summary>
        public InputList<Inputs.ServiceTrafficGetArgs> Traffics
        {
            get => _traffics ?? (_traffics = new InputList<Inputs.ServiceTrafficGetArgs>());
            set => _traffics = value;
        }

        public ServiceState()
        {
        }
    }
}
