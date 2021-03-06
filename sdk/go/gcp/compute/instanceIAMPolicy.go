// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// ## Import
//
// For all import syntaxes, the "resource in question" can take any of the following forms* projects/{{project}}/zones/{{zone}}/instances/{{name}} * {{project}}/{{zone}}/{{name}} * {{zone}}/{{name}} * {{name}} Any variables not passed in the import command will be taken from the provider configuration. Compute Engine instance IAM resources can be imported using the resource identifiers, role, and member. IAM member imports use space-delimited identifiersthe resource in question, the role, and the member identity, e.g.
//
// ```sh
//  $ pulumi import gcp:compute/instanceIAMPolicy:InstanceIAMPolicy editor "projects/{{project}}/zones/{{zone}}/instances/{{instance}} roles/compute.osLogin user:jane@example.com"
// ```
//
//  IAM binding imports use space-delimited identifiersthe resource in question and the role, e.g.
//
// ```sh
//  $ pulumi import gcp:compute/instanceIAMPolicy:InstanceIAMPolicy editor "projects/{{project}}/zones/{{zone}}/instances/{{instance}} roles/compute.osLogin"
// ```
//
//  IAM policy imports use the identifier of the resource in question, e.g.
//
// ```sh
//  $ pulumi import gcp:compute/instanceIAMPolicy:InstanceIAMPolicy editor projects/{{project}}/zones/{{zone}}/instances/{{instance}}
// ```
//
//  -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the
//
// full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.
type InstanceIAMPolicy struct {
	pulumi.CustomResourceState

	// (Computed) The etag of the IAM policy.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Used to find the parent resource to bind the IAM policy to
	InstanceName pulumi.StringOutput `pulumi:"instanceName"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringOutput `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
	// zone is specified, it is taken from the provider configuration.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewInstanceIAMPolicy registers a new resource with the given unique name, arguments, and options.
func NewInstanceIAMPolicy(ctx *pulumi.Context,
	name string, args *InstanceIAMPolicyArgs, opts ...pulumi.ResourceOption) (*InstanceIAMPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceName == nil {
		return nil, errors.New("invalid value for required argument 'InstanceName'")
	}
	if args.PolicyData == nil {
		return nil, errors.New("invalid value for required argument 'PolicyData'")
	}
	var resource InstanceIAMPolicy
	err := ctx.RegisterResource("gcp:compute/instanceIAMPolicy:InstanceIAMPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstanceIAMPolicy gets an existing InstanceIAMPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstanceIAMPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceIAMPolicyState, opts ...pulumi.ResourceOption) (*InstanceIAMPolicy, error) {
	var resource InstanceIAMPolicy
	err := ctx.ReadResource("gcp:compute/instanceIAMPolicy:InstanceIAMPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering InstanceIAMPolicy resources.
type instanceIAMPolicyState struct {
	// (Computed) The etag of the IAM policy.
	Etag *string `pulumi:"etag"`
	// Used to find the parent resource to bind the IAM policy to
	InstanceName *string `pulumi:"instanceName"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData *string `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
	// zone is specified, it is taken from the provider configuration.
	Zone *string `pulumi:"zone"`
}

type InstanceIAMPolicyState struct {
	// (Computed) The etag of the IAM policy.
	Etag pulumi.StringPtrInput
	// Used to find the parent resource to bind the IAM policy to
	InstanceName pulumi.StringPtrInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
	// zone is specified, it is taken from the provider configuration.
	Zone pulumi.StringPtrInput
}

func (InstanceIAMPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceIAMPolicyState)(nil)).Elem()
}

type instanceIAMPolicyArgs struct {
	// Used to find the parent resource to bind the IAM policy to
	InstanceName string `pulumi:"instanceName"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData string `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
	// zone is specified, it is taken from the provider configuration.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a InstanceIAMPolicy resource.
type InstanceIAMPolicyArgs struct {
	// Used to find the parent resource to bind the IAM policy to
	InstanceName pulumi.StringInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
	// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
	// zone is specified, it is taken from the provider configuration.
	Zone pulumi.StringPtrInput
}

func (InstanceIAMPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceIAMPolicyArgs)(nil)).Elem()
}

type InstanceIAMPolicyInput interface {
	pulumi.Input

	ToInstanceIAMPolicyOutput() InstanceIAMPolicyOutput
	ToInstanceIAMPolicyOutputWithContext(ctx context.Context) InstanceIAMPolicyOutput
}

func (*InstanceIAMPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceIAMPolicy)(nil))
}

func (i *InstanceIAMPolicy) ToInstanceIAMPolicyOutput() InstanceIAMPolicyOutput {
	return i.ToInstanceIAMPolicyOutputWithContext(context.Background())
}

func (i *InstanceIAMPolicy) ToInstanceIAMPolicyOutputWithContext(ctx context.Context) InstanceIAMPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceIAMPolicyOutput)
}

func (i *InstanceIAMPolicy) ToInstanceIAMPolicyPtrOutput() InstanceIAMPolicyPtrOutput {
	return i.ToInstanceIAMPolicyPtrOutputWithContext(context.Background())
}

func (i *InstanceIAMPolicy) ToInstanceIAMPolicyPtrOutputWithContext(ctx context.Context) InstanceIAMPolicyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceIAMPolicyPtrOutput)
}

type InstanceIAMPolicyPtrInput interface {
	pulumi.Input

	ToInstanceIAMPolicyPtrOutput() InstanceIAMPolicyPtrOutput
	ToInstanceIAMPolicyPtrOutputWithContext(ctx context.Context) InstanceIAMPolicyPtrOutput
}

type instanceIAMPolicyPtrType InstanceIAMPolicyArgs

func (*instanceIAMPolicyPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceIAMPolicy)(nil))
}

func (i *instanceIAMPolicyPtrType) ToInstanceIAMPolicyPtrOutput() InstanceIAMPolicyPtrOutput {
	return i.ToInstanceIAMPolicyPtrOutputWithContext(context.Background())
}

func (i *instanceIAMPolicyPtrType) ToInstanceIAMPolicyPtrOutputWithContext(ctx context.Context) InstanceIAMPolicyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceIAMPolicyPtrOutput)
}

// InstanceIAMPolicyArrayInput is an input type that accepts InstanceIAMPolicyArray and InstanceIAMPolicyArrayOutput values.
// You can construct a concrete instance of `InstanceIAMPolicyArrayInput` via:
//
//          InstanceIAMPolicyArray{ InstanceIAMPolicyArgs{...} }
type InstanceIAMPolicyArrayInput interface {
	pulumi.Input

	ToInstanceIAMPolicyArrayOutput() InstanceIAMPolicyArrayOutput
	ToInstanceIAMPolicyArrayOutputWithContext(context.Context) InstanceIAMPolicyArrayOutput
}

type InstanceIAMPolicyArray []InstanceIAMPolicyInput

func (InstanceIAMPolicyArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*InstanceIAMPolicy)(nil))
}

func (i InstanceIAMPolicyArray) ToInstanceIAMPolicyArrayOutput() InstanceIAMPolicyArrayOutput {
	return i.ToInstanceIAMPolicyArrayOutputWithContext(context.Background())
}

func (i InstanceIAMPolicyArray) ToInstanceIAMPolicyArrayOutputWithContext(ctx context.Context) InstanceIAMPolicyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceIAMPolicyArrayOutput)
}

// InstanceIAMPolicyMapInput is an input type that accepts InstanceIAMPolicyMap and InstanceIAMPolicyMapOutput values.
// You can construct a concrete instance of `InstanceIAMPolicyMapInput` via:
//
//          InstanceIAMPolicyMap{ "key": InstanceIAMPolicyArgs{...} }
type InstanceIAMPolicyMapInput interface {
	pulumi.Input

	ToInstanceIAMPolicyMapOutput() InstanceIAMPolicyMapOutput
	ToInstanceIAMPolicyMapOutputWithContext(context.Context) InstanceIAMPolicyMapOutput
}

type InstanceIAMPolicyMap map[string]InstanceIAMPolicyInput

func (InstanceIAMPolicyMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*InstanceIAMPolicy)(nil))
}

func (i InstanceIAMPolicyMap) ToInstanceIAMPolicyMapOutput() InstanceIAMPolicyMapOutput {
	return i.ToInstanceIAMPolicyMapOutputWithContext(context.Background())
}

func (i InstanceIAMPolicyMap) ToInstanceIAMPolicyMapOutputWithContext(ctx context.Context) InstanceIAMPolicyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceIAMPolicyMapOutput)
}

type InstanceIAMPolicyOutput struct {
	*pulumi.OutputState
}

func (InstanceIAMPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InstanceIAMPolicy)(nil))
}

func (o InstanceIAMPolicyOutput) ToInstanceIAMPolicyOutput() InstanceIAMPolicyOutput {
	return o
}

func (o InstanceIAMPolicyOutput) ToInstanceIAMPolicyOutputWithContext(ctx context.Context) InstanceIAMPolicyOutput {
	return o
}

func (o InstanceIAMPolicyOutput) ToInstanceIAMPolicyPtrOutput() InstanceIAMPolicyPtrOutput {
	return o.ToInstanceIAMPolicyPtrOutputWithContext(context.Background())
}

func (o InstanceIAMPolicyOutput) ToInstanceIAMPolicyPtrOutputWithContext(ctx context.Context) InstanceIAMPolicyPtrOutput {
	return o.ApplyT(func(v InstanceIAMPolicy) *InstanceIAMPolicy {
		return &v
	}).(InstanceIAMPolicyPtrOutput)
}

type InstanceIAMPolicyPtrOutput struct {
	*pulumi.OutputState
}

func (InstanceIAMPolicyPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceIAMPolicy)(nil))
}

func (o InstanceIAMPolicyPtrOutput) ToInstanceIAMPolicyPtrOutput() InstanceIAMPolicyPtrOutput {
	return o
}

func (o InstanceIAMPolicyPtrOutput) ToInstanceIAMPolicyPtrOutputWithContext(ctx context.Context) InstanceIAMPolicyPtrOutput {
	return o
}

type InstanceIAMPolicyArrayOutput struct{ *pulumi.OutputState }

func (InstanceIAMPolicyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]InstanceIAMPolicy)(nil))
}

func (o InstanceIAMPolicyArrayOutput) ToInstanceIAMPolicyArrayOutput() InstanceIAMPolicyArrayOutput {
	return o
}

func (o InstanceIAMPolicyArrayOutput) ToInstanceIAMPolicyArrayOutputWithContext(ctx context.Context) InstanceIAMPolicyArrayOutput {
	return o
}

func (o InstanceIAMPolicyArrayOutput) Index(i pulumi.IntInput) InstanceIAMPolicyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) InstanceIAMPolicy {
		return vs[0].([]InstanceIAMPolicy)[vs[1].(int)]
	}).(InstanceIAMPolicyOutput)
}

type InstanceIAMPolicyMapOutput struct{ *pulumi.OutputState }

func (InstanceIAMPolicyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]InstanceIAMPolicy)(nil))
}

func (o InstanceIAMPolicyMapOutput) ToInstanceIAMPolicyMapOutput() InstanceIAMPolicyMapOutput {
	return o
}

func (o InstanceIAMPolicyMapOutput) ToInstanceIAMPolicyMapOutputWithContext(ctx context.Context) InstanceIAMPolicyMapOutput {
	return o
}

func (o InstanceIAMPolicyMapOutput) MapIndex(k pulumi.StringInput) InstanceIAMPolicyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) InstanceIAMPolicy {
		return vs[0].(map[string]InstanceIAMPolicy)[vs[1].(string)]
	}).(InstanceIAMPolicyOutput)
}

func init() {
	pulumi.RegisterOutputType(InstanceIAMPolicyOutput{})
	pulumi.RegisterOutputType(InstanceIAMPolicyPtrOutput{})
	pulumi.RegisterOutputType(InstanceIAMPolicyArrayOutput{})
	pulumi.RegisterOutputType(InstanceIAMPolicyMapOutput{})
}
