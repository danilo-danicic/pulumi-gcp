// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package healthcare

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type DicomStoreIamBinding struct {
	pulumi.CustomResourceState

	Condition DicomStoreIamBindingConditionPtrOutput `pulumi:"condition"`
	// The DICOM store ID, in the form
	// `{project_id}/{location_name}/{dataset_name}/{dicom_store_name}` or
	// `{location_name}/{dataset_name}/{dicom_store_name}`. In the second form, the provider's
	// project setting will be used as a fallback.
	DicomStoreId pulumi.StringOutput `pulumi:"dicomStoreId"`
	// (Computed) The etag of the DICOM store's IAM policy.
	Etag    pulumi.StringOutput      `pulumi:"etag"`
	Members pulumi.StringArrayOutput `pulumi:"members"`
	// The role that should be applied. Only one
	// `healthcare.DicomStoreIamBinding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role pulumi.StringOutput `pulumi:"role"`
}

// NewDicomStoreIamBinding registers a new resource with the given unique name, arguments, and options.
func NewDicomStoreIamBinding(ctx *pulumi.Context,
	name string, args *DicomStoreIamBindingArgs, opts ...pulumi.ResourceOption) (*DicomStoreIamBinding, error) {
	if args == nil || args.DicomStoreId == nil {
		return nil, errors.New("missing required argument 'DicomStoreId'")
	}
	if args == nil || args.Members == nil {
		return nil, errors.New("missing required argument 'Members'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	if args == nil {
		args = &DicomStoreIamBindingArgs{}
	}
	var resource DicomStoreIamBinding
	err := ctx.RegisterResource("gcp:healthcare/dicomStoreIamBinding:DicomStoreIamBinding", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDicomStoreIamBinding gets an existing DicomStoreIamBinding resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDicomStoreIamBinding(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DicomStoreIamBindingState, opts ...pulumi.ResourceOption) (*DicomStoreIamBinding, error) {
	var resource DicomStoreIamBinding
	err := ctx.ReadResource("gcp:healthcare/dicomStoreIamBinding:DicomStoreIamBinding", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DicomStoreIamBinding resources.
type dicomStoreIamBindingState struct {
	Condition *DicomStoreIamBindingCondition `pulumi:"condition"`
	// The DICOM store ID, in the form
	// `{project_id}/{location_name}/{dataset_name}/{dicom_store_name}` or
	// `{location_name}/{dataset_name}/{dicom_store_name}`. In the second form, the provider's
	// project setting will be used as a fallback.
	DicomStoreId *string `pulumi:"dicomStoreId"`
	// (Computed) The etag of the DICOM store's IAM policy.
	Etag    *string  `pulumi:"etag"`
	Members []string `pulumi:"members"`
	// The role that should be applied. Only one
	// `healthcare.DicomStoreIamBinding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role *string `pulumi:"role"`
}

type DicomStoreIamBindingState struct {
	Condition DicomStoreIamBindingConditionPtrInput
	// The DICOM store ID, in the form
	// `{project_id}/{location_name}/{dataset_name}/{dicom_store_name}` or
	// `{location_name}/{dataset_name}/{dicom_store_name}`. In the second form, the provider's
	// project setting will be used as a fallback.
	DicomStoreId pulumi.StringPtrInput
	// (Computed) The etag of the DICOM store's IAM policy.
	Etag    pulumi.StringPtrInput
	Members pulumi.StringArrayInput
	// The role that should be applied. Only one
	// `healthcare.DicomStoreIamBinding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role pulumi.StringPtrInput
}

func (DicomStoreIamBindingState) ElementType() reflect.Type {
	return reflect.TypeOf((*dicomStoreIamBindingState)(nil)).Elem()
}

type dicomStoreIamBindingArgs struct {
	Condition *DicomStoreIamBindingCondition `pulumi:"condition"`
	// The DICOM store ID, in the form
	// `{project_id}/{location_name}/{dataset_name}/{dicom_store_name}` or
	// `{location_name}/{dataset_name}/{dicom_store_name}`. In the second form, the provider's
	// project setting will be used as a fallback.
	DicomStoreId string   `pulumi:"dicomStoreId"`
	Members      []string `pulumi:"members"`
	// The role that should be applied. Only one
	// `healthcare.DicomStoreIamBinding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role string `pulumi:"role"`
}

// The set of arguments for constructing a DicomStoreIamBinding resource.
type DicomStoreIamBindingArgs struct {
	Condition DicomStoreIamBindingConditionPtrInput
	// The DICOM store ID, in the form
	// `{project_id}/{location_name}/{dataset_name}/{dicom_store_name}` or
	// `{location_name}/{dataset_name}/{dicom_store_name}`. In the second form, the provider's
	// project setting will be used as a fallback.
	DicomStoreId pulumi.StringInput
	Members      pulumi.StringArrayInput
	// The role that should be applied. Only one
	// `healthcare.DicomStoreIamBinding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role pulumi.StringInput
}

func (DicomStoreIamBindingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dicomStoreIamBindingArgs)(nil)).Elem()
}
