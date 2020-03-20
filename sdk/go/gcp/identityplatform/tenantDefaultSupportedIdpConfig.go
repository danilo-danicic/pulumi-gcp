// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package identityplatform

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type TenantDefaultSupportedIdpConfig struct {
	pulumi.CustomResourceState

	// OAuth client ID
	ClientId pulumi.StringOutput `pulumi:"clientId"`
	// OAuth client secret
	ClientSecret pulumi.StringOutput `pulumi:"clientSecret"`
	// If this IDP allows the user to sign in
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// ID of the IDP. Possible values include: * 'apple.com' * 'facebook.com' * 'gc.apple.com' * 'github.com' * 'google.com' *
	// 'linkedin.com' * 'microsoft.com' * 'playgames.google.com' * 'twitter.com' * 'yahoo.com'
	IdpId pulumi.StringOutput `pulumi:"idpId"`
	// The name of the default supported IDP config resource
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The name of the tenant where this DefaultSupportedIdpConfig resource exists
	Tenant pulumi.StringOutput `pulumi:"tenant"`
}

// NewTenantDefaultSupportedIdpConfig registers a new resource with the given unique name, arguments, and options.
func NewTenantDefaultSupportedIdpConfig(ctx *pulumi.Context,
	name string, args *TenantDefaultSupportedIdpConfigArgs, opts ...pulumi.ResourceOption) (*TenantDefaultSupportedIdpConfig, error) {
	if args == nil || args.ClientId == nil {
		return nil, errors.New("missing required argument 'ClientId'")
	}
	if args == nil || args.ClientSecret == nil {
		return nil, errors.New("missing required argument 'ClientSecret'")
	}
	if args == nil || args.IdpId == nil {
		return nil, errors.New("missing required argument 'IdpId'")
	}
	if args == nil || args.Tenant == nil {
		return nil, errors.New("missing required argument 'Tenant'")
	}
	if args == nil {
		args = &TenantDefaultSupportedIdpConfigArgs{}
	}
	var resource TenantDefaultSupportedIdpConfig
	err := ctx.RegisterResource("gcp:identityplatform/tenantDefaultSupportedIdpConfig:TenantDefaultSupportedIdpConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTenantDefaultSupportedIdpConfig gets an existing TenantDefaultSupportedIdpConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTenantDefaultSupportedIdpConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TenantDefaultSupportedIdpConfigState, opts ...pulumi.ResourceOption) (*TenantDefaultSupportedIdpConfig, error) {
	var resource TenantDefaultSupportedIdpConfig
	err := ctx.ReadResource("gcp:identityplatform/tenantDefaultSupportedIdpConfig:TenantDefaultSupportedIdpConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TenantDefaultSupportedIdpConfig resources.
type tenantDefaultSupportedIdpConfigState struct {
	// OAuth client ID
	ClientId *string `pulumi:"clientId"`
	// OAuth client secret
	ClientSecret *string `pulumi:"clientSecret"`
	// If this IDP allows the user to sign in
	Enabled *bool `pulumi:"enabled"`
	// ID of the IDP. Possible values include: * 'apple.com' * 'facebook.com' * 'gc.apple.com' * 'github.com' * 'google.com' *
	// 'linkedin.com' * 'microsoft.com' * 'playgames.google.com' * 'twitter.com' * 'yahoo.com'
	IdpId *string `pulumi:"idpId"`
	// The name of the default supported IDP config resource
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The name of the tenant where this DefaultSupportedIdpConfig resource exists
	Tenant *string `pulumi:"tenant"`
}

type TenantDefaultSupportedIdpConfigState struct {
	// OAuth client ID
	ClientId pulumi.StringPtrInput
	// OAuth client secret
	ClientSecret pulumi.StringPtrInput
	// If this IDP allows the user to sign in
	Enabled pulumi.BoolPtrInput
	// ID of the IDP. Possible values include: * 'apple.com' * 'facebook.com' * 'gc.apple.com' * 'github.com' * 'google.com' *
	// 'linkedin.com' * 'microsoft.com' * 'playgames.google.com' * 'twitter.com' * 'yahoo.com'
	IdpId pulumi.StringPtrInput
	// The name of the default supported IDP config resource
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The name of the tenant where this DefaultSupportedIdpConfig resource exists
	Tenant pulumi.StringPtrInput
}

func (TenantDefaultSupportedIdpConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*tenantDefaultSupportedIdpConfigState)(nil)).Elem()
}

type tenantDefaultSupportedIdpConfigArgs struct {
	// OAuth client ID
	ClientId string `pulumi:"clientId"`
	// OAuth client secret
	ClientSecret string `pulumi:"clientSecret"`
	// If this IDP allows the user to sign in
	Enabled *bool `pulumi:"enabled"`
	// ID of the IDP. Possible values include: * 'apple.com' * 'facebook.com' * 'gc.apple.com' * 'github.com' * 'google.com' *
	// 'linkedin.com' * 'microsoft.com' * 'playgames.google.com' * 'twitter.com' * 'yahoo.com'
	IdpId string `pulumi:"idpId"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The name of the tenant where this DefaultSupportedIdpConfig resource exists
	Tenant string `pulumi:"tenant"`
}

// The set of arguments for constructing a TenantDefaultSupportedIdpConfig resource.
type TenantDefaultSupportedIdpConfigArgs struct {
	// OAuth client ID
	ClientId pulumi.StringInput
	// OAuth client secret
	ClientSecret pulumi.StringInput
	// If this IDP allows the user to sign in
	Enabled pulumi.BoolPtrInput
	// ID of the IDP. Possible values include: * 'apple.com' * 'facebook.com' * 'gc.apple.com' * 'github.com' * 'google.com' *
	// 'linkedin.com' * 'microsoft.com' * 'playgames.google.com' * 'twitter.com' * 'yahoo.com'
	IdpId pulumi.StringInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The name of the tenant where this DefaultSupportedIdpConfig resource exists
	Tenant pulumi.StringInput
}

func (TenantDefaultSupportedIdpConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tenantDefaultSupportedIdpConfigArgs)(nil)).Elem()
}
