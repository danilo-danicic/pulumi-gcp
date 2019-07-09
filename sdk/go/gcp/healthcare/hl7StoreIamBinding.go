// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package healthcare

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type Hl7StoreIamBinding struct {
	s *pulumi.ResourceState
}

// NewHl7StoreIamBinding registers a new resource with the given unique name, arguments, and options.
func NewHl7StoreIamBinding(ctx *pulumi.Context,
	name string, args *Hl7StoreIamBindingArgs, opts ...pulumi.ResourceOpt) (*Hl7StoreIamBinding, error) {
	if args == nil || args.Hl7V2StoreId == nil {
		return nil, errors.New("missing required argument 'Hl7V2StoreId'")
	}
	if args == nil || args.Members == nil {
		return nil, errors.New("missing required argument 'Members'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["hl7V2StoreId"] = nil
		inputs["members"] = nil
		inputs["role"] = nil
	} else {
		inputs["hl7V2StoreId"] = args.Hl7V2StoreId
		inputs["members"] = args.Members
		inputs["role"] = args.Role
	}
	inputs["etag"] = nil
	s, err := ctx.RegisterResource("gcp:healthcare/hl7StoreIamBinding:Hl7StoreIamBinding", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Hl7StoreIamBinding{s: s}, nil
}

// GetHl7StoreIamBinding gets an existing Hl7StoreIamBinding resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHl7StoreIamBinding(ctx *pulumi.Context,
	name string, id pulumi.ID, state *Hl7StoreIamBindingState, opts ...pulumi.ResourceOpt) (*Hl7StoreIamBinding, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["etag"] = state.Etag
		inputs["hl7V2StoreId"] = state.Hl7V2StoreId
		inputs["members"] = state.Members
		inputs["role"] = state.Role
	}
	s, err := ctx.ReadResource("gcp:healthcare/hl7StoreIamBinding:Hl7StoreIamBinding", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Hl7StoreIamBinding{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Hl7StoreIamBinding) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Hl7StoreIamBinding) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// (Computed) The etag of the HL7v2 store's IAM policy.
func (r *Hl7StoreIamBinding) Etag() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["etag"])
}

// The HL7v2 store ID, in the form
// `{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}` or
// `{location_name}/{dataset_name}/{hl7_v2_store_name}`. In the second form, the provider's
// project setting will be used as a fallback.
func (r *Hl7StoreIamBinding) Hl7V2StoreId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["hl7V2StoreId"])
}

func (r *Hl7StoreIamBinding) Members() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["members"])
}

// The role that should be applied. Only one
// `google_healthcare_hl7_v2_store_iam_binding` can be used per role. Note that custom roles must be of the format
// `[projects|organizations]/{parent-name}/roles/{role-name}`.
func (r *Hl7StoreIamBinding) Role() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["role"])
}

// Input properties used for looking up and filtering Hl7StoreIamBinding resources.
type Hl7StoreIamBindingState struct {
	// (Computed) The etag of the HL7v2 store's IAM policy.
	Etag interface{}
	// The HL7v2 store ID, in the form
	// `{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}` or
	// `{location_name}/{dataset_name}/{hl7_v2_store_name}`. In the second form, the provider's
	// project setting will be used as a fallback.
	Hl7V2StoreId interface{}
	Members interface{}
	// The role that should be applied. Only one
	// `google_healthcare_hl7_v2_store_iam_binding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role interface{}
}

// The set of arguments for constructing a Hl7StoreIamBinding resource.
type Hl7StoreIamBindingArgs struct {
	// The HL7v2 store ID, in the form
	// `{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}` or
	// `{location_name}/{dataset_name}/{hl7_v2_store_name}`. In the second form, the provider's
	// project setting will be used as a fallback.
	Hl7V2StoreId interface{}
	Members interface{}
	// The role that should be applied. Only one
	// `google_healthcare_hl7_v2_store_iam_binding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role interface{}
}
