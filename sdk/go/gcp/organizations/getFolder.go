// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package organizations

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get information about a Google Cloud Folder.
func LookupFolder(ctx *pulumi.Context, args *GetFolderArgs) (*GetFolderResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["folder"] = args.Folder
		inputs["lookupOrganization"] = args.LookupOrganization
	}
	outputs, err := ctx.Invoke("gcp:organizations/getFolder:getFolder", inputs)
	if err != nil {
		return nil, err
	}
	return &GetFolderResult{
		CreateTime: outputs["createTime"],
		DisplayName: outputs["displayName"],
		LifecycleState: outputs["lifecycleState"],
		Name: outputs["name"],
		Organization: outputs["organization"],
		Parent: outputs["parent"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getFolder.
type GetFolderArgs struct {
	// The name of the Folder in the form `{folder_id}` or `folders/{folder_id}`.
	Folder interface{}
	// `true` to find the organization that the folder belongs, `false` to avoid the lookup. It searches up the tree. (defaults to `false`)
	LookupOrganization interface{}
}

// A collection of values returned by getFolder.
type GetFolderResult struct {
	// Timestamp when the Organization was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
	CreateTime interface{}
	// The folder's display name.
	DisplayName interface{}
	// The Folder's current lifecycle state.
	LifecycleState interface{}
	// The resource name of the Folder in the form `folders/{folder_id}`.
	Name interface{}
	// If `lookup_organization` is enable, the resource name of the Organization that the folder belongs.
	Organization interface{}
	// The resource name of the parent Folder or Organization.
	Parent interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
