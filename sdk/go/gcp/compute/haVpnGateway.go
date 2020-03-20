// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type HaVpnGateway struct {
	pulumi.CustomResourceState

	// An optional description of this resource.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name pulumi.StringOutput `pulumi:"name"`
	// The network this VPN gateway is accepting traffic for.
	Network pulumi.StringOutput `pulumi:"network"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The region this gateway should sit in.
	Region pulumi.StringOutput `pulumi:"region"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// A list of interfaces on this VPN gateway.
	VpnInterfaces HaVpnGatewayVpnInterfaceArrayOutput `pulumi:"vpnInterfaces"`
}

// NewHaVpnGateway registers a new resource with the given unique name, arguments, and options.
func NewHaVpnGateway(ctx *pulumi.Context,
	name string, args *HaVpnGatewayArgs, opts ...pulumi.ResourceOption) (*HaVpnGateway, error) {
	if args == nil || args.Network == nil {
		return nil, errors.New("missing required argument 'Network'")
	}
	if args == nil {
		args = &HaVpnGatewayArgs{}
	}
	var resource HaVpnGateway
	err := ctx.RegisterResource("gcp:compute/haVpnGateway:HaVpnGateway", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHaVpnGateway gets an existing HaVpnGateway resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHaVpnGateway(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HaVpnGatewayState, opts ...pulumi.ResourceOption) (*HaVpnGateway, error) {
	var resource HaVpnGateway
	err := ctx.ReadResource("gcp:compute/haVpnGateway:HaVpnGateway", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HaVpnGateway resources.
type haVpnGatewayState struct {
	// An optional description of this resource.
	Description *string `pulumi:"description"`
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name *string `pulumi:"name"`
	// The network this VPN gateway is accepting traffic for.
	Network *string `pulumi:"network"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The region this gateway should sit in.
	Region *string `pulumi:"region"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// A list of interfaces on this VPN gateway.
	VpnInterfaces []HaVpnGatewayVpnInterface `pulumi:"vpnInterfaces"`
}

type HaVpnGatewayState struct {
	// An optional description of this resource.
	Description pulumi.StringPtrInput
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name pulumi.StringPtrInput
	// The network this VPN gateway is accepting traffic for.
	Network pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The region this gateway should sit in.
	Region pulumi.StringPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
	// A list of interfaces on this VPN gateway.
	VpnInterfaces HaVpnGatewayVpnInterfaceArrayInput
}

func (HaVpnGatewayState) ElementType() reflect.Type {
	return reflect.TypeOf((*haVpnGatewayState)(nil)).Elem()
}

type haVpnGatewayArgs struct {
	// An optional description of this resource.
	Description *string `pulumi:"description"`
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name *string `pulumi:"name"`
	// The network this VPN gateway is accepting traffic for.
	Network string `pulumi:"network"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The region this gateway should sit in.
	Region *string `pulumi:"region"`
}

// The set of arguments for constructing a HaVpnGateway resource.
type HaVpnGatewayArgs struct {
	// An optional description of this resource.
	Description pulumi.StringPtrInput
	// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
	// comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name pulumi.StringPtrInput
	// The network this VPN gateway is accepting traffic for.
	Network pulumi.StringInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The region this gateway should sit in.
	Region pulumi.StringPtrInput
}

func (HaVpnGatewayArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*haVpnGatewayArgs)(nil)).Elem()
}
