// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package storage

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Three different resources help you manage your IAM policy for storage bucket. Each of these resources serves a different use case:
// 
// * `google_storage_bucket_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the storage bucket are preserved.
// * `google_storage_bucket_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the storage bucket are preserved.
// * `google_storage_bucket_iam_policy`: Setting a policy removes all other permissions on the bucket, and if done incorrectly, there's a real chance you will lock yourself out of the bucket. If possible for your use case, using multiple google_storage_bucket_iam_binding resources will be much safer. See the usage example on how to work with policy correctly.
// 
// 
// ~> **Note:** `google_storage_bucket_iam_binding` resources **can be** used in conjunction with `google_storage_bucket_iam_member` resources **only if** they do not grant privilege to the same role.
type BucketIAMMember struct {
	s *pulumi.ResourceState
}

// NewBucketIAMMember registers a new resource with the given unique name, arguments, and options.
func NewBucketIAMMember(ctx *pulumi.Context,
	name string, args *BucketIAMMemberArgs, opts ...pulumi.ResourceOpt) (*BucketIAMMember, error) {
	if args == nil || args.Bucket == nil {
		return nil, errors.New("missing required argument 'Bucket'")
	}
	if args == nil || args.Member == nil {
		return nil, errors.New("missing required argument 'Member'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["bucket"] = nil
		inputs["member"] = nil
		inputs["role"] = nil
	} else {
		inputs["bucket"] = args.Bucket
		inputs["member"] = args.Member
		inputs["role"] = args.Role
	}
	inputs["etag"] = nil
	s, err := ctx.RegisterResource("gcp:storage/bucketIAMMember:BucketIAMMember", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &BucketIAMMember{s: s}, nil
}

// GetBucketIAMMember gets an existing BucketIAMMember resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBucketIAMMember(ctx *pulumi.Context,
	name string, id pulumi.ID, state *BucketIAMMemberState, opts ...pulumi.ResourceOpt) (*BucketIAMMember, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["bucket"] = state.Bucket
		inputs["etag"] = state.Etag
		inputs["member"] = state.Member
		inputs["role"] = state.Role
	}
	s, err := ctx.ReadResource("gcp:storage/bucketIAMMember:BucketIAMMember", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &BucketIAMMember{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *BucketIAMMember) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *BucketIAMMember) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The name of the bucket it applies to.
func (r *BucketIAMMember) Bucket() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bucket"])
}

// (Computed) The etag of the storage bucket's IAM policy.
func (r *BucketIAMMember) Etag() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["etag"])
}

func (r *BucketIAMMember) Member() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["member"])
}

// The role that should be applied. Note that custom roles must be of the format
// `[projects|organizations]/{parent-name}/roles/{role-name}`.
func (r *BucketIAMMember) Role() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["role"])
}

// Input properties used for looking up and filtering BucketIAMMember resources.
type BucketIAMMemberState struct {
	// The name of the bucket it applies to.
	Bucket interface{}
	// (Computed) The etag of the storage bucket's IAM policy.
	Etag interface{}
	Member interface{}
	// The role that should be applied. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role interface{}
}

// The set of arguments for constructing a BucketIAMMember resource.
type BucketIAMMemberArgs struct {
	// The name of the bucket it applies to.
	Bucket interface{}
	Member interface{}
	// The role that should be applied. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role interface{}
}
