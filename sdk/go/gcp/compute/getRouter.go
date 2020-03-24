// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get a router within GCE from its name and VPC.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_compute_router.html.markdown.
func LookupRouter(ctx *pulumi.Context, args *LookupRouterArgs, opts ...pulumi.InvokeOption) (*LookupRouterResult, error) {
	var rv LookupRouterResult
	err := ctx.Invoke("gcp:compute/getRouter:getRouter", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRouter.
type LookupRouterArgs struct {
	// The name of the router.
	Name string `pulumi:"name"`
	// The VPC network on which this router lives.
	Network string `pulumi:"network"`
	// The ID of the project in which the resource
	// belongs. If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The region this router has been created in. If
	// unspecified, this defaults to the region configured in the provider.
	Region *string `pulumi:"region"`
}


// A collection of values returned by getRouter.
type LookupRouterResult struct {
	Bgps []GetRouterBgp `pulumi:"bgps"`
	CreationTimestamp string `pulumi:"creationTimestamp"`
	Description string `pulumi:"description"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	Name string `pulumi:"name"`
	Network string `pulumi:"network"`
	Project *string `pulumi:"project"`
	Region *string `pulumi:"region"`
	SelfLink string `pulumi:"selfLink"`
}

