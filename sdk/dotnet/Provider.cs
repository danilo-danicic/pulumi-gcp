// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp
{
    /// <summary>
    /// The provider type for the google-beta package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    public partial class Provider : Pulumi.ProviderResource
    {
        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("gcp", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
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
    }

    public sealed class ProviderArgs : Pulumi.ResourceArgs
    {
        [Input("accessContextManagerCustomEndpoint")]
        public Input<string>? AccessContextManagerCustomEndpoint { get; set; }

        [Input("accessToken")]
        public Input<string>? AccessToken { get; set; }

        [Input("appEngineCustomEndpoint")]
        public Input<string>? AppEngineCustomEndpoint { get; set; }

        [Input("artifactRegistryCustomEndpoint")]
        public Input<string>? ArtifactRegistryCustomEndpoint { get; set; }

        [Input("batching", json: true)]
        public Input<Inputs.ProviderBatchingArgs>? Batching { get; set; }

        [Input("bigQueryCustomEndpoint")]
        public Input<string>? BigQueryCustomEndpoint { get; set; }

        [Input("bigqueryConnectionCustomEndpoint")]
        public Input<string>? BigqueryConnectionCustomEndpoint { get; set; }

        [Input("bigqueryDataTransferCustomEndpoint")]
        public Input<string>? BigqueryDataTransferCustomEndpoint { get; set; }

        [Input("bigqueryReservationCustomEndpoint")]
        public Input<string>? BigqueryReservationCustomEndpoint { get; set; }

        [Input("bigtableCustomEndpoint")]
        public Input<string>? BigtableCustomEndpoint { get; set; }

        [Input("billingCustomEndpoint")]
        public Input<string>? BillingCustomEndpoint { get; set; }

        [Input("binaryAuthorizationCustomEndpoint")]
        public Input<string>? BinaryAuthorizationCustomEndpoint { get; set; }

        [Input("cloudBillingCustomEndpoint")]
        public Input<string>? CloudBillingCustomEndpoint { get; set; }

        [Input("cloudBuildCustomEndpoint")]
        public Input<string>? CloudBuildCustomEndpoint { get; set; }

        [Input("cloudFunctionsCustomEndpoint")]
        public Input<string>? CloudFunctionsCustomEndpoint { get; set; }

        [Input("cloudIotCustomEndpoint")]
        public Input<string>? CloudIotCustomEndpoint { get; set; }

        [Input("cloudRunCustomEndpoint")]
        public Input<string>? CloudRunCustomEndpoint { get; set; }

        [Input("cloudSchedulerCustomEndpoint")]
        public Input<string>? CloudSchedulerCustomEndpoint { get; set; }

        [Input("cloudTasksCustomEndpoint")]
        public Input<string>? CloudTasksCustomEndpoint { get; set; }

        [Input("composerCustomEndpoint")]
        public Input<string>? ComposerCustomEndpoint { get; set; }

        [Input("computeBetaCustomEndpoint")]
        public Input<string>? ComputeBetaCustomEndpoint { get; set; }

        [Input("computeCustomEndpoint")]
        public Input<string>? ComputeCustomEndpoint { get; set; }

        [Input("containerAnalysisCustomEndpoint")]
        public Input<string>? ContainerAnalysisCustomEndpoint { get; set; }

        [Input("containerBetaCustomEndpoint")]
        public Input<string>? ContainerBetaCustomEndpoint { get; set; }

        [Input("containerCustomEndpoint")]
        public Input<string>? ContainerCustomEndpoint { get; set; }

        [Input("credentials")]
        public Input<string>? Credentials { get; set; }

        [Input("dataCatalogCustomEndpoint")]
        public Input<string>? DataCatalogCustomEndpoint { get; set; }

        [Input("dataFusionCustomEndpoint")]
        public Input<string>? DataFusionCustomEndpoint { get; set; }

        [Input("dataflowCustomEndpoint")]
        public Input<string>? DataflowCustomEndpoint { get; set; }

        [Input("dataprocBetaCustomEndpoint")]
        public Input<string>? DataprocBetaCustomEndpoint { get; set; }

        [Input("dataprocCustomEndpoint")]
        public Input<string>? DataprocCustomEndpoint { get; set; }

        [Input("datastoreCustomEndpoint")]
        public Input<string>? DatastoreCustomEndpoint { get; set; }

        [Input("deploymentManagerCustomEndpoint")]
        public Input<string>? DeploymentManagerCustomEndpoint { get; set; }

        [Input("dialogflowCustomEndpoint")]
        public Input<string>? DialogflowCustomEndpoint { get; set; }

        [Input("dnsBetaCustomEndpoint")]
        public Input<string>? DnsBetaCustomEndpoint { get; set; }

        [Input("dnsCustomEndpoint")]
        public Input<string>? DnsCustomEndpoint { get; set; }

        [Input("filestoreCustomEndpoint")]
        public Input<string>? FilestoreCustomEndpoint { get; set; }

        [Input("firebaseCustomEndpoint")]
        public Input<string>? FirebaseCustomEndpoint { get; set; }

        [Input("firestoreCustomEndpoint")]
        public Input<string>? FirestoreCustomEndpoint { get; set; }

        [Input("gameServicesCustomEndpoint")]
        public Input<string>? GameServicesCustomEndpoint { get; set; }

        [Input("healthcareCustomEndpoint")]
        public Input<string>? HealthcareCustomEndpoint { get; set; }

        [Input("iamCredentialsCustomEndpoint")]
        public Input<string>? IamCredentialsCustomEndpoint { get; set; }

        [Input("iamCustomEndpoint")]
        public Input<string>? IamCustomEndpoint { get; set; }

        [Input("iapCustomEndpoint")]
        public Input<string>? IapCustomEndpoint { get; set; }

        [Input("identityPlatformCustomEndpoint")]
        public Input<string>? IdentityPlatformCustomEndpoint { get; set; }

        [Input("kmsCustomEndpoint")]
        public Input<string>? KmsCustomEndpoint { get; set; }

        [Input("loggingCustomEndpoint")]
        public Input<string>? LoggingCustomEndpoint { get; set; }

        [Input("memcacheCustomEndpoint")]
        public Input<string>? MemcacheCustomEndpoint { get; set; }

        [Input("mlEngineCustomEndpoint")]
        public Input<string>? MlEngineCustomEndpoint { get; set; }

        [Input("monitoringCustomEndpoint")]
        public Input<string>? MonitoringCustomEndpoint { get; set; }

        [Input("networkManagementCustomEndpoint")]
        public Input<string>? NetworkManagementCustomEndpoint { get; set; }

        [Input("osLoginCustomEndpoint")]
        public Input<string>? OsLoginCustomEndpoint { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("pubsubCustomEndpoint")]
        public Input<string>? PubsubCustomEndpoint { get; set; }

        [Input("redisCustomEndpoint")]
        public Input<string>? RedisCustomEndpoint { get; set; }

        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("requestTimeout")]
        public Input<string>? RequestTimeout { get; set; }

        [Input("resourceManagerCustomEndpoint")]
        public Input<string>? ResourceManagerCustomEndpoint { get; set; }

        [Input("resourceManagerV2beta1CustomEndpoint")]
        public Input<string>? ResourceManagerV2beta1CustomEndpoint { get; set; }

        [Input("runtimeConfigCustomEndpoint")]
        public Input<string>? RuntimeConfigCustomEndpoint { get; set; }

        [Input("runtimeconfigCustomEndpoint")]
        public Input<string>? RuntimeconfigCustomEndpoint { get; set; }

        [Input("scopes", json: true)]
        private InputList<string>? _scopes;
        public InputList<string> Scopes
        {
            get => _scopes ?? (_scopes = new InputList<string>());
            set => _scopes = value;
        }

        [Input("secretManagerCustomEndpoint")]
        public Input<string>? SecretManagerCustomEndpoint { get; set; }

        [Input("securityCenterCustomEndpoint")]
        public Input<string>? SecurityCenterCustomEndpoint { get; set; }

        [Input("securityScannerCustomEndpoint")]
        public Input<string>? SecurityScannerCustomEndpoint { get; set; }

        [Input("serviceDirectoryCustomEndpoint")]
        public Input<string>? ServiceDirectoryCustomEndpoint { get; set; }

        [Input("serviceManagementCustomEndpoint")]
        public Input<string>? ServiceManagementCustomEndpoint { get; set; }

        [Input("serviceNetworkingCustomEndpoint")]
        public Input<string>? ServiceNetworkingCustomEndpoint { get; set; }

        [Input("serviceUsageCustomEndpoint")]
        public Input<string>? ServiceUsageCustomEndpoint { get; set; }

        [Input("sourceRepoCustomEndpoint")]
        public Input<string>? SourceRepoCustomEndpoint { get; set; }

        [Input("spannerCustomEndpoint")]
        public Input<string>? SpannerCustomEndpoint { get; set; }

        [Input("sqlCustomEndpoint")]
        public Input<string>? SqlCustomEndpoint { get; set; }

        [Input("storageCustomEndpoint")]
        public Input<string>? StorageCustomEndpoint { get; set; }

        [Input("storageTransferCustomEndpoint")]
        public Input<string>? StorageTransferCustomEndpoint { get; set; }

        [Input("tpuCustomEndpoint")]
        public Input<string>? TpuCustomEndpoint { get; set; }

        [Input("userProjectOverride", json: true)]
        public Input<bool>? UserProjectOverride { get; set; }

        [Input("vpcAccessCustomEndpoint")]
        public Input<string>? VpcAccessCustomEndpoint { get; set; }

        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public ProviderArgs()
        {
            Credentials = Utilities.GetEnv("GOOGLE_CREDENTIALS", "GOOGLE_CLOUD_KEYFILE_JSON", "GCLOUD_KEYFILE_JSON");
            Project = Utilities.GetEnv("GOOGLE_PROJECT", "GOOGLE_CLOUD_PROJECT", "GCLOUD_PROJECT", "CLOUDSDK_CORE_PROJECT");
            Region = Utilities.GetEnv("GOOGLE_REGION", "GCLOUD_REGION", "CLOUDSDK_COMPUTE_REGION");
            Zone = Utilities.GetEnv("GOOGLE_ZONE", "GCLOUD_ZONE", "CLOUDSDK_COMPUTE_ZONE");
        }
    }
}
