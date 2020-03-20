// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package storage

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type BucketACL struct {
	pulumi.CustomResourceState

	// The name of the bucket it applies to.
	Bucket pulumi.StringOutput `pulumi:"bucket"`
	// Configure this ACL to be the default ACL.
	DefaultAcl pulumi.StringPtrOutput `pulumi:"defaultAcl"`
	// The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `roleEntity` is not.
	PredefinedAcl pulumi.StringPtrOutput `pulumi:"predefinedAcl"`
	// List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefinedAcl` is not.
	RoleEntities pulumi.StringArrayOutput `pulumi:"roleEntities"`
}

// NewBucketACL registers a new resource with the given unique name, arguments, and options.
func NewBucketACL(ctx *pulumi.Context,
	name string, args *BucketACLArgs, opts ...pulumi.ResourceOption) (*BucketACL, error) {
	if args == nil || args.Bucket == nil {
		return nil, errors.New("missing required argument 'Bucket'")
	}
	if args == nil {
		args = &BucketACLArgs{}
	}
	var resource BucketACL
	err := ctx.RegisterResource("gcp:storage/bucketACL:BucketACL", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBucketACL gets an existing BucketACL resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBucketACL(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BucketACLState, opts ...pulumi.ResourceOption) (*BucketACL, error) {
	var resource BucketACL
	err := ctx.ReadResource("gcp:storage/bucketACL:BucketACL", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BucketACL resources.
type bucketACLState struct {
	// The name of the bucket it applies to.
	Bucket *string `pulumi:"bucket"`
	// Configure this ACL to be the default ACL.
	DefaultAcl *string `pulumi:"defaultAcl"`
	// The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `roleEntity` is not.
	PredefinedAcl *string `pulumi:"predefinedAcl"`
	// List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefinedAcl` is not.
	RoleEntities []string `pulumi:"roleEntities"`
}

type BucketACLState struct {
	// The name of the bucket it applies to.
	Bucket pulumi.StringPtrInput
	// Configure this ACL to be the default ACL.
	DefaultAcl pulumi.StringPtrInput
	// The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `roleEntity` is not.
	PredefinedAcl pulumi.StringPtrInput
	// List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefinedAcl` is not.
	RoleEntities pulumi.StringArrayInput
}

func (BucketACLState) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketACLState)(nil)).Elem()
}

type bucketACLArgs struct {
	// The name of the bucket it applies to.
	Bucket string `pulumi:"bucket"`
	// Configure this ACL to be the default ACL.
	DefaultAcl *string `pulumi:"defaultAcl"`
	// The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `roleEntity` is not.
	PredefinedAcl *string `pulumi:"predefinedAcl"`
	// List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefinedAcl` is not.
	RoleEntities []string `pulumi:"roleEntities"`
}

// The set of arguments for constructing a BucketACL resource.
type BucketACLArgs struct {
	// The name of the bucket it applies to.
	Bucket pulumi.StringInput
	// Configure this ACL to be the default ACL.
	DefaultAcl pulumi.StringPtrInput
	// The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `roleEntity` is not.
	PredefinedAcl pulumi.StringPtrInput
	// List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefinedAcl` is not.
	RoleEntities pulumi.StringArrayInput
}

func (BucketACLArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketACLArgs)(nil)).Elem()
}
