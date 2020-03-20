// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package projects

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Allows creation and management of a Google Cloud Platform project.
//
// Projects created with this resource must be associated with an Organization.
// See the [Organization documentation](https://cloud.google.com/resource-manager/docs/quickstarts) for more details.
//
// The service account used to run this provider when creating a `organizations.Project`
// resource must have `roles/resourcemanager.projectCreator`. See the
// [Access Control for Organizations Using IAM](https://cloud.google.com/resource-manager/docs/access-control-org)
// doc for more information.
//
// Note that prior to 0.8.5, `organizations.Project` functioned like a data source,
// meaning any project referenced by it had to be created and managed outside
// this provider. As of 0.8.5, `organizations.Project` functions like any other
// resource, with this provider creating and managing the project. To replicate the old
// behavior, either:
//
// * Use the project ID directly in whatever is referencing the project, using the
//   [projects.IAMPolicy](https://www.terraform.io/docs/providers/google/r/google_project_iam.html)
//   to replace the old `policyData` property.
// * Use the [import](https://www.terraform.io/docs/import/usage.html) functionality
//   to import your pre-existing project into this provider, where it can be referenced and
//   used just like always, keeping in mind that this provider will attempt to undo any changes
//   made outside this provider.
//
// > It's important to note that any project resources that were added to your config
// prior to 0.8.5 will continue to function as they always have, and will not be managed by
// this provider. Only newly added projects are affected.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_project.html.markdown.
type UsageExportBucket struct {
	pulumi.CustomResourceState

	BucketName pulumi.StringOutput    `pulumi:"bucketName"`
	Prefix     pulumi.StringPtrOutput `pulumi:"prefix"`
	Project    pulumi.StringOutput    `pulumi:"project"`
}

// NewUsageExportBucket registers a new resource with the given unique name, arguments, and options.
func NewUsageExportBucket(ctx *pulumi.Context,
	name string, args *UsageExportBucketArgs, opts ...pulumi.ResourceOption) (*UsageExportBucket, error) {
	if args == nil || args.BucketName == nil {
		return nil, errors.New("missing required argument 'BucketName'")
	}
	if args == nil {
		args = &UsageExportBucketArgs{}
	}
	var resource UsageExportBucket
	err := ctx.RegisterResource("gcp:projects/usageExportBucket:UsageExportBucket", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUsageExportBucket gets an existing UsageExportBucket resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUsageExportBucket(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UsageExportBucketState, opts ...pulumi.ResourceOption) (*UsageExportBucket, error) {
	var resource UsageExportBucket
	err := ctx.ReadResource("gcp:projects/usageExportBucket:UsageExportBucket", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UsageExportBucket resources.
type usageExportBucketState struct {
	BucketName *string `pulumi:"bucketName"`
	Prefix     *string `pulumi:"prefix"`
	Project    *string `pulumi:"project"`
}

type UsageExportBucketState struct {
	BucketName pulumi.StringPtrInput
	Prefix     pulumi.StringPtrInput
	Project    pulumi.StringPtrInput
}

func (UsageExportBucketState) ElementType() reflect.Type {
	return reflect.TypeOf((*usageExportBucketState)(nil)).Elem()
}

type usageExportBucketArgs struct {
	BucketName string  `pulumi:"bucketName"`
	Prefix     *string `pulumi:"prefix"`
	Project    *string `pulumi:"project"`
}

// The set of arguments for constructing a UsageExportBucket resource.
type UsageExportBucketArgs struct {
	BucketName pulumi.StringInput
	Prefix     pulumi.StringPtrInput
	Project    pulumi.StringPtrInput
}

func (UsageExportBucketArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*usageExportBucketArgs)(nil)).Elem()
}
