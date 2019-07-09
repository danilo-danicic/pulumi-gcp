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
// > **Note:** `google_storage_bucket_iam_binding` resources **can be** used in conjunction with `google_storage_bucket_iam_member` resources **only if** they do not grant privilege to the same role.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/storage_bucket_iam_policy.html.markdown.
type BucketIAMPolicy struct {
	s *pulumi.ResourceState
}

// NewBucketIAMPolicy registers a new resource with the given unique name, arguments, and options.
func NewBucketIAMPolicy(ctx *pulumi.Context,
	name string, args *BucketIAMPolicyArgs, opts ...pulumi.ResourceOpt) (*BucketIAMPolicy, error) {
	if args == nil || args.Bucket == nil {
		return nil, errors.New("missing required argument 'Bucket'")
	}
	if args == nil || args.PolicyData == nil {
		return nil, errors.New("missing required argument 'PolicyData'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["bucket"] = nil
		inputs["policyData"] = nil
	} else {
		inputs["bucket"] = args.Bucket
		inputs["policyData"] = args.PolicyData
	}
	inputs["etag"] = nil
	s, err := ctx.RegisterResource("gcp:storage/bucketIAMPolicy:BucketIAMPolicy", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &BucketIAMPolicy{s: s}, nil
}

// GetBucketIAMPolicy gets an existing BucketIAMPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBucketIAMPolicy(ctx *pulumi.Context,
	name string, id pulumi.ID, state *BucketIAMPolicyState, opts ...pulumi.ResourceOpt) (*BucketIAMPolicy, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["bucket"] = state.Bucket
		inputs["etag"] = state.Etag
		inputs["policyData"] = state.PolicyData
	}
	s, err := ctx.ReadResource("gcp:storage/bucketIAMPolicy:BucketIAMPolicy", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &BucketIAMPolicy{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *BucketIAMPolicy) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *BucketIAMPolicy) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The name of the bucket it applies to.
func (r *BucketIAMPolicy) Bucket() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bucket"])
}

// (Computed) The etag of the storage bucket's IAM policy.
func (r *BucketIAMPolicy) Etag() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["etag"])
}

func (r *BucketIAMPolicy) PolicyData() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["policyData"])
}

// Input properties used for looking up and filtering BucketIAMPolicy resources.
type BucketIAMPolicyState struct {
	// The name of the bucket it applies to.
	Bucket interface{}
	// (Computed) The etag of the storage bucket's IAM policy.
	Etag interface{}
	PolicyData interface{}
}

// The set of arguments for constructing a BucketIAMPolicy resource.
type BucketIAMPolicyArgs struct {
	// The name of the bucket it applies to.
	Bucket interface{}
	PolicyData interface{}
}
