// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get information about a BackendBucket.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_compute_backend_bucket.html.markdown.
func LookupBackendBucket(ctx *pulumi.Context, args *LookupBackendBucketArgs, opts ...pulumi.InvokeOption) (*LookupBackendBucketResult, error) {
	var rv LookupBackendBucketResult
	err := ctx.Invoke("gcp:compute/getBackendBucket:getBackendBucket", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getBackendBucket.
type LookupBackendBucketArgs struct {
	// Name of the resource.
	Name string `pulumi:"name"`
	// The ID of the project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project *string `pulumi:"project"`
}


// A collection of values returned by getBackendBucket.
type LookupBackendBucketResult struct {
	// Cloud Storage bucket name.
	BucketName string `pulumi:"bucketName"`
	// Cloud CDN configuration for this Backend Bucket. Structure is documented below.
	CdnPolicies []GetBackendBucketCdnPolicy `pulumi:"cdnPolicies"`
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp string `pulumi:"creationTimestamp"`
	// An optional textual description of the resource; provided by the client when the resource is created.
	Description string `pulumi:"description"`
	// Whether Cloud CDN is enabled for this BackendBucket.
	EnableCdn bool `pulumi:"enableCdn"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	Name string `pulumi:"name"`
	Project *string `pulumi:"project"`
	// The URI of the created resource.
	SelfLink string `pulumi:"selfLink"`
}

