// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type GatewayIamPolicy struct {
	pulumi.CustomResourceState

	// (Computed) The etag of the IAM policy.
	Etag    pulumi.StringOutput `pulumi:"etag"`
	Gateway pulumi.StringOutput `pulumi:"gateway"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringOutput `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The region of the gateway for the API.
	// Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
	// region is specified, it is taken from the provider configuration.
	Region pulumi.StringOutput `pulumi:"region"`
}

// NewGatewayIamPolicy registers a new resource with the given unique name, arguments, and options.
func NewGatewayIamPolicy(ctx *pulumi.Context,
	name string, args *GatewayIamPolicyArgs, opts ...pulumi.ResourceOption) (*GatewayIamPolicy, error) {
	if args == nil || args.Gateway == nil {
		return nil, errors.New("missing required argument 'Gateway'")
	}
	if args == nil || args.PolicyData == nil {
		return nil, errors.New("missing required argument 'PolicyData'")
	}
	if args == nil {
		args = &GatewayIamPolicyArgs{}
	}
	var resource GatewayIamPolicy
	err := ctx.RegisterResource("gcp:apigateway/gatewayIamPolicy:GatewayIamPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGatewayIamPolicy gets an existing GatewayIamPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGatewayIamPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GatewayIamPolicyState, opts ...pulumi.ResourceOption) (*GatewayIamPolicy, error) {
	var resource GatewayIamPolicy
	err := ctx.ReadResource("gcp:apigateway/gatewayIamPolicy:GatewayIamPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GatewayIamPolicy resources.
type gatewayIamPolicyState struct {
	// (Computed) The etag of the IAM policy.
	Etag    *string `pulumi:"etag"`
	Gateway *string `pulumi:"gateway"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData *string `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	// The region of the gateway for the API.
	// Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
	// region is specified, it is taken from the provider configuration.
	Region *string `pulumi:"region"`
}

type GatewayIamPolicyState struct {
	// (Computed) The etag of the IAM policy.
	Etag    pulumi.StringPtrInput
	Gateway pulumi.StringPtrInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	// The region of the gateway for the API.
	// Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
	// region is specified, it is taken from the provider configuration.
	Region pulumi.StringPtrInput
}

func (GatewayIamPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*gatewayIamPolicyState)(nil)).Elem()
}

type gatewayIamPolicyArgs struct {
	Gateway string `pulumi:"gateway"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData string `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	// The region of the gateway for the API.
	// Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
	// region is specified, it is taken from the provider configuration.
	Region *string `pulumi:"region"`
}

// The set of arguments for constructing a GatewayIamPolicy resource.
type GatewayIamPolicyArgs struct {
	Gateway pulumi.StringInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	// The region of the gateway for the API.
	// Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
	// region is specified, it is taken from the provider configuration.
	Region pulumi.StringPtrInput
}

func (GatewayIamPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*gatewayIamPolicyArgs)(nil)).Elem()
}
