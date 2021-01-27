// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Represents an Autoscaler resource.
//
// Autoscalers allow you to automatically scale virtual machine instances in
// managed instance groups according to an autoscaling policy that you
// define.
//
// To get more information about Autoscaler, see:
//
// * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/autoscalers)
// * How-to Guides
//     * [Autoscaling Groups of Instances](https://cloud.google.com/compute/docs/autoscaler/)
//
// ## Example Usage
// ### Autoscaler Single Instance
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-gcp/sdk/v4/go/gcp/compute"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "debian-9"
// 		opt1 := "debian-cloud"
// 		debian9, err := compute.LookupImage(ctx, &compute.LookupImageArgs{
// 			Family:  &opt0,
// 			Project: &opt1,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		defaultInstanceTemplate, err := compute.NewInstanceTemplate(ctx, "defaultInstanceTemplate", &compute.InstanceTemplateArgs{
// 			MachineType:  pulumi.String("e2-medium"),
// 			CanIpForward: pulumi.Bool(false),
// 			Tags: pulumi.StringArray{
// 				pulumi.String("foo"),
// 				pulumi.String("bar"),
// 			},
// 			Disks: compute.InstanceTemplateDiskArray{
// 				&compute.InstanceTemplateDiskArgs{
// 					SourceImage: pulumi.String(debian9.Id),
// 				},
// 			},
// 			NetworkInterfaces: compute.InstanceTemplateNetworkInterfaceArray{
// 				&compute.InstanceTemplateNetworkInterfaceArgs{
// 					Network: pulumi.String("default"),
// 				},
// 			},
// 			Metadata: pulumi.StringMap{
// 				"foo": pulumi.String("bar"),
// 			},
// 			ServiceAccount: &compute.InstanceTemplateServiceAccountArgs{
// 				Scopes: pulumi.StringArray{
// 					pulumi.String("userinfo-email"),
// 					pulumi.String("compute-ro"),
// 					pulumi.String("storage-ro"),
// 				},
// 			},
// 		}, pulumi.Provider(google_beta))
// 		if err != nil {
// 			return err
// 		}
// 		defaultTargetPool, err := compute.NewTargetPool(ctx, "defaultTargetPool", nil, pulumi.Provider(google_beta))
// 		if err != nil {
// 			return err
// 		}
// 		defaultInstanceGroupManager, err := compute.NewInstanceGroupManager(ctx, "defaultInstanceGroupManager", &compute.InstanceGroupManagerArgs{
// 			Zone: pulumi.String("us-central1-f"),
// 			Versions: compute.InstanceGroupManagerVersionArray{
// 				&compute.InstanceGroupManagerVersionArgs{
// 					InstanceTemplate: defaultInstanceTemplate.ID(),
// 					Name:             pulumi.String("primary"),
// 				},
// 			},
// 			TargetPools: pulumi.StringArray{
// 				defaultTargetPool.ID(),
// 			},
// 			BaseInstanceName: pulumi.String("autoscaler-sample"),
// 		}, pulumi.Provider(google_beta))
// 		if err != nil {
// 			return err
// 		}
// 		_, err = compute.NewAutoscaler(ctx, "defaultAutoscaler", &compute.AutoscalerArgs{
// 			Zone:   pulumi.String("us-central1-f"),
// 			Target: defaultInstanceGroupManager.ID(),
// 			AutoscalingPolicy: &compute.AutoscalerAutoscalingPolicyArgs{
// 				MaxReplicas:    pulumi.Int(5),
// 				MinReplicas:    pulumi.Int(1),
// 				CooldownPeriod: pulumi.Int(60),
// 				Metrics: compute.AutoscalerAutoscalingPolicyMetricArray{
// 					&compute.AutoscalerAutoscalingPolicyMetricArgs{
// 						Name:                     pulumi.String("pubsub.googleapis.com/subscription/num_undelivered_messages"),
// 						Filter:                   pulumi.String("resource.type = pubsub_subscription AND resource.label.subscription_id = our-subscription"),
// 						SingleInstanceAssignment: pulumi.Float64(65535),
// 					},
// 				},
// 			},
// 		}, pulumi.Provider(google_beta))
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Autoscaler Basic
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-gcp/sdk/v4/go/gcp/compute"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "debian-9"
// 		opt1 := "debian-cloud"
// 		debian9, err := compute.LookupImage(ctx, &compute.LookupImageArgs{
// 			Family:  &opt0,
// 			Project: &opt1,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		foobarInstanceTemplate, err := compute.NewInstanceTemplate(ctx, "foobarInstanceTemplate", &compute.InstanceTemplateArgs{
// 			MachineType:  pulumi.String("e2-medium"),
// 			CanIpForward: pulumi.Bool(false),
// 			Tags: pulumi.StringArray{
// 				pulumi.String("foo"),
// 				pulumi.String("bar"),
// 			},
// 			Disks: compute.InstanceTemplateDiskArray{
// 				&compute.InstanceTemplateDiskArgs{
// 					SourceImage: pulumi.String(debian9.Id),
// 				},
// 			},
// 			NetworkInterfaces: compute.InstanceTemplateNetworkInterfaceArray{
// 				&compute.InstanceTemplateNetworkInterfaceArgs{
// 					Network: pulumi.String("default"),
// 				},
// 			},
// 			Metadata: pulumi.StringMap{
// 				"foo": pulumi.String("bar"),
// 			},
// 			ServiceAccount: &compute.InstanceTemplateServiceAccountArgs{
// 				Scopes: pulumi.StringArray{
// 					pulumi.String("userinfo-email"),
// 					pulumi.String("compute-ro"),
// 					pulumi.String("storage-ro"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		foobarTargetPool, err := compute.NewTargetPool(ctx, "foobarTargetPool", nil)
// 		if err != nil {
// 			return err
// 		}
// 		foobarInstanceGroupManager, err := compute.NewInstanceGroupManager(ctx, "foobarInstanceGroupManager", &compute.InstanceGroupManagerArgs{
// 			Zone: pulumi.String("us-central1-f"),
// 			Versions: compute.InstanceGroupManagerVersionArray{
// 				&compute.InstanceGroupManagerVersionArgs{
// 					InstanceTemplate: foobarInstanceTemplate.ID(),
// 					Name:             pulumi.String("primary"),
// 				},
// 			},
// 			TargetPools: pulumi.StringArray{
// 				foobarTargetPool.ID(),
// 			},
// 			BaseInstanceName: pulumi.String("foobar"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = compute.NewAutoscaler(ctx, "foobarAutoscaler", &compute.AutoscalerArgs{
// 			Zone:   pulumi.String("us-central1-f"),
// 			Target: foobarInstanceGroupManager.ID(),
// 			AutoscalingPolicy: &compute.AutoscalerAutoscalingPolicyArgs{
// 				MaxReplicas:    pulumi.Int(5),
// 				MinReplicas:    pulumi.Int(1),
// 				CooldownPeriod: pulumi.Int(60),
// 				CpuUtilization: &compute.AutoscalerAutoscalingPolicyCpuUtilizationArgs{
// 					Target: pulumi.Float64(0.5),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// Autoscaler can be imported using any of these accepted formats
//
// ```sh
//  $ pulumi import gcp:compute/autoscalar:Autoscalar default projects/{{project}}/zones/{{zone}}/autoscalers/{{name}}
// ```
//
// ```sh
//  $ pulumi import gcp:compute/autoscalar:Autoscalar default {{project}}/{{zone}}/{{name}}
// ```
//
// ```sh
//  $ pulumi import gcp:compute/autoscalar:Autoscalar default {{zone}}/{{name}}
// ```
//
// ```sh
//  $ pulumi import gcp:compute/autoscalar:Autoscalar default {{name}}
// ```
//
// Deprecated: gcp.compute.Autoscalar has been deprecated in favor of gcp.compute.Autoscaler
type Autoscalar struct {
	pulumi.CustomResourceState

	// The configuration parameters for the autoscaling algorithm. You can
	// define one or more of the policies for an autoscaler: cpuUtilization,
	// customMetricUtilizations, and loadBalancingUtilization.
	// If none of these are specified, the default will be to autoscale based
	// on cpuUtilization to 0.6 or 60%.
	// Structure is documented below.
	AutoscalingPolicy AutoscalarAutoscalingPolicyOutput `pulumi:"autoscalingPolicy"`
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringOutput `pulumi:"creationTimestamp"`
	// An optional description of this resource.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The identifier for this object. Format specified above.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// Fraction of backend capacity utilization (set in HTTP(s) load
	// balancing configuration) that autoscaler should maintain. Must
	// be a positive float value. If not defined, the default is 0.8.
	Target pulumi.StringOutput `pulumi:"target"`
	// URL of the zone where the instance group resides.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewAutoscalar registers a new resource with the given unique name, arguments, and options.
func NewAutoscalar(ctx *pulumi.Context,
	name string, args *AutoscalarArgs, opts ...pulumi.ResourceOption) (*Autoscalar, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AutoscalingPolicy == nil {
		return nil, errors.New("invalid value for required argument 'AutoscalingPolicy'")
	}
	if args.Target == nil {
		return nil, errors.New("invalid value for required argument 'Target'")
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
	// The configuration parameters for the autoscaling algorithm. You can
	// define one or more of the policies for an autoscaler: cpuUtilization,
	// customMetricUtilizations, and loadBalancingUtilization.
	// If none of these are specified, the default will be to autoscale based
	// on cpuUtilization to 0.6 or 60%.
	// Structure is documented below.
	AutoscalingPolicy *AutoscalarAutoscalingPolicy `pulumi:"autoscalingPolicy"`
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp *string `pulumi:"creationTimestamp"`
	// An optional description of this resource.
	Description *string `pulumi:"description"`
	// The identifier for this object. Format specified above.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// Fraction of backend capacity utilization (set in HTTP(s) load
	// balancing configuration) that autoscaler should maintain. Must
	// be a positive float value. If not defined, the default is 0.8.
	Target *string `pulumi:"target"`
	// URL of the zone where the instance group resides.
	Zone *string `pulumi:"zone"`
}

type AutoscalarState struct {
	// The configuration parameters for the autoscaling algorithm. You can
	// define one or more of the policies for an autoscaler: cpuUtilization,
	// customMetricUtilizations, and loadBalancingUtilization.
	// If none of these are specified, the default will be to autoscale based
	// on cpuUtilization to 0.6 or 60%.
	// Structure is documented below.
	AutoscalingPolicy AutoscalarAutoscalingPolicyPtrInput
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringPtrInput
	// An optional description of this resource.
	Description pulumi.StringPtrInput
	// The identifier for this object. Format specified above.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
	// Fraction of backend capacity utilization (set in HTTP(s) load
	// balancing configuration) that autoscaler should maintain. Must
	// be a positive float value. If not defined, the default is 0.8.
	Target pulumi.StringPtrInput
	// URL of the zone where the instance group resides.
	Zone pulumi.StringPtrInput
}

func (AutoscalarState) ElementType() reflect.Type {
	return reflect.TypeOf((*autoscalarState)(nil)).Elem()
}

type autoscalarArgs struct {
	// The configuration parameters for the autoscaling algorithm. You can
	// define one or more of the policies for an autoscaler: cpuUtilization,
	// customMetricUtilizations, and loadBalancingUtilization.
	// If none of these are specified, the default will be to autoscale based
	// on cpuUtilization to 0.6 or 60%.
	// Structure is documented below.
	AutoscalingPolicy AutoscalarAutoscalingPolicy `pulumi:"autoscalingPolicy"`
	// An optional description of this resource.
	Description *string `pulumi:"description"`
	// The identifier for this object. Format specified above.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Fraction of backend capacity utilization (set in HTTP(s) load
	// balancing configuration) that autoscaler should maintain. Must
	// be a positive float value. If not defined, the default is 0.8.
	Target string `pulumi:"target"`
	// URL of the zone where the instance group resides.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a Autoscalar resource.
type AutoscalarArgs struct {
	// The configuration parameters for the autoscaling algorithm. You can
	// define one or more of the policies for an autoscaler: cpuUtilization,
	// customMetricUtilizations, and loadBalancingUtilization.
	// If none of these are specified, the default will be to autoscale based
	// on cpuUtilization to 0.6 or 60%.
	// Structure is documented below.
	AutoscalingPolicy AutoscalarAutoscalingPolicyInput
	// An optional description of this resource.
	Description pulumi.StringPtrInput
	// The identifier for this object. Format specified above.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Fraction of backend capacity utilization (set in HTTP(s) load
	// balancing configuration) that autoscaler should maintain. Must
	// be a positive float value. If not defined, the default is 0.8.
	Target pulumi.StringInput
	// URL of the zone where the instance group resides.
	Zone pulumi.StringPtrInput
}

func (AutoscalarArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*autoscalarArgs)(nil)).Elem()
}

type AutoscalarInput interface {
	pulumi.Input

	ToAutoscalarOutput() AutoscalarOutput
	ToAutoscalarOutputWithContext(ctx context.Context) AutoscalarOutput
}

func (Autoscalar) ElementType() reflect.Type {
	return reflect.TypeOf((*Autoscalar)(nil)).Elem()
}

func (i Autoscalar) ToAutoscalarOutput() AutoscalarOutput {
	return i.ToAutoscalarOutputWithContext(context.Background())
}

func (i Autoscalar) ToAutoscalarOutputWithContext(ctx context.Context) AutoscalarOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AutoscalarOutput)
}

type AutoscalarOutput struct {
	*pulumi.OutputState
}

func (AutoscalarOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AutoscalarOutput)(nil)).Elem()
}

func (o AutoscalarOutput) ToAutoscalarOutput() AutoscalarOutput {
	return o
}

func (o AutoscalarOutput) ToAutoscalarOutputWithContext(ctx context.Context) AutoscalarOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(AutoscalarOutput{})
}
