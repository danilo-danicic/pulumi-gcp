// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package organizations

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get OpenID userinfo about the credentials used with the Google provider,
// specifically the email.
// 
// When the `https://www.googleapis.com/auth/userinfo.email` scope is enabled in
// your provider block, this datasource enables you to export the email of the
// account you've authenticated the provider with; this can be used alongside
// `data.google_client_config`'s `access_token` to perform OpenID Connect
// authentication with GKE and configure an RBAC role for the email used.
// 
// > This resource will only work as expected if the provider is configured to
// use the `https://www.googleapis.com/auth/userinfo.email` scope! You will
// receive an error otherwise.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/client_openid_userinfo.html.markdown.
func LookupClientOpenIdUserInfo(ctx *pulumi.Context) (*GetClientOpenIdUserInfoResult, error) {
	outputs, err := ctx.Invoke("gcp:organizations/getClientOpenIdUserInfo:getClientOpenIdUserInfo", nil)
	if err != nil {
		return nil, err
	}
	return &GetClientOpenIdUserInfoResult{
		Email: outputs["email"],
		Id: outputs["id"],
	}, nil
}

// A collection of values returned by getClientOpenIdUserInfo.
type GetClientOpenIdUserInfoResult struct {
	// The email of the account used by the provider to authenticate with GCP.
	Email interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
