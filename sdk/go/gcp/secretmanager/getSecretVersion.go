// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package secretmanager

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

func LookupSecretVersion(ctx *pulumi.Context, args *LookupSecretVersionArgs, opts ...pulumi.InvokeOption) (*LookupSecretVersionResult, error) {
	var rv LookupSecretVersionResult
	err := ctx.Invoke("gcp:secretmanager/getSecretVersion:getSecretVersion", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSecretVersion.
type LookupSecretVersionArgs struct {
	Project *string `pulumi:"project"`
	Secret  string  `pulumi:"secret"`
	Version *string `pulumi:"version"`
}

// A collection of values returned by getSecretVersion.
type LookupSecretVersionResult struct {
	CreateTime  string `pulumi:"createTime"`
	DestroyTime string `pulumi:"destroyTime"`
	Enabled     bool   `pulumi:"enabled"`
	// id is the provider-assigned unique ID for this managed resource.
	Id         string `pulumi:"id"`
	Name       string `pulumi:"name"`
	Project    string `pulumi:"project"`
	Secret     string `pulumi:"secret"`
	SecretData string `pulumi:"secretData"`
	Version    string `pulumi:"version"`
}
