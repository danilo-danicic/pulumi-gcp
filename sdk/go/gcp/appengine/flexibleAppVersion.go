// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appengine

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Flexible App Version resource to create a new version of flexible GAE Application. Based on Google Compute Engine,
// the App Engine flexible environment automatically scales your app up and down while also balancing the load.
// Learn about the differences between the standard environment and the flexible environment
// at https://cloud.google.com/appengine/docs/the-appengine-environments.
//
// > **Note:** The App Engine flexible environment service account uses the member ID `service-[YOUR_PROJECT_NUMBER]@gae-api-prod.google.com.iam.gserviceaccount.com`
// It should have the App Engine Flexible Environment Service Agent role, which will be applied when the `appengineflex.googleapis.com` service is enabled.
//
// To get more information about FlexibleAppVersion, see:
//
// * [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/appengine/docs/flexible)
//
// ## Example Usage
type FlexibleAppVersion struct {
	pulumi.CustomResourceState

	// Serving configuration for Google Cloud Endpoints.  Structure is documented below.
	ApiConfig FlexibleAppVersionApiConfigPtrOutput `pulumi:"apiConfig"`
	// Automatic scaling is based on request rate, response latencies, and other application metrics.  Structure is documented below.
	AutomaticScaling FlexibleAppVersionAutomaticScalingPtrOutput `pulumi:"automaticScaling"`
	// Metadata settings that are supplied to this version to enable beta runtime features.
	BetaSettings pulumi.StringMapOutput `pulumi:"betaSettings"`
	// Duration that static files should be cached by web proxies and browsers.
	// Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time.
	DefaultExpiration pulumi.StringPtrOutput `pulumi:"defaultExpiration"`
	// If set to `true`, the service will be deleted if it is the last version.
	DeleteServiceOnDestroy pulumi.BoolPtrOutput `pulumi:"deleteServiceOnDestroy"`
	// Code and application artifacts that make up this version.  Structure is documented below.
	Deployment FlexibleAppVersionDeploymentPtrOutput `pulumi:"deployment"`
	// Code and application artifacts that make up this version.  Structure is documented below.
	EndpointsApiService FlexibleAppVersionEndpointsApiServicePtrOutput `pulumi:"endpointsApiService"`
	// The entrypoint for the application.  Structure is documented below.
	Entrypoint FlexibleAppVersionEntrypointPtrOutput `pulumi:"entrypoint"`
	// Environment variables available to the application.  As these are not returned in the API request, the provider will not detect any changes made outside of the config.
	EnvVariables pulumi.StringMapOutput `pulumi:"envVariables"`
	// An ordered list of URL-matching patterns that should be applied to incoming requests.
	// The first matching URL handles the request and other request handlers are not attempted.  Structure is documented below.
	Handlers FlexibleAppVersionHandlerArrayOutput `pulumi:"handlers"`
	// Before an application can receive email or XMPP messages, the application must be configured to enable the service.
	InboundServices pulumi.StringArrayOutput `pulumi:"inboundServices"`
	// Instance class that is used to run this version. Valid values are
	// AutomaticScaling: F1, F2, F4, F4_1G
	// ManualScaling: B1, B2, B4, B8, B4_1G
	// Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
	InstanceClass pulumi.StringPtrOutput `pulumi:"instanceClass"`
	// Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.  Structure is documented below.
	LivenessCheck FlexibleAppVersionLivenessCheckOutput `pulumi:"livenessCheck"`
	// A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.  Structure is documented below.
	ManualScaling FlexibleAppVersionManualScalingPtrOutput `pulumi:"manualScaling"`
	// Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1.
	Name pulumi.StringOutput `pulumi:"name"`
	// Extra network settings  Structure is documented below.
	Network FlexibleAppVersionNetworkPtrOutput `pulumi:"network"`
	// Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
	NobuildFilesRegex pulumi.StringPtrOutput `pulumi:"nobuildFilesRegex"`
	// If set to `true`, the application version will not be deleted.
	NoopOnDestroy pulumi.BoolPtrOutput `pulumi:"noopOnDestroy"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.  Structure is documented below.
	ReadinessCheck FlexibleAppVersionReadinessCheckOutput `pulumi:"readinessCheck"`
	// Machine resources for a version.  Structure is documented below.
	Resources FlexibleAppVersionResourcesPtrOutput `pulumi:"resources"`
	// Desired runtime. Example python27.
	Runtime pulumi.StringOutput `pulumi:"runtime"`
	// The version of the API in the given runtime environment.
	// Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
	RuntimeApiVersion pulumi.StringOutput `pulumi:"runtimeApiVersion"`
	// The channel of the runtime to use. Only available for some runtimes.
	RuntimeChannel pulumi.StringPtrOutput `pulumi:"runtimeChannel"`
	// The path or name of the app's main executable.
	RuntimeMainExecutablePath pulumi.StringPtrOutput `pulumi:"runtimeMainExecutablePath"`
	// AppEngine service resource
	Service pulumi.StringOutput `pulumi:"service"`
	// Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
	ServingStatus pulumi.StringPtrOutput `pulumi:"servingStatus"`
	// Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens.
	// Reserved names,"default", "latest", and any name with the prefix "ah-".
	VersionId pulumi.StringPtrOutput `pulumi:"versionId"`
	// Enables VPC connectivity for standard apps.  Structure is documented below.
	VpcAccessConnector FlexibleAppVersionVpcAccessConnectorPtrOutput `pulumi:"vpcAccessConnector"`
}

// NewFlexibleAppVersion registers a new resource with the given unique name, arguments, and options.
func NewFlexibleAppVersion(ctx *pulumi.Context,
	name string, args *FlexibleAppVersionArgs, opts ...pulumi.ResourceOption) (*FlexibleAppVersion, error) {
	if args == nil || args.LivenessCheck == nil {
		return nil, errors.New("missing required argument 'LivenessCheck'")
	}
	if args == nil || args.ReadinessCheck == nil {
		return nil, errors.New("missing required argument 'ReadinessCheck'")
	}
	if args == nil || args.Runtime == nil {
		return nil, errors.New("missing required argument 'Runtime'")
	}
	if args == nil || args.Service == nil {
		return nil, errors.New("missing required argument 'Service'")
	}
	if args == nil {
		args = &FlexibleAppVersionArgs{}
	}
	var resource FlexibleAppVersion
	err := ctx.RegisterResource("gcp:appengine/flexibleAppVersion:FlexibleAppVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFlexibleAppVersion gets an existing FlexibleAppVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFlexibleAppVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FlexibleAppVersionState, opts ...pulumi.ResourceOption) (*FlexibleAppVersion, error) {
	var resource FlexibleAppVersion
	err := ctx.ReadResource("gcp:appengine/flexibleAppVersion:FlexibleAppVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FlexibleAppVersion resources.
type flexibleAppVersionState struct {
	// Serving configuration for Google Cloud Endpoints.  Structure is documented below.
	ApiConfig *FlexibleAppVersionApiConfig `pulumi:"apiConfig"`
	// Automatic scaling is based on request rate, response latencies, and other application metrics.  Structure is documented below.
	AutomaticScaling *FlexibleAppVersionAutomaticScaling `pulumi:"automaticScaling"`
	// Metadata settings that are supplied to this version to enable beta runtime features.
	BetaSettings map[string]string `pulumi:"betaSettings"`
	// Duration that static files should be cached by web proxies and browsers.
	// Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time.
	DefaultExpiration *string `pulumi:"defaultExpiration"`
	// If set to `true`, the service will be deleted if it is the last version.
	DeleteServiceOnDestroy *bool `pulumi:"deleteServiceOnDestroy"`
	// Code and application artifacts that make up this version.  Structure is documented below.
	Deployment *FlexibleAppVersionDeployment `pulumi:"deployment"`
	// Code and application artifacts that make up this version.  Structure is documented below.
	EndpointsApiService *FlexibleAppVersionEndpointsApiService `pulumi:"endpointsApiService"`
	// The entrypoint for the application.  Structure is documented below.
	Entrypoint *FlexibleAppVersionEntrypoint `pulumi:"entrypoint"`
	// Environment variables available to the application.  As these are not returned in the API request, the provider will not detect any changes made outside of the config.
	EnvVariables map[string]string `pulumi:"envVariables"`
	// An ordered list of URL-matching patterns that should be applied to incoming requests.
	// The first matching URL handles the request and other request handlers are not attempted.  Structure is documented below.
	Handlers []FlexibleAppVersionHandler `pulumi:"handlers"`
	// Before an application can receive email or XMPP messages, the application must be configured to enable the service.
	InboundServices []string `pulumi:"inboundServices"`
	// Instance class that is used to run this version. Valid values are
	// AutomaticScaling: F1, F2, F4, F4_1G
	// ManualScaling: B1, B2, B4, B8, B4_1G
	// Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
	InstanceClass *string `pulumi:"instanceClass"`
	// Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.  Structure is documented below.
	LivenessCheck *FlexibleAppVersionLivenessCheck `pulumi:"livenessCheck"`
	// A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.  Structure is documented below.
	ManualScaling *FlexibleAppVersionManualScaling `pulumi:"manualScaling"`
	// Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1.
	Name *string `pulumi:"name"`
	// Extra network settings  Structure is documented below.
	Network *FlexibleAppVersionNetwork `pulumi:"network"`
	// Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
	NobuildFilesRegex *string `pulumi:"nobuildFilesRegex"`
	// If set to `true`, the application version will not be deleted.
	NoopOnDestroy *bool `pulumi:"noopOnDestroy"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.  Structure is documented below.
	ReadinessCheck *FlexibleAppVersionReadinessCheck `pulumi:"readinessCheck"`
	// Machine resources for a version.  Structure is documented below.
	Resources *FlexibleAppVersionResources `pulumi:"resources"`
	// Desired runtime. Example python27.
	Runtime *string `pulumi:"runtime"`
	// The version of the API in the given runtime environment.
	// Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
	RuntimeApiVersion *string `pulumi:"runtimeApiVersion"`
	// The channel of the runtime to use. Only available for some runtimes.
	RuntimeChannel *string `pulumi:"runtimeChannel"`
	// The path or name of the app's main executable.
	RuntimeMainExecutablePath *string `pulumi:"runtimeMainExecutablePath"`
	// AppEngine service resource
	Service *string `pulumi:"service"`
	// Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
	ServingStatus *string `pulumi:"servingStatus"`
	// Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens.
	// Reserved names,"default", "latest", and any name with the prefix "ah-".
	VersionId *string `pulumi:"versionId"`
	// Enables VPC connectivity for standard apps.  Structure is documented below.
	VpcAccessConnector *FlexibleAppVersionVpcAccessConnector `pulumi:"vpcAccessConnector"`
}

type FlexibleAppVersionState struct {
	// Serving configuration for Google Cloud Endpoints.  Structure is documented below.
	ApiConfig FlexibleAppVersionApiConfigPtrInput
	// Automatic scaling is based on request rate, response latencies, and other application metrics.  Structure is documented below.
	AutomaticScaling FlexibleAppVersionAutomaticScalingPtrInput
	// Metadata settings that are supplied to this version to enable beta runtime features.
	BetaSettings pulumi.StringMapInput
	// Duration that static files should be cached by web proxies and browsers.
	// Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time.
	DefaultExpiration pulumi.StringPtrInput
	// If set to `true`, the service will be deleted if it is the last version.
	DeleteServiceOnDestroy pulumi.BoolPtrInput
	// Code and application artifacts that make up this version.  Structure is documented below.
	Deployment FlexibleAppVersionDeploymentPtrInput
	// Code and application artifacts that make up this version.  Structure is documented below.
	EndpointsApiService FlexibleAppVersionEndpointsApiServicePtrInput
	// The entrypoint for the application.  Structure is documented below.
	Entrypoint FlexibleAppVersionEntrypointPtrInput
	// Environment variables available to the application.  As these are not returned in the API request, the provider will not detect any changes made outside of the config.
	EnvVariables pulumi.StringMapInput
	// An ordered list of URL-matching patterns that should be applied to incoming requests.
	// The first matching URL handles the request and other request handlers are not attempted.  Structure is documented below.
	Handlers FlexibleAppVersionHandlerArrayInput
	// Before an application can receive email or XMPP messages, the application must be configured to enable the service.
	InboundServices pulumi.StringArrayInput
	// Instance class that is used to run this version. Valid values are
	// AutomaticScaling: F1, F2, F4, F4_1G
	// ManualScaling: B1, B2, B4, B8, B4_1G
	// Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
	InstanceClass pulumi.StringPtrInput
	// Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.  Structure is documented below.
	LivenessCheck FlexibleAppVersionLivenessCheckPtrInput
	// A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.  Structure is documented below.
	ManualScaling FlexibleAppVersionManualScalingPtrInput
	// Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1.
	Name pulumi.StringPtrInput
	// Extra network settings  Structure is documented below.
	Network FlexibleAppVersionNetworkPtrInput
	// Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
	NobuildFilesRegex pulumi.StringPtrInput
	// If set to `true`, the application version will not be deleted.
	NoopOnDestroy pulumi.BoolPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.  Structure is documented below.
	ReadinessCheck FlexibleAppVersionReadinessCheckPtrInput
	// Machine resources for a version.  Structure is documented below.
	Resources FlexibleAppVersionResourcesPtrInput
	// Desired runtime. Example python27.
	Runtime pulumi.StringPtrInput
	// The version of the API in the given runtime environment.
	// Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
	RuntimeApiVersion pulumi.StringPtrInput
	// The channel of the runtime to use. Only available for some runtimes.
	RuntimeChannel pulumi.StringPtrInput
	// The path or name of the app's main executable.
	RuntimeMainExecutablePath pulumi.StringPtrInput
	// AppEngine service resource
	Service pulumi.StringPtrInput
	// Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
	ServingStatus pulumi.StringPtrInput
	// Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens.
	// Reserved names,"default", "latest", and any name with the prefix "ah-".
	VersionId pulumi.StringPtrInput
	// Enables VPC connectivity for standard apps.  Structure is documented below.
	VpcAccessConnector FlexibleAppVersionVpcAccessConnectorPtrInput
}

func (FlexibleAppVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*flexibleAppVersionState)(nil)).Elem()
}

type flexibleAppVersionArgs struct {
	// Serving configuration for Google Cloud Endpoints.  Structure is documented below.
	ApiConfig *FlexibleAppVersionApiConfig `pulumi:"apiConfig"`
	// Automatic scaling is based on request rate, response latencies, and other application metrics.  Structure is documented below.
	AutomaticScaling *FlexibleAppVersionAutomaticScaling `pulumi:"automaticScaling"`
	// Metadata settings that are supplied to this version to enable beta runtime features.
	BetaSettings map[string]string `pulumi:"betaSettings"`
	// Duration that static files should be cached by web proxies and browsers.
	// Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time.
	DefaultExpiration *string `pulumi:"defaultExpiration"`
	// If set to `true`, the service will be deleted if it is the last version.
	DeleteServiceOnDestroy *bool `pulumi:"deleteServiceOnDestroy"`
	// Code and application artifacts that make up this version.  Structure is documented below.
	Deployment *FlexibleAppVersionDeployment `pulumi:"deployment"`
	// Code and application artifacts that make up this version.  Structure is documented below.
	EndpointsApiService *FlexibleAppVersionEndpointsApiService `pulumi:"endpointsApiService"`
	// The entrypoint for the application.  Structure is documented below.
	Entrypoint *FlexibleAppVersionEntrypoint `pulumi:"entrypoint"`
	// Environment variables available to the application.  As these are not returned in the API request, the provider will not detect any changes made outside of the config.
	EnvVariables map[string]string `pulumi:"envVariables"`
	// An ordered list of URL-matching patterns that should be applied to incoming requests.
	// The first matching URL handles the request and other request handlers are not attempted.  Structure is documented below.
	Handlers []FlexibleAppVersionHandler `pulumi:"handlers"`
	// Before an application can receive email or XMPP messages, the application must be configured to enable the service.
	InboundServices []string `pulumi:"inboundServices"`
	// Instance class that is used to run this version. Valid values are
	// AutomaticScaling: F1, F2, F4, F4_1G
	// ManualScaling: B1, B2, B4, B8, B4_1G
	// Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
	InstanceClass *string `pulumi:"instanceClass"`
	// Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.  Structure is documented below.
	LivenessCheck FlexibleAppVersionLivenessCheck `pulumi:"livenessCheck"`
	// A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.  Structure is documented below.
	ManualScaling *FlexibleAppVersionManualScaling `pulumi:"manualScaling"`
	// Extra network settings  Structure is documented below.
	Network *FlexibleAppVersionNetwork `pulumi:"network"`
	// Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
	NobuildFilesRegex *string `pulumi:"nobuildFilesRegex"`
	// If set to `true`, the application version will not be deleted.
	NoopOnDestroy *bool `pulumi:"noopOnDestroy"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.  Structure is documented below.
	ReadinessCheck FlexibleAppVersionReadinessCheck `pulumi:"readinessCheck"`
	// Machine resources for a version.  Structure is documented below.
	Resources *FlexibleAppVersionResources `pulumi:"resources"`
	// Desired runtime. Example python27.
	Runtime string `pulumi:"runtime"`
	// The version of the API in the given runtime environment.
	// Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
	RuntimeApiVersion *string `pulumi:"runtimeApiVersion"`
	// The channel of the runtime to use. Only available for some runtimes.
	RuntimeChannel *string `pulumi:"runtimeChannel"`
	// The path or name of the app's main executable.
	RuntimeMainExecutablePath *string `pulumi:"runtimeMainExecutablePath"`
	// AppEngine service resource
	Service string `pulumi:"service"`
	// Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
	ServingStatus *string `pulumi:"servingStatus"`
	// Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens.
	// Reserved names,"default", "latest", and any name with the prefix "ah-".
	VersionId *string `pulumi:"versionId"`
	// Enables VPC connectivity for standard apps.  Structure is documented below.
	VpcAccessConnector *FlexibleAppVersionVpcAccessConnector `pulumi:"vpcAccessConnector"`
}

// The set of arguments for constructing a FlexibleAppVersion resource.
type FlexibleAppVersionArgs struct {
	// Serving configuration for Google Cloud Endpoints.  Structure is documented below.
	ApiConfig FlexibleAppVersionApiConfigPtrInput
	// Automatic scaling is based on request rate, response latencies, and other application metrics.  Structure is documented below.
	AutomaticScaling FlexibleAppVersionAutomaticScalingPtrInput
	// Metadata settings that are supplied to this version to enable beta runtime features.
	BetaSettings pulumi.StringMapInput
	// Duration that static files should be cached by web proxies and browsers.
	// Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time.
	DefaultExpiration pulumi.StringPtrInput
	// If set to `true`, the service will be deleted if it is the last version.
	DeleteServiceOnDestroy pulumi.BoolPtrInput
	// Code and application artifacts that make up this version.  Structure is documented below.
	Deployment FlexibleAppVersionDeploymentPtrInput
	// Code and application artifacts that make up this version.  Structure is documented below.
	EndpointsApiService FlexibleAppVersionEndpointsApiServicePtrInput
	// The entrypoint for the application.  Structure is documented below.
	Entrypoint FlexibleAppVersionEntrypointPtrInput
	// Environment variables available to the application.  As these are not returned in the API request, the provider will not detect any changes made outside of the config.
	EnvVariables pulumi.StringMapInput
	// An ordered list of URL-matching patterns that should be applied to incoming requests.
	// The first matching URL handles the request and other request handlers are not attempted.  Structure is documented below.
	Handlers FlexibleAppVersionHandlerArrayInput
	// Before an application can receive email or XMPP messages, the application must be configured to enable the service.
	InboundServices pulumi.StringArrayInput
	// Instance class that is used to run this version. Valid values are
	// AutomaticScaling: F1, F2, F4, F4_1G
	// ManualScaling: B1, B2, B4, B8, B4_1G
	// Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
	InstanceClass pulumi.StringPtrInput
	// Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.  Structure is documented below.
	LivenessCheck FlexibleAppVersionLivenessCheckInput
	// A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.  Structure is documented below.
	ManualScaling FlexibleAppVersionManualScalingPtrInput
	// Extra network settings  Structure is documented below.
	Network FlexibleAppVersionNetworkPtrInput
	// Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
	NobuildFilesRegex pulumi.StringPtrInput
	// If set to `true`, the application version will not be deleted.
	NoopOnDestroy pulumi.BoolPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.  Structure is documented below.
	ReadinessCheck FlexibleAppVersionReadinessCheckInput
	// Machine resources for a version.  Structure is documented below.
	Resources FlexibleAppVersionResourcesPtrInput
	// Desired runtime. Example python27.
	Runtime pulumi.StringInput
	// The version of the API in the given runtime environment.
	// Please see the app.yaml reference for valid values at https://cloud.google.com/appengine/docs/standard//config/appref
	RuntimeApiVersion pulumi.StringPtrInput
	// The channel of the runtime to use. Only available for some runtimes.
	RuntimeChannel pulumi.StringPtrInput
	// The path or name of the app's main executable.
	RuntimeMainExecutablePath pulumi.StringPtrInput
	// AppEngine service resource
	Service pulumi.StringInput
	// Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
	ServingStatus pulumi.StringPtrInput
	// Relative name of the version within the service. For example, `v1`. Version names can contain only lowercase letters, numbers, or hyphens.
	// Reserved names,"default", "latest", and any name with the prefix "ah-".
	VersionId pulumi.StringPtrInput
	// Enables VPC connectivity for standard apps.  Structure is documented below.
	VpcAccessConnector FlexibleAppVersionVpcAccessConnectorPtrInput
}

func (FlexibleAppVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*flexibleAppVersionArgs)(nil)).Elem()
}
