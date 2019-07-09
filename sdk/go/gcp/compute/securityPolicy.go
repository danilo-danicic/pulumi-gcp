// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type SecurityPolicy struct {
	s *pulumi.ResourceState
}

// NewSecurityPolicy registers a new resource with the given unique name, arguments, and options.
func NewSecurityPolicy(ctx *pulumi.Context,
	name string, args *SecurityPolicyArgs, opts ...pulumi.ResourceOpt) (*SecurityPolicy, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["name"] = nil
		inputs["project"] = nil
		inputs["rules"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["project"] = args.Project
		inputs["rules"] = args.Rules
	}
	inputs["fingerprint"] = nil
	inputs["selfLink"] = nil
	s, err := ctx.RegisterResource("gcp:compute/securityPolicy:SecurityPolicy", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SecurityPolicy{s: s}, nil
}

// GetSecurityPolicy gets an existing SecurityPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecurityPolicy(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SecurityPolicyState, opts ...pulumi.ResourceOpt) (*SecurityPolicy, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["description"] = state.Description
		inputs["fingerprint"] = state.Fingerprint
		inputs["name"] = state.Name
		inputs["project"] = state.Project
		inputs["rules"] = state.Rules
		inputs["selfLink"] = state.SelfLink
	}
	s, err := ctx.ReadResource("gcp:compute/securityPolicy:SecurityPolicy", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SecurityPolicy{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *SecurityPolicy) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *SecurityPolicy) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// An optional description of this security policy. Max size is 2048.
func (r *SecurityPolicy) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// Fingerprint of this resource.
func (r *SecurityPolicy) Fingerprint() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["fingerprint"])
}

// The name of the security policy.
func (r *SecurityPolicy) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The project in which the resource belongs. If it
// is not provided, the provider project is used.
func (r *SecurityPolicy) Project() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["project"])
}

// The set of rules that belong to this policy. There must always be a default
// rule (rule with priority 2147483647 and match "\*"). If no rules are provided when creating a
// security policy, a default rule with action "allow" will be added. Structure is documented below.
func (r *SecurityPolicy) Rules() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["rules"])
}

// The URI of the created resource.
func (r *SecurityPolicy) SelfLink() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["selfLink"])
}

// Input properties used for looking up and filtering SecurityPolicy resources.
type SecurityPolicyState struct {
	// An optional description of this security policy. Max size is 2048.
	Description interface{}
	// Fingerprint of this resource.
	Fingerprint interface{}
	// The name of the security policy.
	Name interface{}
	// The project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project interface{}
	// The set of rules that belong to this policy. There must always be a default
	// rule (rule with priority 2147483647 and match "\*"). If no rules are provided when creating a
	// security policy, a default rule with action "allow" will be added. Structure is documented below.
	Rules interface{}
	// The URI of the created resource.
	SelfLink interface{}
}

// The set of arguments for constructing a SecurityPolicy resource.
type SecurityPolicyArgs struct {
	// An optional description of this security policy. Max size is 2048.
	Description interface{}
	// The name of the security policy.
	Name interface{}
	// The project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project interface{}
	// The set of rules that belong to this policy. There must always be a default
	// rule (rule with priority 2147483647 and match "\*"). If no rules are provided when creating a
	// security policy, a default rule with action "allow" will be added. Structure is documented below.
	Rules interface{}
}
