// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iap

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// ## Import
//
// For all import syntaxes, the "resource in question" can take any of the following forms* projects/{{project}}/iap_tunnel/zones/{{zone}}/instances/{{name}} * projects/{{project}}/zones/{{zone}}/instances/{{name}} * {{project}}/{{zone}}/{{name}} * {{zone}}/{{name}} * {{name}} Any variables not passed in the import command will be taken from the provider configuration. Identity-Aware Proxy tunnelinstance IAM resources can be imported using the resource identifiers, role, and member. IAM member imports use space-delimited identifiersthe resource in question, the role, and the member identity, e.g.
//
// ```sh
//  $ pulumi import gcp:iap/tunnelInstanceIAMPolicy:TunnelInstanceIAMPolicy editor "projects/{{project}}/iap_tunnel/zones/{{zone}}/instances/{{tunnel_instance}} roles/iap.tunnelResourceAccessor user:jane@example.com"
// ```
//
//  IAM binding imports use space-delimited identifiersthe resource in question and the role, e.g.
//
// ```sh
//  $ pulumi import gcp:iap/tunnelInstanceIAMPolicy:TunnelInstanceIAMPolicy editor "projects/{{project}}/iap_tunnel/zones/{{zone}}/instances/{{tunnel_instance}} roles/iap.tunnelResourceAccessor"
// ```
//
//  IAM policy imports use the identifier of the resource in question, e.g.
//
// ```sh
//  $ pulumi import gcp:iap/tunnelInstanceIAMPolicy:TunnelInstanceIAMPolicy editor projects/{{project}}/iap_tunnel/zones/{{zone}}/instances/{{tunnel_instance}}
// ```
//
//  -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the
//
// full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.
type TunnelInstanceIAMPolicy struct {
	pulumi.CustomResourceState

	// (Computed) The etag of the IAM policy.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Used to find the parent resource to bind the IAM policy to
	Instance pulumi.StringOutput `pulumi:"instance"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringOutput `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	Zone    pulumi.StringOutput `pulumi:"zone"`
}

// NewTunnelInstanceIAMPolicy registers a new resource with the given unique name, arguments, and options.
func NewTunnelInstanceIAMPolicy(ctx *pulumi.Context,
	name string, args *TunnelInstanceIAMPolicyArgs, opts ...pulumi.ResourceOption) (*TunnelInstanceIAMPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Instance == nil {
		return nil, errors.New("invalid value for required argument 'Instance'")
	}
	if args.PolicyData == nil {
		return nil, errors.New("invalid value for required argument 'PolicyData'")
	}
	var resource TunnelInstanceIAMPolicy
	err := ctx.RegisterResource("gcp:iap/tunnelInstanceIAMPolicy:TunnelInstanceIAMPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTunnelInstanceIAMPolicy gets an existing TunnelInstanceIAMPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTunnelInstanceIAMPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TunnelInstanceIAMPolicyState, opts ...pulumi.ResourceOption) (*TunnelInstanceIAMPolicy, error) {
	var resource TunnelInstanceIAMPolicy
	err := ctx.ReadResource("gcp:iap/tunnelInstanceIAMPolicy:TunnelInstanceIAMPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TunnelInstanceIAMPolicy resources.
type tunnelInstanceIAMPolicyState struct {
	// (Computed) The etag of the IAM policy.
	Etag *string `pulumi:"etag"`
	// Used to find the parent resource to bind the IAM policy to
	Instance *string `pulumi:"instance"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData *string `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	Zone    *string `pulumi:"zone"`
}

type TunnelInstanceIAMPolicyState struct {
	// (Computed) The etag of the IAM policy.
	Etag pulumi.StringPtrInput
	// Used to find the parent resource to bind the IAM policy to
	Instance pulumi.StringPtrInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	Zone    pulumi.StringPtrInput
}

func (TunnelInstanceIAMPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*tunnelInstanceIAMPolicyState)(nil)).Elem()
}

type tunnelInstanceIAMPolicyArgs struct {
	// Used to find the parent resource to bind the IAM policy to
	Instance string `pulumi:"instance"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData string `pulumi:"policyData"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	Zone    *string `pulumi:"zone"`
}

// The set of arguments for constructing a TunnelInstanceIAMPolicy resource.
type TunnelInstanceIAMPolicyArgs struct {
	// Used to find the parent resource to bind the IAM policy to
	Instance pulumi.StringInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	Zone    pulumi.StringPtrInput
}

func (TunnelInstanceIAMPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tunnelInstanceIAMPolicyArgs)(nil)).Elem()
}

type TunnelInstanceIAMPolicyInput interface {
	pulumi.Input

	ToTunnelInstanceIAMPolicyOutput() TunnelInstanceIAMPolicyOutput
	ToTunnelInstanceIAMPolicyOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyOutput
}

func (*TunnelInstanceIAMPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((*TunnelInstanceIAMPolicy)(nil))
}

func (i *TunnelInstanceIAMPolicy) ToTunnelInstanceIAMPolicyOutput() TunnelInstanceIAMPolicyOutput {
	return i.ToTunnelInstanceIAMPolicyOutputWithContext(context.Background())
}

func (i *TunnelInstanceIAMPolicy) ToTunnelInstanceIAMPolicyOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TunnelInstanceIAMPolicyOutput)
}

func (i *TunnelInstanceIAMPolicy) ToTunnelInstanceIAMPolicyPtrOutput() TunnelInstanceIAMPolicyPtrOutput {
	return i.ToTunnelInstanceIAMPolicyPtrOutputWithContext(context.Background())
}

func (i *TunnelInstanceIAMPolicy) ToTunnelInstanceIAMPolicyPtrOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TunnelInstanceIAMPolicyPtrOutput)
}

type TunnelInstanceIAMPolicyPtrInput interface {
	pulumi.Input

	ToTunnelInstanceIAMPolicyPtrOutput() TunnelInstanceIAMPolicyPtrOutput
	ToTunnelInstanceIAMPolicyPtrOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyPtrOutput
}

type tunnelInstanceIAMPolicyPtrType TunnelInstanceIAMPolicyArgs

func (*tunnelInstanceIAMPolicyPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**TunnelInstanceIAMPolicy)(nil))
}

func (i *tunnelInstanceIAMPolicyPtrType) ToTunnelInstanceIAMPolicyPtrOutput() TunnelInstanceIAMPolicyPtrOutput {
	return i.ToTunnelInstanceIAMPolicyPtrOutputWithContext(context.Background())
}

func (i *tunnelInstanceIAMPolicyPtrType) ToTunnelInstanceIAMPolicyPtrOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TunnelInstanceIAMPolicyPtrOutput)
}

// TunnelInstanceIAMPolicyArrayInput is an input type that accepts TunnelInstanceIAMPolicyArray and TunnelInstanceIAMPolicyArrayOutput values.
// You can construct a concrete instance of `TunnelInstanceIAMPolicyArrayInput` via:
//
//          TunnelInstanceIAMPolicyArray{ TunnelInstanceIAMPolicyArgs{...} }
type TunnelInstanceIAMPolicyArrayInput interface {
	pulumi.Input

	ToTunnelInstanceIAMPolicyArrayOutput() TunnelInstanceIAMPolicyArrayOutput
	ToTunnelInstanceIAMPolicyArrayOutputWithContext(context.Context) TunnelInstanceIAMPolicyArrayOutput
}

type TunnelInstanceIAMPolicyArray []TunnelInstanceIAMPolicyInput

func (TunnelInstanceIAMPolicyArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*TunnelInstanceIAMPolicy)(nil))
}

func (i TunnelInstanceIAMPolicyArray) ToTunnelInstanceIAMPolicyArrayOutput() TunnelInstanceIAMPolicyArrayOutput {
	return i.ToTunnelInstanceIAMPolicyArrayOutputWithContext(context.Background())
}

func (i TunnelInstanceIAMPolicyArray) ToTunnelInstanceIAMPolicyArrayOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TunnelInstanceIAMPolicyArrayOutput)
}

// TunnelInstanceIAMPolicyMapInput is an input type that accepts TunnelInstanceIAMPolicyMap and TunnelInstanceIAMPolicyMapOutput values.
// You can construct a concrete instance of `TunnelInstanceIAMPolicyMapInput` via:
//
//          TunnelInstanceIAMPolicyMap{ "key": TunnelInstanceIAMPolicyArgs{...} }
type TunnelInstanceIAMPolicyMapInput interface {
	pulumi.Input

	ToTunnelInstanceIAMPolicyMapOutput() TunnelInstanceIAMPolicyMapOutput
	ToTunnelInstanceIAMPolicyMapOutputWithContext(context.Context) TunnelInstanceIAMPolicyMapOutput
}

type TunnelInstanceIAMPolicyMap map[string]TunnelInstanceIAMPolicyInput

func (TunnelInstanceIAMPolicyMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*TunnelInstanceIAMPolicy)(nil))
}

func (i TunnelInstanceIAMPolicyMap) ToTunnelInstanceIAMPolicyMapOutput() TunnelInstanceIAMPolicyMapOutput {
	return i.ToTunnelInstanceIAMPolicyMapOutputWithContext(context.Background())
}

func (i TunnelInstanceIAMPolicyMap) ToTunnelInstanceIAMPolicyMapOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TunnelInstanceIAMPolicyMapOutput)
}

type TunnelInstanceIAMPolicyOutput struct {
	*pulumi.OutputState
}

func (TunnelInstanceIAMPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TunnelInstanceIAMPolicy)(nil))
}

func (o TunnelInstanceIAMPolicyOutput) ToTunnelInstanceIAMPolicyOutput() TunnelInstanceIAMPolicyOutput {
	return o
}

func (o TunnelInstanceIAMPolicyOutput) ToTunnelInstanceIAMPolicyOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyOutput {
	return o
}

func (o TunnelInstanceIAMPolicyOutput) ToTunnelInstanceIAMPolicyPtrOutput() TunnelInstanceIAMPolicyPtrOutput {
	return o.ToTunnelInstanceIAMPolicyPtrOutputWithContext(context.Background())
}

func (o TunnelInstanceIAMPolicyOutput) ToTunnelInstanceIAMPolicyPtrOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyPtrOutput {
	return o.ApplyT(func(v TunnelInstanceIAMPolicy) *TunnelInstanceIAMPolicy {
		return &v
	}).(TunnelInstanceIAMPolicyPtrOutput)
}

type TunnelInstanceIAMPolicyPtrOutput struct {
	*pulumi.OutputState
}

func (TunnelInstanceIAMPolicyPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TunnelInstanceIAMPolicy)(nil))
}

func (o TunnelInstanceIAMPolicyPtrOutput) ToTunnelInstanceIAMPolicyPtrOutput() TunnelInstanceIAMPolicyPtrOutput {
	return o
}

func (o TunnelInstanceIAMPolicyPtrOutput) ToTunnelInstanceIAMPolicyPtrOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyPtrOutput {
	return o
}

type TunnelInstanceIAMPolicyArrayOutput struct{ *pulumi.OutputState }

func (TunnelInstanceIAMPolicyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TunnelInstanceIAMPolicy)(nil))
}

func (o TunnelInstanceIAMPolicyArrayOutput) ToTunnelInstanceIAMPolicyArrayOutput() TunnelInstanceIAMPolicyArrayOutput {
	return o
}

func (o TunnelInstanceIAMPolicyArrayOutput) ToTunnelInstanceIAMPolicyArrayOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyArrayOutput {
	return o
}

func (o TunnelInstanceIAMPolicyArrayOutput) Index(i pulumi.IntInput) TunnelInstanceIAMPolicyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) TunnelInstanceIAMPolicy {
		return vs[0].([]TunnelInstanceIAMPolicy)[vs[1].(int)]
	}).(TunnelInstanceIAMPolicyOutput)
}

type TunnelInstanceIAMPolicyMapOutput struct{ *pulumi.OutputState }

func (TunnelInstanceIAMPolicyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]TunnelInstanceIAMPolicy)(nil))
}

func (o TunnelInstanceIAMPolicyMapOutput) ToTunnelInstanceIAMPolicyMapOutput() TunnelInstanceIAMPolicyMapOutput {
	return o
}

func (o TunnelInstanceIAMPolicyMapOutput) ToTunnelInstanceIAMPolicyMapOutputWithContext(ctx context.Context) TunnelInstanceIAMPolicyMapOutput {
	return o
}

func (o TunnelInstanceIAMPolicyMapOutput) MapIndex(k pulumi.StringInput) TunnelInstanceIAMPolicyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) TunnelInstanceIAMPolicy {
		return vs[0].(map[string]TunnelInstanceIAMPolicy)[vs[1].(string)]
	}).(TunnelInstanceIAMPolicyOutput)
}

func init() {
	pulumi.RegisterOutputType(TunnelInstanceIAMPolicyOutput{})
	pulumi.RegisterOutputType(TunnelInstanceIAMPolicyPtrOutput{})
	pulumi.RegisterOutputType(TunnelInstanceIAMPolicyArrayOutput{})
	pulumi.RegisterOutputType(TunnelInstanceIAMPolicyMapOutput{})
}
