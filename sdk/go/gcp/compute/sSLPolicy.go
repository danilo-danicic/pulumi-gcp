// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Represents a SSL policy. SSL policies give you the ability to control the
// features of SSL that your SSL proxy or HTTPS load balancer negotiates.
// 
// 
// To get more information about SslPolicy, see:
// 
// * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/sslPolicies)
// * How-to Guides
//     * [Using SSL Policies](https://cloud.google.com/compute/docs/load-balancing/ssl-policies)
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ssl_policy.html.markdown.
type SSLPolicy struct {
	s *pulumi.ResourceState
}

// NewSSLPolicy registers a new resource with the given unique name, arguments, and options.
func NewSSLPolicy(ctx *pulumi.Context,
	name string, args *SSLPolicyArgs, opts ...pulumi.ResourceOpt) (*SSLPolicy, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["customFeatures"] = nil
		inputs["description"] = nil
		inputs["minTlsVersion"] = nil
		inputs["name"] = nil
		inputs["profile"] = nil
		inputs["project"] = nil
	} else {
		inputs["customFeatures"] = args.CustomFeatures
		inputs["description"] = args.Description
		inputs["minTlsVersion"] = args.MinTlsVersion
		inputs["name"] = args.Name
		inputs["profile"] = args.Profile
		inputs["project"] = args.Project
	}
	inputs["creationTimestamp"] = nil
	inputs["enabledFeatures"] = nil
	inputs["fingerprint"] = nil
	inputs["selfLink"] = nil
	s, err := ctx.RegisterResource("gcp:compute/sSLPolicy:SSLPolicy", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SSLPolicy{s: s}, nil
}

// GetSSLPolicy gets an existing SSLPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSSLPolicy(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SSLPolicyState, opts ...pulumi.ResourceOpt) (*SSLPolicy, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["creationTimestamp"] = state.CreationTimestamp
		inputs["customFeatures"] = state.CustomFeatures
		inputs["description"] = state.Description
		inputs["enabledFeatures"] = state.EnabledFeatures
		inputs["fingerprint"] = state.Fingerprint
		inputs["minTlsVersion"] = state.MinTlsVersion
		inputs["name"] = state.Name
		inputs["profile"] = state.Profile
		inputs["project"] = state.Project
		inputs["selfLink"] = state.SelfLink
	}
	s, err := ctx.ReadResource("gcp:compute/sSLPolicy:SSLPolicy", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SSLPolicy{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *SSLPolicy) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *SSLPolicy) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *SSLPolicy) CreationTimestamp() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["creationTimestamp"])
}

func (r *SSLPolicy) CustomFeatures() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["customFeatures"])
}

func (r *SSLPolicy) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

func (r *SSLPolicy) EnabledFeatures() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["enabledFeatures"])
}

func (r *SSLPolicy) Fingerprint() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["fingerprint"])
}

func (r *SSLPolicy) MinTlsVersion() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["minTlsVersion"])
}

func (r *SSLPolicy) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

func (r *SSLPolicy) Profile() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["profile"])
}

// The ID of the project in which the resource belongs.
// If it is not provided, the provider project is used.
func (r *SSLPolicy) Project() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["project"])
}

// The URI of the created resource.
func (r *SSLPolicy) SelfLink() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["selfLink"])
}

// Input properties used for looking up and filtering SSLPolicy resources.
type SSLPolicyState struct {
	CreationTimestamp interface{}
	CustomFeatures interface{}
	Description interface{}
	EnabledFeatures interface{}
	Fingerprint interface{}
	MinTlsVersion interface{}
	Name interface{}
	Profile interface{}
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project interface{}
	// The URI of the created resource.
	SelfLink interface{}
}

// The set of arguments for constructing a SSLPolicy resource.
type SSLPolicyArgs struct {
	CustomFeatures interface{}
	Description interface{}
	MinTlsVersion interface{}
	Name interface{}
	Profile interface{}
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project interface{}
}
