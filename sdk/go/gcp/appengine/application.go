// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package appengine

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Allows creation and management of an App Engine application.
//
// > App Engine applications cannot be deleted once they're created; you have to delete the
//    entire project to delete the application. This provider will report the application has been
//    successfully deleted; this is a limitation of this provider, and will go away in the future.
//    This provider is not able to delete App Engine applications.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_application.html.markdown.
type Application struct {
	pulumi.CustomResourceState

	// Identifier of the app, usually `{PROJECT_ID}`
	AppId pulumi.StringOutput `pulumi:"appId"`
	// The domain to authenticate users with when using App Engine's User API.
	AuthDomain pulumi.StringOutput `pulumi:"authDomain"`
	// The GCS bucket code is being stored in for this app.
	CodeBucket pulumi.StringOutput `pulumi:"codeBucket"`
	// The GCS bucket content is being stored in for this app.
	DefaultBucket pulumi.StringOutput `pulumi:"defaultBucket"`
	// The default hostname for this app.
	DefaultHostname pulumi.StringOutput `pulumi:"defaultHostname"`
	// A block of optional settings to configure specific App Engine features:
	FeatureSettings ApplicationFeatureSettingsOutput `pulumi:"featureSettings"`
	// The GCR domain used for storing managed Docker images for this app.
	GcrDomain pulumi.StringOutput `pulumi:"gcrDomain"`
	// Settings for enabling Cloud Identity Aware Proxy
	Iap ApplicationIapPtrOutput `pulumi:"iap"`
	// The [location](https://cloud.google.com/appengine/docs/locations)
	// to serve the app from.
	LocationId pulumi.StringOutput `pulumi:"locationId"`
	// Unique name of the app, usually `apps/{PROJECT_ID}`
	Name pulumi.StringOutput `pulumi:"name"`
	// The project ID to create the application under.
	// ~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
	// you may get a "Permission denied" error.
	Project pulumi.StringOutput `pulumi:"project"`
	// The serving status of the app.
	ServingStatus pulumi.StringOutput `pulumi:"servingStatus"`
	// A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
	UrlDispatchRules ApplicationUrlDispatchRuleArrayOutput `pulumi:"urlDispatchRules"`
}

// NewApplication registers a new resource with the given unique name, arguments, and options.
func NewApplication(ctx *pulumi.Context,
	name string, args *ApplicationArgs, opts ...pulumi.ResourceOption) (*Application, error) {
	if args == nil || args.LocationId == nil {
		return nil, errors.New("missing required argument 'LocationId'")
	}
	if args == nil {
		args = &ApplicationArgs{}
	}
	var resource Application
	err := ctx.RegisterResource("gcp:appengine/application:Application", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApplication gets an existing Application resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApplication(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApplicationState, opts ...pulumi.ResourceOption) (*Application, error) {
	var resource Application
	err := ctx.ReadResource("gcp:appengine/application:Application", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Application resources.
type applicationState struct {
	// Identifier of the app, usually `{PROJECT_ID}`
	AppId *string `pulumi:"appId"`
	// The domain to authenticate users with when using App Engine's User API.
	AuthDomain *string `pulumi:"authDomain"`
	// The GCS bucket code is being stored in for this app.
	CodeBucket *string `pulumi:"codeBucket"`
	// The GCS bucket content is being stored in for this app.
	DefaultBucket *string `pulumi:"defaultBucket"`
	// The default hostname for this app.
	DefaultHostname *string `pulumi:"defaultHostname"`
	// A block of optional settings to configure specific App Engine features:
	FeatureSettings *ApplicationFeatureSettings `pulumi:"featureSettings"`
	// The GCR domain used for storing managed Docker images for this app.
	GcrDomain *string `pulumi:"gcrDomain"`
	// Settings for enabling Cloud Identity Aware Proxy
	Iap *ApplicationIap `pulumi:"iap"`
	// The [location](https://cloud.google.com/appengine/docs/locations)
	// to serve the app from.
	LocationId *string `pulumi:"locationId"`
	// Unique name of the app, usually `apps/{PROJECT_ID}`
	Name *string `pulumi:"name"`
	// The project ID to create the application under.
	// ~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
	// you may get a "Permission denied" error.
	Project *string `pulumi:"project"`
	// The serving status of the app.
	ServingStatus *string `pulumi:"servingStatus"`
	// A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
	UrlDispatchRules []ApplicationUrlDispatchRule `pulumi:"urlDispatchRules"`
}

type ApplicationState struct {
	// Identifier of the app, usually `{PROJECT_ID}`
	AppId pulumi.StringPtrInput
	// The domain to authenticate users with when using App Engine's User API.
	AuthDomain pulumi.StringPtrInput
	// The GCS bucket code is being stored in for this app.
	CodeBucket pulumi.StringPtrInput
	// The GCS bucket content is being stored in for this app.
	DefaultBucket pulumi.StringPtrInput
	// The default hostname for this app.
	DefaultHostname pulumi.StringPtrInput
	// A block of optional settings to configure specific App Engine features:
	FeatureSettings ApplicationFeatureSettingsPtrInput
	// The GCR domain used for storing managed Docker images for this app.
	GcrDomain pulumi.StringPtrInput
	// Settings for enabling Cloud Identity Aware Proxy
	Iap ApplicationIapPtrInput
	// The [location](https://cloud.google.com/appengine/docs/locations)
	// to serve the app from.
	LocationId pulumi.StringPtrInput
	// Unique name of the app, usually `apps/{PROJECT_ID}`
	Name pulumi.StringPtrInput
	// The project ID to create the application under.
	// ~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
	// you may get a "Permission denied" error.
	Project pulumi.StringPtrInput
	// The serving status of the app.
	ServingStatus pulumi.StringPtrInput
	// A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
	UrlDispatchRules ApplicationUrlDispatchRuleArrayInput
}

func (ApplicationState) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationState)(nil)).Elem()
}

type applicationArgs struct {
	// The domain to authenticate users with when using App Engine's User API.
	AuthDomain *string `pulumi:"authDomain"`
	// A block of optional settings to configure specific App Engine features:
	FeatureSettings *ApplicationFeatureSettings `pulumi:"featureSettings"`
	// Settings for enabling Cloud Identity Aware Proxy
	Iap *ApplicationIap `pulumi:"iap"`
	// The [location](https://cloud.google.com/appengine/docs/locations)
	// to serve the app from.
	LocationId string `pulumi:"locationId"`
	// The project ID to create the application under.
	// ~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
	// you may get a "Permission denied" error.
	Project *string `pulumi:"project"`
	// The serving status of the app.
	ServingStatus *string `pulumi:"servingStatus"`
}

// The set of arguments for constructing a Application resource.
type ApplicationArgs struct {
	// The domain to authenticate users with when using App Engine's User API.
	AuthDomain pulumi.StringPtrInput
	// A block of optional settings to configure specific App Engine features:
	FeatureSettings ApplicationFeatureSettingsPtrInput
	// Settings for enabling Cloud Identity Aware Proxy
	Iap ApplicationIapPtrInput
	// The [location](https://cloud.google.com/appengine/docs/locations)
	// to serve the app from.
	LocationId pulumi.StringInput
	// The project ID to create the application under.
	// ~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
	// you may get a "Permission denied" error.
	Project pulumi.StringPtrInput
	// The serving status of the app.
	ServingStatus pulumi.StringPtrInput
}

func (ApplicationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationArgs)(nil)).Elem()
}
