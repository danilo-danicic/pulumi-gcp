// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datacatalog

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
	case "gcp:datacatalog/entry:Entry":
		r, err = NewEntry(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/entryGroup:EntryGroup":
		r, err = NewEntryGroup(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/entryGroupIamBinding:EntryGroupIamBinding":
		r, err = NewEntryGroupIamBinding(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/entryGroupIamMember:EntryGroupIamMember":
		r, err = NewEntryGroupIamMember(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/entryGroupIamPolicy:EntryGroupIamPolicy":
		r, err = NewEntryGroupIamPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/policyTag:PolicyTag":
		r, err = NewPolicyTag(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/policyTagIamBinding:PolicyTagIamBinding":
		r, err = NewPolicyTagIamBinding(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/policyTagIamMember:PolicyTagIamMember":
		r, err = NewPolicyTagIamMember(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/policyTagIamPolicy:PolicyTagIamPolicy":
		r, err = NewPolicyTagIamPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/tag:Tag":
		r, err = NewTag(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/tagTemplate:TagTemplate":
		r, err = NewTagTemplate(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/taxonomy:Taxonomy":
		r, err = NewTaxonomy(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/taxonomyIamBinding:TaxonomyIamBinding":
		r, err = NewTaxonomyIamBinding(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/taxonomyIamMember:TaxonomyIamMember":
		r, err = NewTaxonomyIamMember(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:datacatalog/taxonomyIamPolicy:TaxonomyIamPolicy":
		r, err = NewTaxonomyIamPolicy(ctx, name, nil, pulumi.URN_(urn))
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
		"datacatalog/entry",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/entryGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/entryGroupIamBinding",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/entryGroupIamMember",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/entryGroupIamPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/policyTag",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/policyTagIamBinding",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/policyTagIamMember",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/policyTagIamPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/tag",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/tagTemplate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/taxonomy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/taxonomyIamBinding",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/taxonomyIamMember",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"datacatalog/taxonomyIamPolicy",
		&module{version},
	)
}
