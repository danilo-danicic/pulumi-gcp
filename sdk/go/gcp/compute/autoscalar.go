// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type Autoscalar struct {
	pulumi.CustomResourceState

	// The configuration parameters for the autoscaling algorithm. You can define one or more of the policies for an
	// autoscaler: cpuUtilization, customMetricUtilizations, and loadBalancingUtilization. If none of these are specified, the
	// default will be to autoscale based on cpuUtilization to 0.6 or 60%.
	AutoscalingPolicy AutoscalarAutoscalingPolicyOutput `pulumi:"autoscalingPolicy"`
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringOutput `pulumi:"creationTimestamp"`
	// An optional description of this resource.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Name of the resource. The name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name    pulumi.StringOutput `pulumi:"name"`
	Project pulumi.StringOutput `pulumi:"project"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// URL of the managed instance group that this autoscaler will scale.
	Target pulumi.StringOutput `pulumi:"target"`
	// URL of the zone where the instance group resides.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewAutoscalar registers a new resource with the given unique name, arguments, and options.
func NewAutoscalar(ctx *pulumi.Context,
	name string, args *AutoscalarArgs, opts ...pulumi.ResourceOption) (*Autoscalar, error) {
	if args == nil || args.AutoscalingPolicy == nil {
		return nil, errors.New("missing required argument 'AutoscalingPolicy'")
	}
	if args == nil || args.Target == nil {
		return nil, errors.New("missing required argument 'Target'")
	}
	if args == nil {
		args = &AutoscalarArgs{}
	}
	var resource Autoscalar
	err := ctx.RegisterResource("gcp:compute/autoscalar:Autoscalar", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAutoscalar gets an existing Autoscalar resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAutoscalar(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AutoscalarState, opts ...pulumi.ResourceOption) (*Autoscalar, error) {
	var resource Autoscalar
	err := ctx.ReadResource("gcp:compute/autoscalar:Autoscalar", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Autoscalar resources.
type autoscalarState struct {
	// The configuration parameters for the autoscaling algorithm. You can define one or more of the policies for an
	// autoscaler: cpuUtilization, customMetricUtilizations, and loadBalancingUtilization. If none of these are specified, the
	// default will be to autoscale based on cpuUtilization to 0.6 or 60%.
	AutoscalingPolicy *AutoscalarAutoscalingPolicy `pulumi:"autoscalingPolicy"`
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp *string `pulumi:"creationTimestamp"`
	// An optional description of this resource.
	Description *string `pulumi:"description"`
	// Name of the resource. The name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name    *string `pulumi:"name"`
	Project *string `pulumi:"project"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// URL of the managed instance group that this autoscaler will scale.
	Target *string `pulumi:"target"`
	// URL of the zone where the instance group resides.
	Zone *string `pulumi:"zone"`
}

type AutoscalarState struct {
	// The configuration parameters for the autoscaling algorithm. You can define one or more of the policies for an
	// autoscaler: cpuUtilization, customMetricUtilizations, and loadBalancingUtilization. If none of these are specified, the
	// default will be to autoscale based on cpuUtilization to 0.6 or 60%.
	AutoscalingPolicy AutoscalarAutoscalingPolicyPtrInput
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringPtrInput
	// An optional description of this resource.
	Description pulumi.StringPtrInput
	// Name of the resource. The name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name    pulumi.StringPtrInput
	Project pulumi.StringPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
	// URL of the managed instance group that this autoscaler will scale.
	Target pulumi.StringPtrInput
	// URL of the zone where the instance group resides.
	Zone pulumi.StringPtrInput
}

func (AutoscalarState) ElementType() reflect.Type {
	return reflect.TypeOf((*autoscalarState)(nil)).Elem()
}

type autoscalarArgs struct {
	// The configuration parameters for the autoscaling algorithm. You can define one or more of the policies for an
	// autoscaler: cpuUtilization, customMetricUtilizations, and loadBalancingUtilization. If none of these are specified, the
	// default will be to autoscale based on cpuUtilization to 0.6 or 60%.
	AutoscalingPolicy AutoscalarAutoscalingPolicy `pulumi:"autoscalingPolicy"`
	// An optional description of this resource.
	Description *string `pulumi:"description"`
	// Name of the resource. The name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name    *string `pulumi:"name"`
	Project *string `pulumi:"project"`
	// URL of the managed instance group that this autoscaler will scale.
	Target string `pulumi:"target"`
	// URL of the zone where the instance group resides.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a Autoscalar resource.
type AutoscalarArgs struct {
	// The configuration parameters for the autoscaling algorithm. You can define one or more of the policies for an
	// autoscaler: cpuUtilization, customMetricUtilizations, and loadBalancingUtilization. If none of these are specified, the
	// default will be to autoscale based on cpuUtilization to 0.6 or 60%.
	AutoscalingPolicy AutoscalarAutoscalingPolicyInput
	// An optional description of this resource.
	Description pulumi.StringPtrInput
	// Name of the resource. The name must be 1-63 characters long and match the regular expression
	// '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
	// must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
	Name    pulumi.StringPtrInput
	Project pulumi.StringPtrInput
	// URL of the managed instance group that this autoscaler will scale.
	Target pulumi.StringInput
	// URL of the zone where the instance group resides.
	Zone pulumi.StringPtrInput
}

func (AutoscalarArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*autoscalarArgs)(nil)).Elem()
}
