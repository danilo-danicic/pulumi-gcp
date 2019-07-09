// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package logging

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type FolderExclusion struct {
	s *pulumi.ResourceState
}

// NewFolderExclusion registers a new resource with the given unique name, arguments, and options.
func NewFolderExclusion(ctx *pulumi.Context,
	name string, args *FolderExclusionArgs, opts ...pulumi.ResourceOpt) (*FolderExclusion, error) {
	if args == nil || args.Filter == nil {
		return nil, errors.New("missing required argument 'Filter'")
	}
	if args == nil || args.Folder == nil {
		return nil, errors.New("missing required argument 'Folder'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["disabled"] = nil
		inputs["filter"] = nil
		inputs["folder"] = nil
		inputs["name"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["disabled"] = args.Disabled
		inputs["filter"] = args.Filter
		inputs["folder"] = args.Folder
		inputs["name"] = args.Name
	}
	s, err := ctx.RegisterResource("gcp:logging/folderExclusion:FolderExclusion", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &FolderExclusion{s: s}, nil
}

// GetFolderExclusion gets an existing FolderExclusion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFolderExclusion(ctx *pulumi.Context,
	name string, id pulumi.ID, state *FolderExclusionState, opts ...pulumi.ResourceOpt) (*FolderExclusion, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["description"] = state.Description
		inputs["disabled"] = state.Disabled
		inputs["filter"] = state.Filter
		inputs["folder"] = state.Folder
		inputs["name"] = state.Name
	}
	s, err := ctx.ReadResource("gcp:logging/folderExclusion:FolderExclusion", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &FolderExclusion{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *FolderExclusion) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *FolderExclusion) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// A human-readable description.
func (r *FolderExclusion) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// Whether this exclusion rule should be disabled or not. This defaults to
// false.
func (r *FolderExclusion) Disabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["disabled"])
}

// The filter to apply when excluding logs. Only log entries that match the filter are excluded.
// See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
// write a filter.
func (r *FolderExclusion) Filter() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["filter"])
}

// The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
// accepted.
func (r *FolderExclusion) Folder() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["folder"])
}

// The name of the logging exclusion.
func (r *FolderExclusion) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Input properties used for looking up and filtering FolderExclusion resources.
type FolderExclusionState struct {
	// A human-readable description.
	Description interface{}
	// Whether this exclusion rule should be disabled or not. This defaults to
	// false.
	Disabled interface{}
	// The filter to apply when excluding logs. Only log entries that match the filter are excluded.
	// See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
	// write a filter.
	Filter interface{}
	// The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
	// accepted.
	Folder interface{}
	// The name of the logging exclusion.
	Name interface{}
}

// The set of arguments for constructing a FolderExclusion resource.
type FolderExclusionArgs struct {
	// A human-readable description.
	Description interface{}
	// Whether this exclusion rule should be disabled or not. This defaults to
	// false.
	Disabled interface{}
	// The filter to apply when excluding logs. Only log entries that match the filter are excluded.
	// See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
	// write a filter.
	Filter interface{}
	// The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
	// accepted.
	Folder interface{}
	// The name of the logging exclusion.
	Name interface{}
}
