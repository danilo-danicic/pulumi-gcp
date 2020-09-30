// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudFunctions
{
    /// <summary>
    /// Creates a new Cloud Function. For more information see
    /// [the official documentation](https://cloud.google.com/functions/docs/)
    /// and
    /// [API](https://cloud.google.com/functions/docs/apis).
    /// 
    /// &gt; **Warning:** As of November 1, 2019, newly created Functions are
    /// private-by-default and will require [appropriate IAM permissions](https://cloud.google.com/functions/docs/reference/iam/roles)
    /// to be invoked. See below examples for how to set up the appropriate permissions,
    /// or view the [Cloud Functions IAM resources](https://www.terraform.io/docs/providers/google/r/cloudfunctions_cloud_function_iam.html)
    /// for Cloud Functions.
    /// 
    /// ## Example Usage
    /// </summary>
    public partial class Function : Pulumi.CustomResource
    {
        /// <summary>
        /// Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
        /// </summary>
        [Output("availableMemoryMb")]
        public Output<int?> AvailableMemoryMb { get; private set; } = null!;

        /// <summary>
        /// Description of the function.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Name of the function that will be executed when the Google Cloud Function is triggered.
        /// </summary>
        [Output("entryPoint")]
        public Output<string?> EntryPoint { get; private set; } = null!;

        /// <summary>
        /// A set of key/value environment variable pairs to assign to the function.
        /// </summary>
        [Output("environmentVariables")]
        public Output<ImmutableDictionary<string, object>?> EnvironmentVariables { get; private set; } = null!;

        /// <summary>
        /// A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
        /// </summary>
        [Output("eventTrigger")]
        public Output<Outputs.FunctionEventTrigger> EventTrigger { get; private set; } = null!;

        /// <summary>
        /// URL which triggers function execution. Returned only if `trigger_http` is used.
        /// </summary>
        [Output("httpsTriggerUrl")]
        public Output<string> HttpsTriggerUrl { get; private set; } = null!;

        /// <summary>
        /// String value that controls what traffic can reach the function. Allowed values are `ALLOW_ALL`, `ALLOW_INTERNAL_AND_GCLB` and `ALLOW_INTERNAL_ONLY`. Changes to this field will recreate the cloud function.
        /// </summary>
        [Output("ingressSettings")]
        public Output<string?> IngressSettings { get; private set; } = null!;

        /// <summary>
        /// A set of key/value label pairs to assign to the function. Label keys must follow the requirements at https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, object>?> Labels { get; private set; } = null!;

        /// <summary>
        /// The limit on the maximum number of function instances that may coexist at a given time.
        /// </summary>
        [Output("maxInstances")]
        public Output<int?> MaxInstances { get; private set; } = null!;

        /// <summary>
        /// A user-defined name of the function. Function names must be unique globally.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Project of the function. If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The runtime in which the function is going to run.
        /// Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`, `"go113"`.
        /// </summary>
        [Output("runtime")]
        public Output<string> Runtime { get; private set; } = null!;

        /// <summary>
        /// If provided, the self-provided service account to run the function with.
        /// </summary>
        [Output("serviceAccountEmail")]
        public Output<string> ServiceAccountEmail { get; private set; } = null!;

        /// <summary>
        /// The GCS bucket containing the zip archive which contains the function.
        /// </summary>
        [Output("sourceArchiveBucket")]
        public Output<string?> SourceArchiveBucket { get; private set; } = null!;

        /// <summary>
        /// The source archive object (file) in archive bucket.
        /// </summary>
        [Output("sourceArchiveObject")]
        public Output<string?> SourceArchiveObject { get; private set; } = null!;

        /// <summary>
        /// Represents parameters related to source repository where a function is hosted.
        /// Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
        /// </summary>
        [Output("sourceRepository")]
        public Output<Outputs.FunctionSourceRepository?> SourceRepository { get; private set; } = null!;

        /// <summary>
        /// Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
        /// </summary>
        [Output("timeout")]
        public Output<int?> Timeout { get; private set; } = null!;

        /// <summary>
        /// Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
        /// </summary>
        [Output("triggerHttp")]
        public Output<bool?> TriggerHttp { get; private set; } = null!;

        /// <summary>
        /// The VPC Network Connector that this cloud function can connect to. It should be set up as fully-qualified URI. The format of this field is `projects/*/locations/*/connectors/*`.
        /// </summary>
        [Output("vpcConnector")]
        public Output<string?> VpcConnector { get; private set; } = null!;

        /// <summary>
        /// The egress settings for the connector, controlling what traffic is diverted through it. Allowed values are `ALL_TRAFFIC` and `PRIVATE_RANGES_ONLY`. Defaults to `PRIVATE_RANGES_ONLY`. If unset, this field preserves the previously set value.
        /// </summary>
        [Output("vpcConnectorEgressSettings")]
        public Output<string> VpcConnectorEgressSettings { get; private set; } = null!;


        /// <summary>
        /// Create a Function resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Function(string name, FunctionArgs args, CustomResourceOptions? options = null)
            : base("gcp:cloudfunctions/function:Function", name, args ?? new FunctionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Function(string name, Input<string> id, FunctionState? state = null, CustomResourceOptions? options = null)
            : base("gcp:cloudfunctions/function:Function", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Function resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Function Get(string name, Input<string> id, FunctionState? state = null, CustomResourceOptions? options = null)
        {
            return new Function(name, id, state, options);
        }
    }

    public sealed class FunctionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
        /// </summary>
        [Input("availableMemoryMb")]
        public Input<int>? AvailableMemoryMb { get; set; }

        /// <summary>
        /// Description of the function.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the function that will be executed when the Google Cloud Function is triggered.
        /// </summary>
        [Input("entryPoint")]
        public Input<string>? EntryPoint { get; set; }

        [Input("environmentVariables")]
        private InputMap<object>? _environmentVariables;

        /// <summary>
        /// A set of key/value environment variable pairs to assign to the function.
        /// </summary>
        public InputMap<object> EnvironmentVariables
        {
            get => _environmentVariables ?? (_environmentVariables = new InputMap<object>());
            set => _environmentVariables = value;
        }

        /// <summary>
        /// A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
        /// </summary>
        [Input("eventTrigger")]
        public Input<Inputs.FunctionEventTriggerArgs>? EventTrigger { get; set; }

        /// <summary>
        /// URL which triggers function execution. Returned only if `trigger_http` is used.
        /// </summary>
        [Input("httpsTriggerUrl")]
        public Input<string>? HttpsTriggerUrl { get; set; }

        /// <summary>
        /// String value that controls what traffic can reach the function. Allowed values are `ALLOW_ALL`, `ALLOW_INTERNAL_AND_GCLB` and `ALLOW_INTERNAL_ONLY`. Changes to this field will recreate the cloud function.
        /// </summary>
        [Input("ingressSettings")]
        public Input<string>? IngressSettings { get; set; }

        [Input("labels")]
        private InputMap<object>? _labels;

        /// <summary>
        /// A set of key/value label pairs to assign to the function. Label keys must follow the requirements at https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements.
        /// </summary>
        public InputMap<object> Labels
        {
            get => _labels ?? (_labels = new InputMap<object>());
            set => _labels = value;
        }

        /// <summary>
        /// The limit on the maximum number of function instances that may coexist at a given time.
        /// </summary>
        [Input("maxInstances")]
        public Input<int>? MaxInstances { get; set; }

        /// <summary>
        /// A user-defined name of the function. Function names must be unique globally.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Project of the function. If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The runtime in which the function is going to run.
        /// Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`, `"go113"`.
        /// </summary>
        [Input("runtime", required: true)]
        public Input<string> Runtime { get; set; } = null!;

        /// <summary>
        /// If provided, the self-provided service account to run the function with.
        /// </summary>
        [Input("serviceAccountEmail")]
        public Input<string>? ServiceAccountEmail { get; set; }

        /// <summary>
        /// The GCS bucket containing the zip archive which contains the function.
        /// </summary>
        [Input("sourceArchiveBucket")]
        public Input<string>? SourceArchiveBucket { get; set; }

        /// <summary>
        /// The source archive object (file) in archive bucket.
        /// </summary>
        [Input("sourceArchiveObject")]
        public Input<string>? SourceArchiveObject { get; set; }

        /// <summary>
        /// Represents parameters related to source repository where a function is hosted.
        /// Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
        /// </summary>
        [Input("sourceRepository")]
        public Input<Inputs.FunctionSourceRepositoryArgs>? SourceRepository { get; set; }

        /// <summary>
        /// Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
        /// </summary>
        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        /// <summary>
        /// Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
        /// </summary>
        [Input("triggerHttp")]
        public Input<bool>? TriggerHttp { get; set; }

        /// <summary>
        /// The VPC Network Connector that this cloud function can connect to. It should be set up as fully-qualified URI. The format of this field is `projects/*/locations/*/connectors/*`.
        /// </summary>
        [Input("vpcConnector")]
        public Input<string>? VpcConnector { get; set; }

        /// <summary>
        /// The egress settings for the connector, controlling what traffic is diverted through it. Allowed values are `ALL_TRAFFIC` and `PRIVATE_RANGES_ONLY`. Defaults to `PRIVATE_RANGES_ONLY`. If unset, this field preserves the previously set value.
        /// </summary>
        [Input("vpcConnectorEgressSettings")]
        public Input<string>? VpcConnectorEgressSettings { get; set; }

        public FunctionArgs()
        {
        }
    }

    public sealed class FunctionState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
        /// </summary>
        [Input("availableMemoryMb")]
        public Input<int>? AvailableMemoryMb { get; set; }

        /// <summary>
        /// Description of the function.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the function that will be executed when the Google Cloud Function is triggered.
        /// </summary>
        [Input("entryPoint")]
        public Input<string>? EntryPoint { get; set; }

        [Input("environmentVariables")]
        private InputMap<object>? _environmentVariables;

        /// <summary>
        /// A set of key/value environment variable pairs to assign to the function.
        /// </summary>
        public InputMap<object> EnvironmentVariables
        {
            get => _environmentVariables ?? (_environmentVariables = new InputMap<object>());
            set => _environmentVariables = value;
        }

        /// <summary>
        /// A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
        /// </summary>
        [Input("eventTrigger")]
        public Input<Inputs.FunctionEventTriggerGetArgs>? EventTrigger { get; set; }

        /// <summary>
        /// URL which triggers function execution. Returned only if `trigger_http` is used.
        /// </summary>
        [Input("httpsTriggerUrl")]
        public Input<string>? HttpsTriggerUrl { get; set; }

        /// <summary>
        /// String value that controls what traffic can reach the function. Allowed values are `ALLOW_ALL`, `ALLOW_INTERNAL_AND_GCLB` and `ALLOW_INTERNAL_ONLY`. Changes to this field will recreate the cloud function.
        /// </summary>
        [Input("ingressSettings")]
        public Input<string>? IngressSettings { get; set; }

        [Input("labels")]
        private InputMap<object>? _labels;

        /// <summary>
        /// A set of key/value label pairs to assign to the function. Label keys must follow the requirements at https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements.
        /// </summary>
        public InputMap<object> Labels
        {
            get => _labels ?? (_labels = new InputMap<object>());
            set => _labels = value;
        }

        /// <summary>
        /// The limit on the maximum number of function instances that may coexist at a given time.
        /// </summary>
        [Input("maxInstances")]
        public Input<int>? MaxInstances { get; set; }

        /// <summary>
        /// A user-defined name of the function. Function names must be unique globally.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Project of the function. If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The runtime in which the function is going to run.
        /// Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`, `"go113"`.
        /// </summary>
        [Input("runtime")]
        public Input<string>? Runtime { get; set; }

        /// <summary>
        /// If provided, the self-provided service account to run the function with.
        /// </summary>
        [Input("serviceAccountEmail")]
        public Input<string>? ServiceAccountEmail { get; set; }

        /// <summary>
        /// The GCS bucket containing the zip archive which contains the function.
        /// </summary>
        [Input("sourceArchiveBucket")]
        public Input<string>? SourceArchiveBucket { get; set; }

        /// <summary>
        /// The source archive object (file) in archive bucket.
        /// </summary>
        [Input("sourceArchiveObject")]
        public Input<string>? SourceArchiveObject { get; set; }

        /// <summary>
        /// Represents parameters related to source repository where a function is hosted.
        /// Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
        /// </summary>
        [Input("sourceRepository")]
        public Input<Inputs.FunctionSourceRepositoryGetArgs>? SourceRepository { get; set; }

        /// <summary>
        /// Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
        /// </summary>
        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        /// <summary>
        /// Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
        /// </summary>
        [Input("triggerHttp")]
        public Input<bool>? TriggerHttp { get; set; }

        /// <summary>
        /// The VPC Network Connector that this cloud function can connect to. It should be set up as fully-qualified URI. The format of this field is `projects/*/locations/*/connectors/*`.
        /// </summary>
        [Input("vpcConnector")]
        public Input<string>? VpcConnector { get; set; }

        /// <summary>
        /// The egress settings for the connector, controlling what traffic is diverted through it. Allowed values are `ALL_TRAFFIC` and `PRIVATE_RANGES_ONLY`. Defaults to `PRIVATE_RANGES_ONLY`. If unset, this field preserves the previously set value.
        /// </summary>
        [Input("vpcConnectorEgressSettings")]
        public Input<string>? VpcConnectorEgressSettings { get; set; }

        public FunctionState()
        {
        }
    }
}
