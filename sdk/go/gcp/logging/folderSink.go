// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package logging

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type FolderSink struct {
	pulumi.CustomResourceState

	// Options that affect sinks exporting data to BigQuery. Structure documented below.
	BigqueryOptions FolderSinkBigqueryOptionsOutput `pulumi:"bigqueryOptions"`
	// The destination of the sink (or, in other words, where logs are written to). Can be a
	// Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
	// The writer associated with the sink must have access to write to the above resource.
	Destination pulumi.StringOutput `pulumi:"destination"`
	// The filter to apply when exporting logs. Only log entries that match the filter are exported.
	// See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
	// write a filter.
	Filter pulumi.StringPtrOutput `pulumi:"filter"`
	// The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
	// accepted.
	Folder pulumi.StringOutput `pulumi:"folder"`
	// Whether or not to include children folders in the sink export. If true, logs
	// associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
	IncludeChildren pulumi.BoolPtrOutput `pulumi:"includeChildren"`
	// The name of the logging sink.
	Name pulumi.StringOutput `pulumi:"name"`
	// The identity associated with this sink. This identity must be granted write access to the
	// configured `destination`.
	WriterIdentity pulumi.StringOutput `pulumi:"writerIdentity"`
}

// NewFolderSink registers a new resource with the given unique name, arguments, and options.
func NewFolderSink(ctx *pulumi.Context,
	name string, args *FolderSinkArgs, opts ...pulumi.ResourceOption) (*FolderSink, error) {
	if args == nil || args.Destination == nil {
		return nil, errors.New("missing required argument 'Destination'")
	}
	if args == nil || args.Folder == nil {
		return nil, errors.New("missing required argument 'Folder'")
	}
	if args == nil {
		args = &FolderSinkArgs{}
	}
	var resource FolderSink
	err := ctx.RegisterResource("gcp:logging/folderSink:FolderSink", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFolderSink gets an existing FolderSink resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFolderSink(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FolderSinkState, opts ...pulumi.ResourceOption) (*FolderSink, error) {
	var resource FolderSink
	err := ctx.ReadResource("gcp:logging/folderSink:FolderSink", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FolderSink resources.
type folderSinkState struct {
	// Options that affect sinks exporting data to BigQuery. Structure documented below.
	BigqueryOptions *FolderSinkBigqueryOptions `pulumi:"bigqueryOptions"`
	// The destination of the sink (or, in other words, where logs are written to). Can be a
	// Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
	// The writer associated with the sink must have access to write to the above resource.
	Destination *string `pulumi:"destination"`
	// The filter to apply when exporting logs. Only log entries that match the filter are exported.
	// See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
	// write a filter.
	Filter *string `pulumi:"filter"`
	// The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
	// accepted.
	Folder *string `pulumi:"folder"`
	// Whether or not to include children folders in the sink export. If true, logs
	// associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
	IncludeChildren *bool `pulumi:"includeChildren"`
	// The name of the logging sink.
	Name *string `pulumi:"name"`
	// The identity associated with this sink. This identity must be granted write access to the
	// configured `destination`.
	WriterIdentity *string `pulumi:"writerIdentity"`
}

type FolderSinkState struct {
	// Options that affect sinks exporting data to BigQuery. Structure documented below.
	BigqueryOptions FolderSinkBigqueryOptionsPtrInput
	// The destination of the sink (or, in other words, where logs are written to). Can be a
	// Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
	// The writer associated with the sink must have access to write to the above resource.
	Destination pulumi.StringPtrInput
	// The filter to apply when exporting logs. Only log entries that match the filter are exported.
	// See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
	// write a filter.
	Filter pulumi.StringPtrInput
	// The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
	// accepted.
	Folder pulumi.StringPtrInput
	// Whether or not to include children folders in the sink export. If true, logs
	// associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
	IncludeChildren pulumi.BoolPtrInput
	// The name of the logging sink.
	Name pulumi.StringPtrInput
	// The identity associated with this sink. This identity must be granted write access to the
	// configured `destination`.
	WriterIdentity pulumi.StringPtrInput
}

func (FolderSinkState) ElementType() reflect.Type {
	return reflect.TypeOf((*folderSinkState)(nil)).Elem()
}

type folderSinkArgs struct {
	// Options that affect sinks exporting data to BigQuery. Structure documented below.
	BigqueryOptions *FolderSinkBigqueryOptions `pulumi:"bigqueryOptions"`
	// The destination of the sink (or, in other words, where logs are written to). Can be a
	// Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
	// The writer associated with the sink must have access to write to the above resource.
	Destination string `pulumi:"destination"`
	// The filter to apply when exporting logs. Only log entries that match the filter are exported.
	// See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
	// write a filter.
	Filter *string `pulumi:"filter"`
	// The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
	// accepted.
	Folder string `pulumi:"folder"`
	// Whether or not to include children folders in the sink export. If true, logs
	// associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
	IncludeChildren *bool `pulumi:"includeChildren"`
	// The name of the logging sink.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a FolderSink resource.
type FolderSinkArgs struct {
	// Options that affect sinks exporting data to BigQuery. Structure documented below.
	BigqueryOptions FolderSinkBigqueryOptionsPtrInput
	// The destination of the sink (or, in other words, where logs are written to). Can be a
	// Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
	// The writer associated with the sink must have access to write to the above resource.
	Destination pulumi.StringInput
	// The filter to apply when exporting logs. Only log entries that match the filter are exported.
	// See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
	// write a filter.
	Filter pulumi.StringPtrInput
	// The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
	// accepted.
	Folder pulumi.StringInput
	// Whether or not to include children folders in the sink export. If true, logs
	// associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
	IncludeChildren pulumi.BoolPtrInput
	// The name of the logging sink.
	Name pulumi.StringPtrInput
}

func (FolderSinkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*folderSinkArgs)(nil)).Elem()
}
