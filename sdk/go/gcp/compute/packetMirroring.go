// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type PacketMirroring struct {
	pulumi.CustomResourceState

	// The Forwarding Rule resource (of type load_balancing_scheme=INTERNAL) that will be used as collector for mirrored
	// traffic. The specified forwarding rule must have is_mirroring_collector set to true.
	CollectorIlb PacketMirroringCollectorIlbOutput `pulumi:"collectorIlb"`
	// A human-readable description of the rule.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// A filter for mirrored traffic. If unset, all traffic is mirrored.
	Filter PacketMirroringFilterPtrOutput `pulumi:"filter"`
	// A means of specifying which resources to mirror.
	MirroredResources PacketMirroringMirroredResourcesOutput `pulumi:"mirroredResources"`
	// The name of the packet mirroring rule
	Name pulumi.StringOutput `pulumi:"name"`
	// Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in
	// the given network. All mirrored subnetworks should belong to the given network.
	Network PacketMirroringNetworkOutput `pulumi:"network"`
	// Since only one rule can be active at a time, priority is used to break ties in the case of two rules that apply to the
	// same instances.
	Priority pulumi.IntOutput    `pulumi:"priority"`
	Project  pulumi.StringOutput `pulumi:"project"`
	// The Region in which the created address should reside. If it is not provided, the provider region is used.
	Region pulumi.StringOutput `pulumi:"region"`
}

// NewPacketMirroring registers a new resource with the given unique name, arguments, and options.
func NewPacketMirroring(ctx *pulumi.Context,
	name string, args *PacketMirroringArgs, opts ...pulumi.ResourceOption) (*PacketMirroring, error) {
	if args == nil || args.CollectorIlb == nil {
		return nil, errors.New("missing required argument 'CollectorIlb'")
	}
	if args == nil || args.MirroredResources == nil {
		return nil, errors.New("missing required argument 'MirroredResources'")
	}
	if args == nil || args.Network == nil {
		return nil, errors.New("missing required argument 'Network'")
	}
	if args == nil {
		args = &PacketMirroringArgs{}
	}
	var resource PacketMirroring
	err := ctx.RegisterResource("gcp:compute/packetMirroring:PacketMirroring", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPacketMirroring gets an existing PacketMirroring resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPacketMirroring(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PacketMirroringState, opts ...pulumi.ResourceOption) (*PacketMirroring, error) {
	var resource PacketMirroring
	err := ctx.ReadResource("gcp:compute/packetMirroring:PacketMirroring", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PacketMirroring resources.
type packetMirroringState struct {
	// The Forwarding Rule resource (of type load_balancing_scheme=INTERNAL) that will be used as collector for mirrored
	// traffic. The specified forwarding rule must have is_mirroring_collector set to true.
	CollectorIlb *PacketMirroringCollectorIlb `pulumi:"collectorIlb"`
	// A human-readable description of the rule.
	Description *string `pulumi:"description"`
	// A filter for mirrored traffic. If unset, all traffic is mirrored.
	Filter *PacketMirroringFilter `pulumi:"filter"`
	// A means of specifying which resources to mirror.
	MirroredResources *PacketMirroringMirroredResources `pulumi:"mirroredResources"`
	// The name of the packet mirroring rule
	Name *string `pulumi:"name"`
	// Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in
	// the given network. All mirrored subnetworks should belong to the given network.
	Network *PacketMirroringNetwork `pulumi:"network"`
	// Since only one rule can be active at a time, priority is used to break ties in the case of two rules that apply to the
	// same instances.
	Priority *int    `pulumi:"priority"`
	Project  *string `pulumi:"project"`
	// The Region in which the created address should reside. If it is not provided, the provider region is used.
	Region *string `pulumi:"region"`
}

type PacketMirroringState struct {
	// The Forwarding Rule resource (of type load_balancing_scheme=INTERNAL) that will be used as collector for mirrored
	// traffic. The specified forwarding rule must have is_mirroring_collector set to true.
	CollectorIlb PacketMirroringCollectorIlbPtrInput
	// A human-readable description of the rule.
	Description pulumi.StringPtrInput
	// A filter for mirrored traffic. If unset, all traffic is mirrored.
	Filter PacketMirroringFilterPtrInput
	// A means of specifying which resources to mirror.
	MirroredResources PacketMirroringMirroredResourcesPtrInput
	// The name of the packet mirroring rule
	Name pulumi.StringPtrInput
	// Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in
	// the given network. All mirrored subnetworks should belong to the given network.
	Network PacketMirroringNetworkPtrInput
	// Since only one rule can be active at a time, priority is used to break ties in the case of two rules that apply to the
	// same instances.
	Priority pulumi.IntPtrInput
	Project  pulumi.StringPtrInput
	// The Region in which the created address should reside. If it is not provided, the provider region is used.
	Region pulumi.StringPtrInput
}

func (PacketMirroringState) ElementType() reflect.Type {
	return reflect.TypeOf((*packetMirroringState)(nil)).Elem()
}

type packetMirroringArgs struct {
	// The Forwarding Rule resource (of type load_balancing_scheme=INTERNAL) that will be used as collector for mirrored
	// traffic. The specified forwarding rule must have is_mirroring_collector set to true.
	CollectorIlb PacketMirroringCollectorIlb `pulumi:"collectorIlb"`
	// A human-readable description of the rule.
	Description *string `pulumi:"description"`
	// A filter for mirrored traffic. If unset, all traffic is mirrored.
	Filter *PacketMirroringFilter `pulumi:"filter"`
	// A means of specifying which resources to mirror.
	MirroredResources PacketMirroringMirroredResources `pulumi:"mirroredResources"`
	// The name of the packet mirroring rule
	Name *string `pulumi:"name"`
	// Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in
	// the given network. All mirrored subnetworks should belong to the given network.
	Network PacketMirroringNetwork `pulumi:"network"`
	// Since only one rule can be active at a time, priority is used to break ties in the case of two rules that apply to the
	// same instances.
	Priority *int    `pulumi:"priority"`
	Project  *string `pulumi:"project"`
	// The Region in which the created address should reside. If it is not provided, the provider region is used.
	Region *string `pulumi:"region"`
}

// The set of arguments for constructing a PacketMirroring resource.
type PacketMirroringArgs struct {
	// The Forwarding Rule resource (of type load_balancing_scheme=INTERNAL) that will be used as collector for mirrored
	// traffic. The specified forwarding rule must have is_mirroring_collector set to true.
	CollectorIlb PacketMirroringCollectorIlbInput
	// A human-readable description of the rule.
	Description pulumi.StringPtrInput
	// A filter for mirrored traffic. If unset, all traffic is mirrored.
	Filter PacketMirroringFilterPtrInput
	// A means of specifying which resources to mirror.
	MirroredResources PacketMirroringMirroredResourcesInput
	// The name of the packet mirroring rule
	Name pulumi.StringPtrInput
	// Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in
	// the given network. All mirrored subnetworks should belong to the given network.
	Network PacketMirroringNetworkInput
	// Since only one rule can be active at a time, priority is used to break ties in the case of two rules that apply to the
	// same instances.
	Priority pulumi.IntPtrInput
	Project  pulumi.StringPtrInput
	// The Region in which the created address should reside. If it is not provided, the provider region is used.
	Region pulumi.StringPtrInput
}

func (PacketMirroringArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*packetMirroringArgs)(nil)).Elem()
}
