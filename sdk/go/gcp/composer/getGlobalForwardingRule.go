// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package composer

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Get a global forwarding rule within GCE from its name.
func GetGlobalForwardingRule(ctx *pulumi.Context, args *GetGlobalForwardingRuleArgs, opts ...pulumi.InvokeOption) (*GetGlobalForwardingRuleResult, error) {
	var rv GetGlobalForwardingRuleResult
	err := ctx.Invoke("gcp:composer/getGlobalForwardingRule:getGlobalForwardingRule", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGlobalForwardingRule.
type GetGlobalForwardingRuleArgs struct {
	// The name of the global forwarding rule.
	Name string `pulumi:"name"`
	// The project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project *string `pulumi:"project"`
}

// A collection of values returned by getGlobalForwardingRule.
type GetGlobalForwardingRuleResult struct {
	Description string `pulumi:"description"`
	// The provider-assigned unique ID for this managed resource.
	Id                  string                                  `pulumi:"id"`
	IpAddress           string                                  `pulumi:"ipAddress"`
	IpProtocol          string                                  `pulumi:"ipProtocol"`
	IpVersion           string                                  `pulumi:"ipVersion"`
	LabelFingerprint    string                                  `pulumi:"labelFingerprint"`
	Labels              map[string]string                       `pulumi:"labels"`
	LoadBalancingScheme string                                  `pulumi:"loadBalancingScheme"`
	MetadataFilters     []GetGlobalForwardingRuleMetadataFilter `pulumi:"metadataFilters"`
	Name                string                                  `pulumi:"name"`
	Network             string                                  `pulumi:"network"`
	PortRange           string                                  `pulumi:"portRange"`
	Project             *string                                 `pulumi:"project"`
	SelfLink            string                                  `pulumi:"selfLink"`
	Target              string                                  `pulumi:"target"`
}