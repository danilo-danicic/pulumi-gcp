// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package billing

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-gcp/sdk/v4/go/gcp"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "gcp:billing/accountIamBinding:AccountIamBinding":
		r, err = NewAccountIamBinding(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:billing/accountIamMember:AccountIamMember":
		r, err = NewAccountIamMember(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:billing/accountIamPolicy:AccountIamPolicy":
		r, err = NewAccountIamPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:billing/budget:Budget":
		r, err = NewBudget(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:billing/subAccount:SubAccount":
		r, err = NewSubAccount(ctx, name, nil, pulumi.URN_(urn))
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	return
}

func init() {
	version, err := gcp.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"gcp",
		"billing/accountIamBinding",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"billing/accountIamMember",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"billing/accountIamPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"billing/budget",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"billing/subAccount",
		&module{version},
	)
}
