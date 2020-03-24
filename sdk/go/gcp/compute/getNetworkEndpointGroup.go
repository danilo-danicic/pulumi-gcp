// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to access a Network Endpoint Group's attributes.
//
// The NEG may be found by providing either a `selfLink`, or a `name` and a `zone`.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_compute_network_endpoint_group.html.markdown.
func LookupNetworkEndpointGroup(ctx *pulumi.Context, args *LookupNetworkEndpointGroupArgs, opts ...pulumi.InvokeOption) (*LookupNetworkEndpointGroupResult, error) {
	var rv LookupNetworkEndpointGroupResult
	err := ctx.Invoke("gcp:compute/getNetworkEndpointGroup:getNetworkEndpointGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNetworkEndpointGroup.
type LookupNetworkEndpointGroupArgs struct {
	// The Network Endpoint Group name.
	// Provide either this or a `selfLink`.
	Name *string `pulumi:"name"`
	// The Network Endpoint Group self\_link.
	SelfLink *string `pulumi:"selfLink"`
	// The Network Endpoint Group availability zone.
	Zone *string `pulumi:"zone"`
}


// A collection of values returned by getNetworkEndpointGroup.
type LookupNetworkEndpointGroupResult struct {
	// The NEG default port.
	DefaultPort int `pulumi:"defaultPort"`
	// The NEG description.
	Description string `pulumi:"description"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	Name *string `pulumi:"name"`
	// The network to which all network endpoints in the NEG belong.
	Network string `pulumi:"network"`
	// Type of network endpoints in this network endpoint group.
	NetworkEndpointType string `pulumi:"networkEndpointType"`
	Project string `pulumi:"project"`
	SelfLink *string `pulumi:"selfLink"`
	// Number of network endpoints in the network endpoint group.
	Size int `pulumi:"size"`
	// subnetwork to which all network endpoints in the NEG belong.
	Subnetwork string `pulumi:"subnetwork"`
	Zone *string `pulumi:"zone"`
}

