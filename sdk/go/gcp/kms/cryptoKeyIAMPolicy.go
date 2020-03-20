// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package kms

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type CryptoKeyIAMPolicy struct {
	pulumi.CustomResourceState

	// The crypto key ID, in the form
	// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
	// `{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
	// the provider's project setting will be used as a fallback.
	CryptoKeyId pulumi.StringOutput `pulumi:"cryptoKeyId"`
	// (Computed) The etag of the project's IAM policy.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringOutput `pulumi:"policyData"`
}

// NewCryptoKeyIAMPolicy registers a new resource with the given unique name, arguments, and options.
func NewCryptoKeyIAMPolicy(ctx *pulumi.Context,
	name string, args *CryptoKeyIAMPolicyArgs, opts ...pulumi.ResourceOption) (*CryptoKeyIAMPolicy, error) {
	if args == nil || args.CryptoKeyId == nil {
		return nil, errors.New("missing required argument 'CryptoKeyId'")
	}
	if args == nil || args.PolicyData == nil {
		return nil, errors.New("missing required argument 'PolicyData'")
	}
	if args == nil {
		args = &CryptoKeyIAMPolicyArgs{}
	}
	var resource CryptoKeyIAMPolicy
	err := ctx.RegisterResource("gcp:kms/cryptoKeyIAMPolicy:CryptoKeyIAMPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCryptoKeyIAMPolicy gets an existing CryptoKeyIAMPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCryptoKeyIAMPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CryptoKeyIAMPolicyState, opts ...pulumi.ResourceOption) (*CryptoKeyIAMPolicy, error) {
	var resource CryptoKeyIAMPolicy
	err := ctx.ReadResource("gcp:kms/cryptoKeyIAMPolicy:CryptoKeyIAMPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CryptoKeyIAMPolicy resources.
type cryptoKeyIAMPolicyState struct {
	// The crypto key ID, in the form
	// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
	// `{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
	// the provider's project setting will be used as a fallback.
	CryptoKeyId *string `pulumi:"cryptoKeyId"`
	// (Computed) The etag of the project's IAM policy.
	Etag *string `pulumi:"etag"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData *string `pulumi:"policyData"`
}

type CryptoKeyIAMPolicyState struct {
	// The crypto key ID, in the form
	// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
	// `{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
	// the provider's project setting will be used as a fallback.
	CryptoKeyId pulumi.StringPtrInput
	// (Computed) The etag of the project's IAM policy.
	Etag pulumi.StringPtrInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringPtrInput
}

func (CryptoKeyIAMPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*cryptoKeyIAMPolicyState)(nil)).Elem()
}

type cryptoKeyIAMPolicyArgs struct {
	// The crypto key ID, in the form
	// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
	// `{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
	// the provider's project setting will be used as a fallback.
	CryptoKeyId string `pulumi:"cryptoKeyId"`
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData string `pulumi:"policyData"`
}

// The set of arguments for constructing a CryptoKeyIAMPolicy resource.
type CryptoKeyIAMPolicyArgs struct {
	// The crypto key ID, in the form
	// `{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
	// `{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
	// the provider's project setting will be used as a fallback.
	CryptoKeyId pulumi.StringInput
	// The policy data generated by
	// a `organizations.getIAMPolicy` data source.
	PolicyData pulumi.StringInput
}

func (CryptoKeyIAMPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cryptoKeyIAMPolicyArgs)(nil)).Elem()
}
