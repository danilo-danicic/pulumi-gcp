// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package monitoring

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

func LookupNotificationChannel(ctx *pulumi.Context, args *LookupNotificationChannelArgs, opts ...pulumi.InvokeOption) (*LookupNotificationChannelResult, error) {
	var rv LookupNotificationChannelResult
	err := ctx.Invoke("gcp:monitoring/getNotificationChannel:getNotificationChannel", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNotificationChannel.
type LookupNotificationChannelArgs struct {
	DisplayName *string           `pulumi:"displayName"`
	Labels      map[string]string `pulumi:"labels"`
	Project     *string           `pulumi:"project"`
	Type        *string           `pulumi:"type"`
	UserLabels  map[string]string `pulumi:"userLabels"`
}

// A collection of values returned by getNotificationChannel.
type LookupNotificationChannelResult struct {
	Description string  `pulumi:"description"`
	DisplayName *string `pulumi:"displayName"`
	Enabled     bool    `pulumi:"enabled"`
	// id is the provider-assigned unique ID for this managed resource.
	Id                 string            `pulumi:"id"`
	Labels             map[string]string `pulumi:"labels"`
	Name               string            `pulumi:"name"`
	Project            *string           `pulumi:"project"`
	Type               *string           `pulumi:"type"`
	UserLabels         map[string]string `pulumi:"userLabels"`
	VerificationStatus string            `pulumi:"verificationStatus"`
}
