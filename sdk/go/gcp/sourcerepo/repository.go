// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sourcerepo

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type Repository struct {
	pulumi.CustomResourceState

	// Resource name of the repository, of the form '{{repo}}'. The repo name may contain slashes. eg, 'name/with/slash'
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.
	PubsubConfigs RepositoryPubsubConfigArrayOutput `pulumi:"pubsubConfigs"`
	// The disk usage of the repo, in bytes.
	Size pulumi.IntOutput `pulumi:"size"`
	// URL to clone the repository from Google Cloud Source Repositories.
	Url pulumi.StringOutput `pulumi:"url"`
}

// NewRepository registers a new resource with the given unique name, arguments, and options.
func NewRepository(ctx *pulumi.Context,
	name string, args *RepositoryArgs, opts ...pulumi.ResourceOption) (*Repository, error) {
	if args == nil {
		args = &RepositoryArgs{}
	}
	var resource Repository
	err := ctx.RegisterResource("gcp:sourcerepo/repository:Repository", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRepository gets an existing Repository resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRepository(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RepositoryState, opts ...pulumi.ResourceOption) (*Repository, error) {
	var resource Repository
	err := ctx.ReadResource("gcp:sourcerepo/repository:Repository", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Repository resources.
type repositoryState struct {
	// Resource name of the repository, of the form '{{repo}}'. The repo name may contain slashes. eg, 'name/with/slash'
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.
	PubsubConfigs []RepositoryPubsubConfig `pulumi:"pubsubConfigs"`
	// The disk usage of the repo, in bytes.
	Size *int `pulumi:"size"`
	// URL to clone the repository from Google Cloud Source Repositories.
	Url *string `pulumi:"url"`
}

type RepositoryState struct {
	// Resource name of the repository, of the form '{{repo}}'. The repo name may contain slashes. eg, 'name/with/slash'
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.
	PubsubConfigs RepositoryPubsubConfigArrayInput
	// The disk usage of the repo, in bytes.
	Size pulumi.IntPtrInput
	// URL to clone the repository from Google Cloud Source Repositories.
	Url pulumi.StringPtrInput
}

func (RepositoryState) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryState)(nil)).Elem()
}

type repositoryArgs struct {
	// Resource name of the repository, of the form '{{repo}}'. The repo name may contain slashes. eg, 'name/with/slash'
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.
	PubsubConfigs []RepositoryPubsubConfig `pulumi:"pubsubConfigs"`
}

// The set of arguments for constructing a Repository resource.
type RepositoryArgs struct {
	// Resource name of the repository, of the form '{{repo}}'. The repo name may contain slashes. eg, 'name/with/slash'
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.
	PubsubConfigs RepositoryPubsubConfigArrayInput
}

func (RepositoryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryArgs)(nil)).Elem()
}
