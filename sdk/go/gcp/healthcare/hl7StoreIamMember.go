// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package healthcare

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// > **Warning:** These resources are in beta, and should be used with the terraform-provider-google-beta provider.
// See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta resources.
// 
// Three different resources help you manage your IAM policy for Healthcare HL7v2 store. Each of these resources serves a different use case:
// 
// * `google_healthcare_hl7_v2_store_iam_policy`: Authoritative. Sets the IAM policy for the HL7v2 store and replaces any existing policy already attached.
// * `google_healthcare_hl7_v2_store_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the HL7v2 store are preserved.
// * `google_healthcare_hl7_v2_store_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the HL7v2 store are preserved.
// 
// > **Note:** `google_healthcare_hl7_v2_store_iam_policy` **cannot** be used in conjunction with `google_healthcare_hl7_v2_store_iam_binding` and `google_healthcare_hl7_v2_store_iam_member` or they will fight over what your policy should be.
// 
// > **Note:** `google_healthcare_hl7_v2_store_iam_binding` resources **can be** used in conjunction with `google_healthcare_hl7_v2_store_iam_member` resources **only if** they do not grant privilege to the same role.
type Hl7StoreIamMember struct {
	s *pulumi.ResourceState
}

// NewHl7StoreIamMember registers a new resource with the given unique name, arguments, and options.
func NewHl7StoreIamMember(ctx *pulumi.Context,
	name string, args *Hl7StoreIamMemberArgs, opts ...pulumi.ResourceOpt) (*Hl7StoreIamMember, error) {
	if args == nil || args.Hl7V2StoreId == nil {
		return nil, errors.New("missing required argument 'Hl7V2StoreId'")
	}
	if args == nil || args.Member == nil {
		return nil, errors.New("missing required argument 'Member'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["hl7V2StoreId"] = nil
		inputs["member"] = nil
		inputs["role"] = nil
	} else {
		inputs["hl7V2StoreId"] = args.Hl7V2StoreId
		inputs["member"] = args.Member
		inputs["role"] = args.Role
	}
	inputs["etag"] = nil
	s, err := ctx.RegisterResource("gcp:healthcare/hl7StoreIamMember:Hl7StoreIamMember", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Hl7StoreIamMember{s: s}, nil
}

// GetHl7StoreIamMember gets an existing Hl7StoreIamMember resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHl7StoreIamMember(ctx *pulumi.Context,
	name string, id pulumi.ID, state *Hl7StoreIamMemberState, opts ...pulumi.ResourceOpt) (*Hl7StoreIamMember, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["etag"] = state.Etag
		inputs["hl7V2StoreId"] = state.Hl7V2StoreId
		inputs["member"] = state.Member
		inputs["role"] = state.Role
	}
	s, err := ctx.ReadResource("gcp:healthcare/hl7StoreIamMember:Hl7StoreIamMember", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Hl7StoreIamMember{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Hl7StoreIamMember) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Hl7StoreIamMember) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// (Computed) The etag of the HL7v2 store's IAM policy.
func (r *Hl7StoreIamMember) Etag() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["etag"])
}

// The HL7v2 store ID, in the form
// `{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}` or
// `{location_name}/{dataset_name}/{hl7_v2_store_name}`. In the second form, the provider's
// project setting will be used as a fallback.
func (r *Hl7StoreIamMember) Hl7V2StoreId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["hl7V2StoreId"])
}

func (r *Hl7StoreIamMember) Member() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["member"])
}

// The role that should be applied. Only one
// `google_healthcare_hl7_v2_store_iam_binding` can be used per role. Note that custom roles must be of the format
// `[projects|organizations]/{parent-name}/roles/{role-name}`.
func (r *Hl7StoreIamMember) Role() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["role"])
}

// Input properties used for looking up and filtering Hl7StoreIamMember resources.
type Hl7StoreIamMemberState struct {
	// (Computed) The etag of the HL7v2 store's IAM policy.
	Etag interface{}
	// The HL7v2 store ID, in the form
	// `{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}` or
	// `{location_name}/{dataset_name}/{hl7_v2_store_name}`. In the second form, the provider's
	// project setting will be used as a fallback.
	Hl7V2StoreId interface{}
	Member interface{}
	// The role that should be applied. Only one
	// `google_healthcare_hl7_v2_store_iam_binding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role interface{}
}

// The set of arguments for constructing a Hl7StoreIamMember resource.
type Hl7StoreIamMemberArgs struct {
	// The HL7v2 store ID, in the form
	// `{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}` or
	// `{location_name}/{dataset_name}/{hl7_v2_store_name}`. In the second form, the provider's
	// project setting will be used as a fallback.
	Hl7V2StoreId interface{}
	Member interface{}
	// The role that should be applied. Only one
	// `google_healthcare_hl7_v2_store_iam_binding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role interface{}
}