// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The Google Compute Engine Instance Group Manager API creates and manages pools
// of homogeneous Compute Engine virtual machine instances from a common instance
// template. For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/manager)
// and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroupManagers)
// 
// ~> **Note:** Use [google_compute_region_instance_group_manager](https://www.terraform.io/docs/providers/google/r/compute_region_instance_group_manager.html) to create a regional (multi-zone) instance group manager.
type InstanceGroupManager struct {
	s *pulumi.ResourceState
}

// NewInstanceGroupManager registers a new resource with the given unique name, arguments, and options.
func NewInstanceGroupManager(ctx *pulumi.Context,
	name string, args *InstanceGroupManagerArgs, opts ...pulumi.ResourceOpt) (*InstanceGroupManager, error) {
	if args == nil || args.BaseInstanceName == nil {
		return nil, errors.New("missing required argument 'BaseInstanceName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["autoHealingPolicies"] = nil
		inputs["baseInstanceName"] = nil
		inputs["description"] = nil
		inputs["instanceTemplate"] = nil
		inputs["name"] = nil
		inputs["namedPorts"] = nil
		inputs["project"] = nil
		inputs["rollingUpdatePolicy"] = nil
		inputs["targetPools"] = nil
		inputs["targetSize"] = nil
		inputs["updateStrategy"] = nil
		inputs["versions"] = nil
		inputs["waitForInstances"] = nil
		inputs["zone"] = nil
	} else {
		inputs["autoHealingPolicies"] = args.AutoHealingPolicies
		inputs["baseInstanceName"] = args.BaseInstanceName
		inputs["description"] = args.Description
		inputs["instanceTemplate"] = args.InstanceTemplate
		inputs["name"] = args.Name
		inputs["namedPorts"] = args.NamedPorts
		inputs["project"] = args.Project
		inputs["rollingUpdatePolicy"] = args.RollingUpdatePolicy
		inputs["targetPools"] = args.TargetPools
		inputs["targetSize"] = args.TargetSize
		inputs["updateStrategy"] = args.UpdateStrategy
		inputs["versions"] = args.Versions
		inputs["waitForInstances"] = args.WaitForInstances
		inputs["zone"] = args.Zone
	}
	inputs["fingerprint"] = nil
	inputs["instanceGroup"] = nil
	inputs["selfLink"] = nil
	s, err := ctx.RegisterResource("gcp:compute/instanceGroupManager:InstanceGroupManager", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &InstanceGroupManager{s: s}, nil
}

// GetInstanceGroupManager gets an existing InstanceGroupManager resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstanceGroupManager(ctx *pulumi.Context,
	name string, id pulumi.ID, state *InstanceGroupManagerState, opts ...pulumi.ResourceOpt) (*InstanceGroupManager, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["autoHealingPolicies"] = state.AutoHealingPolicies
		inputs["baseInstanceName"] = state.BaseInstanceName
		inputs["description"] = state.Description
		inputs["fingerprint"] = state.Fingerprint
		inputs["instanceGroup"] = state.InstanceGroup
		inputs["instanceTemplate"] = state.InstanceTemplate
		inputs["name"] = state.Name
		inputs["namedPorts"] = state.NamedPorts
		inputs["project"] = state.Project
		inputs["rollingUpdatePolicy"] = state.RollingUpdatePolicy
		inputs["selfLink"] = state.SelfLink
		inputs["targetPools"] = state.TargetPools
		inputs["targetSize"] = state.TargetSize
		inputs["updateStrategy"] = state.UpdateStrategy
		inputs["versions"] = state.Versions
		inputs["waitForInstances"] = state.WaitForInstances
		inputs["zone"] = state.Zone
	}
	s, err := ctx.ReadResource("gcp:compute/instanceGroupManager:InstanceGroupManager", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &InstanceGroupManager{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *InstanceGroupManager) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *InstanceGroupManager) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The autohealing policies for this managed instance
// group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).
// This property is in beta, and should be used with the terraform-provider-google-beta provider.
// See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta fields.
func (r *InstanceGroupManager) AutoHealingPolicies() *pulumi.Output {
	return r.s.State["autoHealingPolicies"]
}

// The base instance name to use for
// instances in this group. The value must be a valid
// [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
// are lowercase letters, numbers, and hyphens (-). Instances are named by
// appending a hyphen and a random four-character string to the base instance
// name.
func (r *InstanceGroupManager) BaseInstanceName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["baseInstanceName"])
}

// An optional textual description of the instance
// group manager.
func (r *InstanceGroupManager) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The fingerprint of the instance group manager.
func (r *InstanceGroupManager) Fingerprint() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["fingerprint"])
}

// The full URL of the instance group created by the manager.
func (r *InstanceGroupManager) InstanceGroup() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["instanceGroup"])
}

// - The full URL to an instance template from which all new instances of this version will be created.
func (r *InstanceGroupManager) InstanceTemplate() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["instanceTemplate"])
}

// - Version name.
func (r *InstanceGroupManager) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The named port configuration. See the section below
// for details on configuration.
func (r *InstanceGroupManager) NamedPorts() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["namedPorts"])
}

// The ID of the project in which the resource belongs. If it
// is not provided, the provider project is used.
func (r *InstanceGroupManager) Project() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["project"])
}

// The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch)
// This property is in beta, and should be used with the terraform-provider-google-beta provider.
// See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta fields.
// - - -
func (r *InstanceGroupManager) RollingUpdatePolicy() *pulumi.Output {
	return r.s.State["rollingUpdatePolicy"]
}

// The URL of the created resource.
func (r *InstanceGroupManager) SelfLink() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["selfLink"])
}

// The full URL of all target pools to which new
// instances in the group are added. Updating the target pools attribute does
// not affect existing instances.
func (r *InstanceGroupManager) TargetPools() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["targetPools"])
}

// - The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.
func (r *InstanceGroupManager) TargetSize() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["targetSize"])
}

// If the `instance_template`
// resource is modified, a value of `"NONE"` will prevent any of the managed
// instances from being restarted by Terraform. A value of `"REPLACE"` will
// restart all of the instances at once. `"ROLLING_UPDATE"` is supported as a beta feature.
// A value of `"ROLLING_UPDATE"` requires `rolling_update_policy` block to be set
func (r *InstanceGroupManager) UpdateStrategy() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["updateStrategy"])
}

// Application versions managed by this instance group. Each
// version deals with a specific instance template, allowing canary release scenarios.
// Conflicts with `instance_template`. Structure is documented below. Beware that
// exactly one version must not specify a target size. It means that versions with
// a target size will respect the setting, and the one without target size will
// be applied to all remaining Instances (top level target_size - each version target_size).
// This property is in beta, and should be used with the terraform-provider-google-beta provider.
// See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta fields.
func (r *InstanceGroupManager) Versions() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["versions"])
}

// Whether to wait for all instances to be created/updated before
// returning. Note that if this is set to true and the operation does not succeed, Terraform will
// continue trying until it times out.
func (r *InstanceGroupManager) WaitForInstances() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["waitForInstances"])
}

// The zone that instances in this group should be created
// in.
func (r *InstanceGroupManager) Zone() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["zone"])
}

// Input properties used for looking up and filtering InstanceGroupManager resources.
type InstanceGroupManagerState struct {
	// The autohealing policies for this managed instance
	// group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).
	// This property is in beta, and should be used with the terraform-provider-google-beta provider.
	// See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta fields.
	AutoHealingPolicies interface{}
	// The base instance name to use for
	// instances in this group. The value must be a valid
	// [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
	// are lowercase letters, numbers, and hyphens (-). Instances are named by
	// appending a hyphen and a random four-character string to the base instance
	// name.
	BaseInstanceName interface{}
	// An optional textual description of the instance
	// group manager.
	Description interface{}
	// The fingerprint of the instance group manager.
	Fingerprint interface{}
	// The full URL of the instance group created by the manager.
	InstanceGroup interface{}
	// - The full URL to an instance template from which all new instances of this version will be created.
	InstanceTemplate interface{}
	// - Version name.
	Name interface{}
	// The named port configuration. See the section below
	// for details on configuration.
	NamedPorts interface{}
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project interface{}
	// The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch)
	// This property is in beta, and should be used with the terraform-provider-google-beta provider.
	// See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta fields.
	// - - -
	RollingUpdatePolicy interface{}
	// The URL of the created resource.
	SelfLink interface{}
	// The full URL of all target pools to which new
	// instances in the group are added. Updating the target pools attribute does
	// not affect existing instances.
	TargetPools interface{}
	// - The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.
	TargetSize interface{}
	// If the `instance_template`
	// resource is modified, a value of `"NONE"` will prevent any of the managed
	// instances from being restarted by Terraform. A value of `"REPLACE"` will
	// restart all of the instances at once. `"ROLLING_UPDATE"` is supported as a beta feature.
	// A value of `"ROLLING_UPDATE"` requires `rolling_update_policy` block to be set
	UpdateStrategy interface{}
	// Application versions managed by this instance group. Each
	// version deals with a specific instance template, allowing canary release scenarios.
	// Conflicts with `instance_template`. Structure is documented below. Beware that
	// exactly one version must not specify a target size. It means that versions with
	// a target size will respect the setting, and the one without target size will
	// be applied to all remaining Instances (top level target_size - each version target_size).
	// This property is in beta, and should be used with the terraform-provider-google-beta provider.
	// See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta fields.
	Versions interface{}
	// Whether to wait for all instances to be created/updated before
	// returning. Note that if this is set to true and the operation does not succeed, Terraform will
	// continue trying until it times out.
	WaitForInstances interface{}
	// The zone that instances in this group should be created
	// in.
	Zone interface{}
}

// The set of arguments for constructing a InstanceGroupManager resource.
type InstanceGroupManagerArgs struct {
	// The autohealing policies for this managed instance
	// group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).
	// This property is in beta, and should be used with the terraform-provider-google-beta provider.
	// See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta fields.
	AutoHealingPolicies interface{}
	// The base instance name to use for
	// instances in this group. The value must be a valid
	// [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
	// are lowercase letters, numbers, and hyphens (-). Instances are named by
	// appending a hyphen and a random four-character string to the base instance
	// name.
	BaseInstanceName interface{}
	// An optional textual description of the instance
	// group manager.
	Description interface{}
	// - The full URL to an instance template from which all new instances of this version will be created.
	InstanceTemplate interface{}
	// - Version name.
	Name interface{}
	// The named port configuration. See the section below
	// for details on configuration.
	NamedPorts interface{}
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project interface{}
	// The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch)
	// This property is in beta, and should be used with the terraform-provider-google-beta provider.
	// See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta fields.
	// - - -
	RollingUpdatePolicy interface{}
	// The full URL of all target pools to which new
	// instances in the group are added. Updating the target pools attribute does
	// not affect existing instances.
	TargetPools interface{}
	// - The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.
	TargetSize interface{}
	// If the `instance_template`
	// resource is modified, a value of `"NONE"` will prevent any of the managed
	// instances from being restarted by Terraform. A value of `"REPLACE"` will
	// restart all of the instances at once. `"ROLLING_UPDATE"` is supported as a beta feature.
	// A value of `"ROLLING_UPDATE"` requires `rolling_update_policy` block to be set
	UpdateStrategy interface{}
	// Application versions managed by this instance group. Each
	// version deals with a specific instance template, allowing canary release scenarios.
	// Conflicts with `instance_template`. Structure is documented below. Beware that
	// exactly one version must not specify a target size. It means that versions with
	// a target size will respect the setting, and the one without target size will
	// be applied to all remaining Instances (top level target_size - each version target_size).
	// This property is in beta, and should be used with the terraform-provider-google-beta provider.
	// See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta fields.
	Versions interface{}
	// Whether to wait for all instances to be created/updated before
	// returning. Note that if this is set to true and the operation does not succeed, Terraform will
	// continue trying until it times out.
	WaitForInstances interface{}
	// The zone that instances in this group should be created
	// in.
	Zone interface{}
}
