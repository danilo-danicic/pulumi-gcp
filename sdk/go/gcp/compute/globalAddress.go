// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type GlobalAddress struct {
	s *pulumi.ResourceState
}

// NewGlobalAddress registers a new resource with the given unique name, arguments, and options.
func NewGlobalAddress(ctx *pulumi.Context,
	name string, args *GlobalAddressArgs, opts ...pulumi.ResourceOpt) (*GlobalAddress, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["addressType"] = nil
		inputs["description"] = nil
		inputs["ipVersion"] = nil
		inputs["labels"] = nil
		inputs["name"] = nil
		inputs["network"] = nil
		inputs["prefixLength"] = nil
		inputs["project"] = nil
		inputs["purpose"] = nil
	} else {
		inputs["addressType"] = args.AddressType
		inputs["description"] = args.Description
		inputs["ipVersion"] = args.IpVersion
		inputs["labels"] = args.Labels
		inputs["name"] = args.Name
		inputs["network"] = args.Network
		inputs["prefixLength"] = args.PrefixLength
		inputs["project"] = args.Project
		inputs["purpose"] = args.Purpose
	}
	inputs["address"] = nil
	inputs["creationTimestamp"] = nil
	inputs["labelFingerprint"] = nil
	inputs["selfLink"] = nil
	s, err := ctx.RegisterResource("gcp:compute/globalAddress:GlobalAddress", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GlobalAddress{s: s}, nil
}

// GetGlobalAddress gets an existing GlobalAddress resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGlobalAddress(ctx *pulumi.Context,
	name string, id pulumi.ID, state *GlobalAddressState, opts ...pulumi.ResourceOpt) (*GlobalAddress, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["address"] = state.Address
		inputs["addressType"] = state.AddressType
		inputs["creationTimestamp"] = state.CreationTimestamp
		inputs["description"] = state.Description
		inputs["ipVersion"] = state.IpVersion
		inputs["labelFingerprint"] = state.LabelFingerprint
		inputs["labels"] = state.Labels
		inputs["name"] = state.Name
		inputs["network"] = state.Network
		inputs["prefixLength"] = state.PrefixLength
		inputs["project"] = state.Project
		inputs["purpose"] = state.Purpose
		inputs["selfLink"] = state.SelfLink
	}
	s, err := ctx.ReadResource("gcp:compute/globalAddress:GlobalAddress", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GlobalAddress{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *GlobalAddress) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *GlobalAddress) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *GlobalAddress) Address() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["address"])
}

func (r *GlobalAddress) AddressType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["addressType"])
}

func (r *GlobalAddress) CreationTimestamp() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["creationTimestamp"])
}

func (r *GlobalAddress) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

func (r *GlobalAddress) IpVersion() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["ipVersion"])
}

func (r *GlobalAddress) LabelFingerprint() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["labelFingerprint"])
}

func (r *GlobalAddress) Labels() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["labels"])
}

func (r *GlobalAddress) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

func (r *GlobalAddress) Network() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["network"])
}

func (r *GlobalAddress) PrefixLength() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["prefixLength"])
}

// The ID of the project in which the resource belongs.
// If it is not provided, the provider project is used.
func (r *GlobalAddress) Project() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["project"])
}

func (r *GlobalAddress) Purpose() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["purpose"])
}

// The URI of the created resource.
func (r *GlobalAddress) SelfLink() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["selfLink"])
}

// Input properties used for looking up and filtering GlobalAddress resources.
type GlobalAddressState struct {
	Address interface{}
	AddressType interface{}
	CreationTimestamp interface{}
	Description interface{}
	IpVersion interface{}
	LabelFingerprint interface{}
	Labels interface{}
	Name interface{}
	Network interface{}
	PrefixLength interface{}
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project interface{}
	Purpose interface{}
	// The URI of the created resource.
	SelfLink interface{}
}

// The set of arguments for constructing a GlobalAddress resource.
type GlobalAddressArgs struct {
	AddressType interface{}
	Description interface{}
	IpVersion interface{}
	Labels interface{}
	Name interface{}
	Network interface{}
	PrefixLength interface{}
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project interface{}
	Purpose interface{}
}
